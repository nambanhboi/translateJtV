from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
#định nghĩa các router
router.register('sentence_list', views.SentenceViewSet, basename='sentence_list')



urlpatterns = router.urls