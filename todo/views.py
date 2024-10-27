from django.shortcuts import render, redirect
from todo.models import Task
from todo.forms import TaskForm


def main_page(request):
    if request.method == 'GET':
        return render(request, 'base.html')

def list_view(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        return render(request, 'list_view.html', context={'task':tasks})

def detail_view(request, post_id):
    if request.method == 'GET':
        tasks = Task.objects.get(id=post_id)
        return render(request, 'detail_view.html', context={'post':tasks})

def create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'posts/post_create.html', context={'form':form})
        form.save()
        return redirect('/posts/')