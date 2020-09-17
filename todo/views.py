from django.shortcuts import get_object_or_404, render, redirect
from .forms import TodoForm
from .models import Todo


def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todo/index.html', context)


def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)

    context = {
        "todo": todo
    }
    return render(request, "todo/todo_detail.html", context)


def todo_create(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')

    context = {
        "form": form,
    }

    return render(request, 'todo/todo_create.html', context)


def todo_update(request, id):
    todo = get_object_or_404(Todo, id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = { "form": form }
    return render(request, 'todo/update_todo.html', context)


def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')
