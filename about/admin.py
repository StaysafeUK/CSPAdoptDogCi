from django.contrib import admin
from .models import About, CollaborateRequest, LeaveComment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)

# LEave Comment admin fields
@admin.register(LeaveComment)
class LeaveComment(admin.ModelAdmin):

    list_display = ('name', 'email', 'comment', 'approved', 'created_on')