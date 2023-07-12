from django.urls import path
from . import views
urlpatterns = [
    path('sentence_list', views.SentenceList.as_view(), name="sentence_list")
]