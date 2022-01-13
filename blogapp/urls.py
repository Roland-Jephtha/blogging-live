from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('register', views.register, name = 'register'),
    path('login', views.login, name = 'login' ),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
    path("<category>/", views.blog_category, name="blog_category"),
]