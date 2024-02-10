from django.shortcuts import render
from .models import Thesis

def thesis_list(request):
    theses = Thesis.objects.all()
    return render(request, 'thesis_app/thesis_list.html', {'theses': theses})
