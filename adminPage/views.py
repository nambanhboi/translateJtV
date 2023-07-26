from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .serializers import SentenceSerializer, ParagraphSerializer
from DictionaryJtVApp.models import Sentence, Paragraph

# Create your views here.

class SentenceViewSet(viewsets.ModelViewSet):
    serializer_class = SentenceSerializer
    def get_queryset(self):
        paragraph_id = self.kwargs.get('paragraph_id')
        if paragraph_id:
            return Sentence.objects.filter(paragraph__id=paragraph_id)
        return Sentence.objects.all()
class ParagraphViewSet(viewsets.ModelViewSet):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer


   