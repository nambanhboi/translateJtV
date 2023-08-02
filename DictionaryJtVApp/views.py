from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import filters, viewsets,status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from .models import Sentence,Comment, Report, Contribute
from .serializers import UserSerializer,SentenceSeializer,CommentSeializer, reportSeializer,ContributetSeializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken

import json
from django.core import serializers
# from django.views.decorators.http import require_GET
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.conf import settings
# Create your views here.

#tạo ra 1 clas chứa tất cả phương thức get, put, pót, delete, filter
class SentenceViewSet(viewsets.ModelViewSet):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSeializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filteret_fields = ('sentenceJV', 'sentenceVN', 'style', 'topic')
    #các trường tìm kiếm
    search_fields = ('sentenceJV', 'sentenceVN', 'style', 'topic')
@api_view(['GET'])
# @authentication_classes([])
# @permission_classes([IsAuthenticated])
def get_username(request):
    user = request.user
    return Response({'username':user.username})

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = reportSeializer
    # def requestUser(request):
    #     request.user 

class ContributeViewSet(viewsets.ModelViewSet):
    queryset = Contribute.objects.all()
    serializer_class = ContributetSeializer
    
@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token = AuthToken.objects.create(user)
    return Response({
        'user':{
            'id' : user.id,
            'username': user.username,
        },
        'token': token.key, 
    })

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        # Tạo token cho người dùng vừa đăng ký
        refresh = RefreshToken.for_user(user)
        token = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(user_data, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
# #register
# class CustomerUserCreate(APIView):
#     def post(self, request, format='json'):
#         serializer = CustomerUserSerializer(data=request.data)

#         if serializer.is_valid():
#             user = serializer.save()
#             if user:
#                 refresh = RefreshToken.for_user(user)
#                 response_data = {
#                     'refresh': str(refresh),
#                     'access': str(refresh.access_token)
#                 }
#                 return Response(response_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# #login
# class CustomTokenObtainPairView(APIView):
#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = authenticate(username=username, password=password)

#         if user is not None:
#             refresh = RefreshToken.for_user(user)
#             response_data = {
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token)
#             }
#             return Response(response_data, status=status.HTTP_200_OK)
#         else:
#             return Response({'detail': 'No active account found with the given credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# class CustomerUserCreate(generics.CreateAPIView):
#     queryset = CustomerUser.objects.all()
#     serializer_class = CustomerUserSerializer

# class CustomTokenObtainPairView(APIView):
#     def post(self, request):
#         serializer = CustomerUserLoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = authenticate(
#             request,
#             username=serializer.validated_data['username'],
#             password=serializer.validated_data['password']
#         )
#         if user:
#             refresh = RefreshToken.for_user(user)
#             data = {
#                 'refresh_token': str(refresh),
#                 'access_token': str(refresh.access_token),
#                  'access_expires': int(settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].total_seconds()),
#                 'refresh_expires': int(settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'].total_seconds())
#             }
#             return Response(data, status=status.HTTP_200_OK)

#         return Response({
#             'error_message': 'username or password is incorrect!',
#             'error_code': 400
#         }, status=status.HTTP_400_BAD_REQUEST)
