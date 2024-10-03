from .models import CollaborateRequest, LeaveComment
from django import forms


# Collaborate Form on About Page
class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')


# LeaveComment Form on About Page
class LeaveCommentForm(forms.ModelForm):
    class Meta:
        model = LeaveComment
        fields = ('name', 'email', 'comment')

