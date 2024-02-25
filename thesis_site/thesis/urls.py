
from django.urls import path
from . import views

app_name = "Thesis"

urlpatterns = [
    path('', views.thesis_list, name="thesis_list"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.thesis_list,
         name='thesis_detail'),

    path('<int:post_id>/comment/',
         views.post_comment, name='post_comment'),
]