from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/index.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('blog/post/<int:post_id>/', views.blog_post, name='blog_post'),
    path('blog/create/', views.create_post, name='create_post'),
    path('blog/create_comment/<int:post_id>/', views.create_comment, name='create_comment'),]