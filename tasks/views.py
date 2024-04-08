from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Task
from .forms import TaskForm

# Create your views here.


def task_create(request):
    if request.method == 'POST':
        # 将用户数据和表单数据进行绑定
        form = TaskForm(request.POST)
        # 验证数据
        if form.is_valid():
            form.save()
            # 跳转到任务列表页
            return redirect(reverse('tasks:task_list'))
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})


# Retrieve task list
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


# Retrieve single task
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks/task_detail.html', {'task': task})


# Update a single task
def task_update(request, pk):
    task_obj = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task_obj)
        if form.is_valid():
            form.save()
            return redirect(reverse('tasks:task_detail'), args=[pk,])
    else:
        form = TaskForm(instance=task_obj)
    return render(request, 'tasks/task_form.html', {'form': form, 'object': task_obj})


# Delete a single task
def task_delete(request, pk):
    task_obj = get_object_or_404(Task, pk=pk)
    task_obj.delete()
    return redirect(reverse('tasks:task_list'))

