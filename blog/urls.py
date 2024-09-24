from . import views
from django.urls import path

#URL pattern for default site 
urlpatterns = [

    path('signup/', views.signup, name='signup'),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate_account, name='activate'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('search_sanctuaries', views.search_sanctuaries, name='search-sanctuaries'),
    path('dog/<slug:slug>/', views.dog_detail, name='dog_detail'),
     path('', views.PostList.as_view(), name='home')
]