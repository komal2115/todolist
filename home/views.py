from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.
def home(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['description']
    
        ins = Task(taskTitle = title, taskDesc = desc)
        ins.save()
        
    return render(request,'index.html')


def task(request):
    task = Task.objects.all()
    context = {
        'task':task
    }
    return render(request,'task.html', context)