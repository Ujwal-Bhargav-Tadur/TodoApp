from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home_page(request):
    return render(request, 'TodoApp/index.html')


def create_task(request):
    return render(request, '')
    # return HttpResponse("Creates a task to Todo list")


def update_task(request):
    return HttpResponse("Update task in Todo list")


def delete_task(request):
    return HttpResponse("Delete task in Todo list")


def get_task(request):
    return HttpResponse("Get task from todo list")
