from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.

def index(request):
    todos = Todo.objects.all()

    context = {
        'todos' : todos,
    }

    return render(request, 'index.html', context)




def detail(request, todo_pk):
    detail = Todo.objects.get(pk=todo_pk)

    context = {
        'detail' : detail,
    }

    return render(request, 'detail.html', context)




def new(request):
    return render(request, 'new.html')




def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    priority = request.POST.get('priority')
    deadline = request.POST.get('deadline')

    creates = Todo(title=title, content=content, priority=priority, deadline=deadline)
    creates.save()

    return redirect('todos:index')




def delete(request, todo_pk):
    deletes = Todo.objects.get(pk=todo_pk)
    deletes.delete()

    return redirect('todos:index')




def edit(request, todo_pk):
    edits = Todo.objects.get(pk=todo_pk)

    context = {
        'edits' : edits
    }

    return render(request, 'edit.html', context)




def update(request, todo_pk):
    updates = Todo.objects.get(pk=todo_pk)

    title = request.POST.get('title')
    content = request.POST.get('content')
    priority = request.POST.get('priority')
    deadline = request.POST.get('deadline')

    updates.title = title
    updates.content = content
    updates.priority = priority
    updates.deadline = deadline

    updates.save()

    return redirect('todos:detail', updates.pk)

