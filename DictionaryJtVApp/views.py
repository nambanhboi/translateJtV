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
from rest_framework.authtoken.serializers import AuthTokenSerializer

import json
from django.core import serializers
# from django.views.decorators.http import require_GET
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
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
    permission_classes = [IsAuthenticated]


    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     print(request.data)
    #     print(request.user)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(user=request.user)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response({'message': 'Report created successfully'}, status=status.HTTP_201_CREATED, headers=headers)

class ContributeViewSet(viewsets.ModelViewSet):
    queryset = Contribute.objects.all()
    serializer_class = ContributetSeializer

@api_view(['POSt'])
@csrf_exempt
def report(request):
    serializer = reportSeializer(data=request.data)
    print(request.user)
    print(request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)  # Tự động gán người dùng hiện tại
        return Response({'message': 'Report created successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        if User.objects.filter(username=username).exists():
            # Tên người dùng đã tồn tại, trả về thông báo lỗi
            return Response({'message': 'Tên người dùng đã tồn tại'}, status=status.HTTP_409_CONFLICT)

        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()

        # Tạo token cho người dùng vừa đăng ký
        refresh = RefreshToken.for_user(user)
        token = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        # Trả về thông tin người dùng và token
        user_data = {
            'user': {
                'id': user.id,
                'username': user.username,
            },
            'token': token,
        }
        return Response(user_data, status=status.HTTP_201_CREATED)  # HTTP 201 CREATED cho người dùng mới
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # HTTP 400 BAD REQUEST nếu thông tin đăng ký không hợp lệ
    
@csrf_exempt
@api_view(['POST'])
def login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        # Xác thực thành công, tạo token cho người dùng
        refresh = RefreshToken.for_user(user)
        token = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        # Trả về thông tin người dùng và token
        user_data = {
            'user': {
                'id': user.id,
                'username': user.username,
            },
            'token': token,
        }
        return Response(user_data, status=status.HTTP_200_OK)
    else:
        # Xác thực thất bại, trả về thông báo lỗi
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
