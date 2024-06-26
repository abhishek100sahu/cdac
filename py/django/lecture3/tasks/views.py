from django import forms
from django.shortcuts import render

tasks = ['buy groceries', 'dump garbage', 'call manager']

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority",  min_value=0, max_value=10)

# Create your views here.
def index(request):
    return render(request, 'tasks/index.html' , {
        "tasks": tasks
    })
def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            print (form.cleaned_data)
            tasks.append(task)
        else:
            return render(request, 'tasks/add.html', {
                "form": form
            })
    return render(request, 'tasks/add.html', {
        "form": NewTaskForm()
    })