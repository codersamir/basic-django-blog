from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_added')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('date_added',)
    list_editable = ('date_added',)


admin.site.register(Post, PostAdmin)
