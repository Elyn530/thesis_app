from django.contrib import admin
from .models import thesis

class ThesisAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'department', 'publish', 'adviser')  
    search_fields = ['title', 'author', 'department', 'publish', 'adviser']  # Specify the fields to be searchable

admin.site.register(thesis, ThesisAdmin)
