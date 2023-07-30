from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import filters, viewsets,status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
<<<<<<< HEAD
from .models import Sentence,Comment
from .serializers import UserSerializer,SentenceSeializer,CommentSeializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken

=======
import json
from django.core import serializers
from .models import Sentence, CustomerUser
from .serializers import SentenceSeializer, CustomerUserSerializer, CustomerUserLoginSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.conf import settings
>>>>>>> ce2dde03f829450266422e67b2d8e86c5aa7e31b
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

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSeializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    
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
<<<<<<< HEAD

        return Response({"token": token, "user": serializer.data})   
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def login(request):
#     # Xử lý đăng nhập và kiểm tra thông tin người dùng
#     # Sau khi xác thực thành công, lấy thông tin người dùng
#     username = request.data.get('username')
#     password = request.data.get('password')

#     # Xác thực người dùng bằng cách sử dụng authenticate từ Django
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         # Tạo một đối tượng JSON chứa thông tin người dùng, bao gồm cả 'username'
#         user_data = {
#             'username': user.username,
#             # Bổ sung các thông tin khác của người dùng nếu cần
#         }
#         return Response(user_data, status=status.HTTP_200_OK)
#     else:
#         return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
        
#         # Perform authentication logic here (e.g., username and password validation)
        
#         if username and password:
#             user = User.objects.get(username=username)
#             refresh = RefreshToken.for_user(user)
#             access_token = str(refresh.access_token)
#             return Response({'access_token': access_token})
        
#         return Response({'error': 'Invalid credentials'}, status=400)

# class UserInfoView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         serializer = UserSerializer(request.user)
#         return Response(serializer.data)
=======
        return Response(user_data, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
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


class CustomerUserCreate(generics.CreateAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = CustomerUserSerializer

class CustomTokenObtainPairView(APIView):
    def post(self, request):
        serializer = CustomerUserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(
            request,
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        if user:
            refresh = RefreshToken.for_user(user)
            data = {
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token),
                 'access_expires': int(settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].total_seconds()),
                'refresh_expires': int(settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'].total_seconds())
            }
            return Response(data, status=status.HTTP_200_OK)

        return Response({
            'error_message': 'username or password is incorrect!',
            'error_code': 400
        }, status=status.HTTP_400_BAD_REQUEST)
>>>>>>> ce2dde03f829450266422e67b2d8e86c5aa7e31b
