from django.shortcuts import render
from django.db.models import Q
from .models import Thesis

def thesis_search(request):
    query = request.GET.get('q')
    if query:
        results = Thesis.objects.filter(
            Q(title__icontains=query) | 
            Q(author__icontains=query) | 
            Q(department__icontains=query) |
            Q(publish__icontains=query) |
            Q(adviser__icontains=query)
        )
    else:
        results = Thesis.objects.all()

    return render(request, 'thesis_app/thesis_search.html', {'results': results, 'query': query})

def landing_page(request):
    return render (request, 'thesis_site/landing_page.html')
