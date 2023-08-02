from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
#định nghĩa các router
router.register('sentence_list', views.SentenceViewSet, basename='sentence_list')
router.register('comment', views.CommentViewSet, basename='comment')
router.register('user', views.UserViewSet, basename='user')
router.register('Report', views.ReportViewSet, basename='Report')
router.register('Contribute', views.ContributeViewSet, basename='Contribute')

# router = DefaultRouter()
# #định nghĩa các router
# # router.register('register', views.CustomerUserCreate.as_view(), basename='register')

urlpatterns = router.urls

# urlpatterns = [
#     #path('sentence_list/', views.SentenceViewSet.as_view(), name='sentence_list'),
#     path('register/', views.CustomerUserCreate.as_view(), name='register'),
#     path('login/', views.CustomTokenObtainPairView.as_view(), name='login'),
# ]