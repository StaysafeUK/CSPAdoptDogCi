from . import views
from django.urls import path

urlpatterns = [
   
    path('about/', views.about_me, name='about_me'),
    path('edit_leavecomment/<int:leavecomment_id>/', views.leavecomment_edit, name='edit_leavecomment'), 
    path('', views.about_me, name='about'), # URL for editing 
   # path('delete_leavecomment/<int:leavecomment_id>/', leavecomment_delete, name='delete_leavecomment'),  # URL for deleting 
]