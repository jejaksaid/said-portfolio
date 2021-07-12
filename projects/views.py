from django.shortcuts import render

from django.http import HttpResponse
from .models import Project

projectList = [
    {
        'id':'2',
        'title': "Ecommerce Website",
        'description': "Fully functional ecommerce website"
    },
    {
        'id': '3',
        'title': "Portfolio website",
        'description': "This has a project where I built out my portfolio website"
    },
    {
        'id': '4',
        'title': 'Social Network',
        'description': "Awesome open source project I am still working"
    },
]

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    print('projectObj:', projectObj)
    return render(request, 'projects/single-project.html', {'project': projectObj, 'tags': tags})