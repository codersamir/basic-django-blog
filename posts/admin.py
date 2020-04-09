from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


class PostAdmin(SummernoteModelAdmin):
    list_display = ('id', 'title', 'date_added')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('date_added',)
    list_editable = ('date_added',)
    summernote_fields = ('content',)


admin.site.register(Post, PostAdmin)
