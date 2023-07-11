from django.shortcuts import render
from django.http import HttpResponse
from .models import Sentence

# Create your views here.
def test(request):
    sen = Sentence.objects.all()
    return HttpResponse(sen[1].id)