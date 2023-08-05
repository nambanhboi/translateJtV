from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views



urlpatterns = [
    #path('sentence_list/', views.SentenceViewSet.as_view(), name='sentence_list'),
    path('signup', views.signup, name='signup'),
    path('login', views.login_api, name='login'),
    path('sentence_list', views.SentenceViewSet.as_view({'get': 'list'}), name='sentence_list'),
    path('Report', views.ReportViewSet.as_view({'get': 'list'}), name='Report'),
    path('Contribute', views.ContributeViewSet.as_view({'get': 'list'}), name='Contribute'),

] 

# # #định nghĩa các router
# router.register('sentence_list', views.SentenceViewSet, basename='sentence_list')
# router.register('comment', views.CommentViewSet, basename='comment')
# # router.register('user', views.UserViewSet, basename='user')
# router.register('Report', views.ReportViewSet, basename='Report')
# router.register('Contribute', views.ContributeViewSet, basename='Contribute')
# router.register('login', views.login_api, basename='login')
# router.register('signup', views.signup, basename='signup')



# router = DefaultRouter()
# #định nghĩa các router
# router.register(r'report', views.ReportViewSet, basename='report')

# urlpatterns = router.urls

urlpatterns = [
    path('sentence_list/', views.SentenceViewSet.as_view({'get': 'list'}), name='sentence_list'),
    path('signup', views.signup, name='signup'),
    path('login', views.login_api, name='login'),
    # path('', include(router.urls)),
    path('report', views.report, name='report'),
]