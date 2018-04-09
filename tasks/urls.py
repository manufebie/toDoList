from django.urls import path


from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='list'),
    path('add', views.add_task, name='create'),
    path('complete/<task_id>', views.task_completed, name='complete'),
    path('delete-completed-tasks', views.delete_completed_task, name='delete-completed')
]