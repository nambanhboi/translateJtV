from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import filters, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend

from .models import Sentence
from .serializers import SentenceSeializer
# Create your views here.
# class SentenceList(APIView):
#     def get(self, request):
#         sen = Sentence.objects.all()
#         data = SentenceSeializer(sen, many=True).data
#         return Response(data)

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