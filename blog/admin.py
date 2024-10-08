from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Sanctuary

# Register your models here.
admin.site.register(Comment)
admin.site.register(Sanctuary)


@admin.register(Post)
# add to Summernote in Admin pages 
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
