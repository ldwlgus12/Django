from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.

def index(request):
    todos = Todo.objects.all()

    context = {
        'todos' : todos,
    }

    return render(request, 'index.html', context)




def detail(request, todo_pk):
    todos = Todo.objects.get(pk=todo_pk)

    context = {
        'todos' : todos,
    }

    return render(request, 'detail.html', context)





def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todos = form.save()
            return redirect('todos:detail', todos.pk)
    
    else:
        form = TodoForm()
    context = {
        'form' : form,
    }
    return render(request, 'create.html', context)





def update(request, todo_pk):
    todos = Todo.objects.get(pk=todo_pk)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todos)
        if form.is_valid():
            todos = form.save()
            return redirect('todos:detail', todos.pk)

    
    else:
        form = TodoForm(instance=todos)
    context = {
        'todos' : todos,
        'form' : form,
    }
    return render(request, 'update.html', context)





def delete(request, todo_pk):
    todos = Todo.objects.get(pk=todo_pk)
    todos.delete()

    return redirect('todos:index')





# def new(request):
#     return render(request, 'new.html')




# def create(request):
#     title = request.POST.get('title')
#     content = request.POST.get('content')
#     priority = request.POST.get('priority')
#     deadline = request.POST.get('deadline')

#     creates = Todo(title=title, content=content, priority=priority, deadline=deadline)
#     creates.save()

#     return redirect('todos:index')








# def edit(request, todo_pk):
#     edits = Todo.objects.get(pk=todo_pk)

#     context = {
#         'edits' : edits
#     }

#     return render(request, 'edit.html', context)




# def update(request, todo_pk):
#     updates = Todo.objects.get(pk=todo_pk)

#     title = request.POST.get('title')
#     content = request.POST.get('content')
#     priority = request.POST.get('priority')
#     deadline = request.POST.get('deadline')

#     updates.title = title
#     updates.content = content
#     updates.priority = priority
#     updates.deadline = deadline

#     updates.save()

#     return redirect('todos:detail', updates.pk)

