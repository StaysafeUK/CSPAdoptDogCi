from . import views
from django.urls import path

#URL pattern for default site 
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
]