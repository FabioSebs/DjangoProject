from django.urls import path
#make sure to import your view
from . import views
from .views import PostListView

urlpatterns = [
    path('post', PostListView.as_view(), name='website-posts'),
    path('', views.home , name='website-home'),
    path('quotes' , views.tweets, name='website-quotes'),
    
]