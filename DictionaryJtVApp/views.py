from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import filters, viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django_filters.rest_framework import DjangoFilterBackend
import json
from django.core import serializers
from .models import Sentence, Report, Contribute
from .serializers import SentenceSeializer, reportSeializer,ContributetSeializer
# from django.views.decorators.http import require_GET


from .models import Sentence
from .serializers import SentenceSeializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
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

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = reportSeializer

class ContributeViewSet(viewsets.ModelViewSet):
    queryset = Contribute.objects.all()
    serializer_class = ContributetSeializer
@api_view(['GET'])
@authentication_classes([])
@permission_classes([IsAuthenticated])
def get_username(request):
    user = request.user
    return Response({'username':user.username})

@api_view(['POST'])
def login(request):
    # Xử lý đăng nhập và kiểm tra thông tin người dùng
    # Sau khi xác thực thành công, lấy thông tin người dùng
    username = request.data.get('username')
    password = request.data.get('password')

    # Xác thực người dùng bằng cách sử dụng authenticate từ Django
    user = authenticate(username=username, password=password)
    if user is not None:
        # Tạo một đối tượng JSON chứa thông tin người dùng, bao gồm cả 'username'
        user_data = {
            'username': user.username,
            # Bổ sung các thông tin khác của người dùng nếu cần
        }
        return Response(user_data, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
