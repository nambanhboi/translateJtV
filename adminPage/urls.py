from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
#lấy ra các sentence trong cùng cùng 1 paragraph
router.register(r'paragraph_list/(?P<paragraph_id>\d+)/sentence_list', views.SentenceViewSet, basename='sentence_list')
router.register('paragraph_list', views.ParagraphViewSet, basename='paragraph_list')

urlpatterns = router.urls