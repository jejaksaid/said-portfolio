from django.shortcuts import render

from django.http import HttpResponse

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
    page = 'projects'
    context = {'page': page, 'projects': projectList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for i in projectList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})