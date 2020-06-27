from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from django.contrib.auth.decorators import login_required

def home(request):
    projects = Project.objects
    return render(request, 'projects/home.html', {'projects':projects})

def detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/detail.html', {'project':project})

@login_required
def upvote(request, project_id):
    if request.method=='POST':
        project = get_object_or_404(Project, pk=project_id)
        project.votes_total += 1
        project.save()
        return redirect('/projects/' + str(project.id))
