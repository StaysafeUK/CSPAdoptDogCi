from .models import CollaborateRequest, LeaveComment
from django import forms


class CollaborateForm(forms.ModelForm):
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')

class LeaveCommentForm(forms.ModelForm):
    class Meta:
        model = LeaveComment
        fields = ('name', 'email', 'comment')

