from django.shortcuts import render
from django.http import HttpResponse
from .models import Sentence
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SentenceSeializer
# Create your views here.
class SentenceList(APIView):
    def get(self, request):
        sen = Sentence.objects.all()
        data = SentenceSeializer(sen, many=True).data
        return Response(data)
