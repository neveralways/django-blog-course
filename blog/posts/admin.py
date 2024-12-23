from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published_date')
    list_display_links = ('id', 'title')
    list_filter = ('published_date',)
    search_fields = ('title', 'content')