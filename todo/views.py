from django.shortcuts import render, redirect

from .models import Task
from .forms import TaskForm


def index(request):

    form = TaskForm()
    tasks = Task.objects.all()

    if request.method == "POST":
        # 这里表示index中的input提交了POST请求
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("todo:index")

    context = {'tasks': tasks, 'TaskForm': form}

    return render(request, 'tasks.html', context=context)


def updateTask(request):
    pass