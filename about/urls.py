from . import views
from django.urls import path

urlpatterns = [
   
    path('', views.about_me, name='about_me'),
    path('edit_leavecomment/<int:leavecomment_id>/', views.leavecomment_edit, name='edit_leavecomment'),
    path('delete_leavecomment/<int:leavecomment_id>/', views.leavecomment_delete, name='delete_leavecomment'),  # URL for deleting 
    path('', views.about_me, name='about'), # URL for about page
]
    