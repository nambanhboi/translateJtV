from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('sentence_list', views.SentenceViewSet, basename='sentence_list')
router.register('paragraph_list', views.ParagraphViewSet, basename='paragraph_list')

urlpatterns = router.urls