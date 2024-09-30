from .models import Comment, Post
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Comments on post_detail.html with CRUD functionality
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
# Model for Email Authentication and authorisation currently not used in this project
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
