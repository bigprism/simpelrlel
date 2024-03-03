from django.urls import path

from . import views

urlpatterns = [
    path('tasks/', views.task_list_api, name='task_list_api'),
    path('tasks/<int:pk>/', views.task_detail_api, name='task_detail_api'),
    path('tasks/create/', views.task_create_api, name='task_create_api'),
    path('tasks/<int:pk>/update/', views.task_update_api, name='task_update_api'),
    path('tasks/<int:pk>/delete/', views.task_delete_api, name='task_delete_api'),
]