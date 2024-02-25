from django.contrib import admin
from .models import ThesisList, Comment

@admin.register(ThesisList)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_field = ['title', 'author', 'department']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=['name', 'email', 'created', 'active', 'body']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']