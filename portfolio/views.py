from django.shortcuts import render

from .models import Education, Experience, Project

def experiences(request):
    experiences = Experience.objects.all().order_by('order')
    return render(request, 'experiences.html', {'experiences': experiences})

def index(request):
    return render(request, 'index.html')

def education(request):
    education = Education.objects.all()  
    return render(request, 'education.html', {'education': education})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def skills(request):
    return render(request, 'in_construction.html')
