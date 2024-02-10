from django.urls import path
from .views import thesis_list
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('thesis/', thesis_list, name='thesis_list'),
    path('admin/', admin.site.urls),
    path('', include('thesis_app.urls')),
]
