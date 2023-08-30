from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# # #định nghĩa các router
router.register('sentence_list', views.SentenceViewSet, basename='sentence_list')
router.register('comment', views.CommentViewSet, basename='comment')

urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('signup', views.signup, name='signup'),
    path('login', views.login_api, name='login'),
    path('report', views.report, name='report'),
    path('comment', views.comment, name='comment'),
    path('contribute',views.contribute, name='contribute'),
    path('ngucanh/<int:sentenceId>/',views.ngucanh, name='ngucanh'),

]