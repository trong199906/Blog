from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('blog-post', views.blog_post, name='blog-post'),
    path('blog-list', views.blog_list, name='blog-list')
]