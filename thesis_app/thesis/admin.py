from django.contrib import admin
from .models import Thesislist

class ThesisAdmin(admin.ModelAdmin):
    list_display = ('Title','Abstract', 'Approval', 'Author', 'department', 'Adviser', 'Publish',  )  
    

admin.site.register(Thesislist, ThesisAdmin)
