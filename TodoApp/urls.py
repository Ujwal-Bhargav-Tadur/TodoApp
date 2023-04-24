from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home_page, name='home'),
    path('create', views.create_task, name="create_task"),
    path('get', views.get_task, name="get_task"),
    path('update', views.update_task, name="update_task"),
    path('delete', views.delete_task, name="delete_task")
]
