from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_me, name='about'),
    path('about/', views.about_me, name='about_me')
]