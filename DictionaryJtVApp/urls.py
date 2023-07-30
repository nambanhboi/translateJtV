from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

<<<<<<< HEAD
router = DefaultRouter()
#định nghĩa các router
router.register('sentence_list', views.SentenceViewSet, basename='sentence_list')
router.register('comment', views.CommentViewSet, basename='comment')
router.register('user', views.UserViewSet, basename='user')


=======
# router = DefaultRouter()
# #định nghĩa các router
# # router.register('register', views.CustomerUserCreate.as_view(), basename='register')
>>>>>>> ce2dde03f829450266422e67b2d8e86c5aa7e31b



# urlpatterns = router.urls

urlpatterns = [
    #path('sentence_list/', views.SentenceViewSet.as_view(), name='sentence_list'),
    path('register/', views.CustomerUserCreate.as_view(), name='register'),
    path('login/', views.CustomTokenObtainPairView.as_view(), name='login'),
]