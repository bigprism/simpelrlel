from django.urls import path

from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:pk>/update/', views.task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),

    path('api/tasks/', views.task_list_api, name='task_list_api'),
    path('api/tasks/<int:pk>/', views.task_detail_api, name='task_detail_api'),
    path('api/tasks/create/', views.task_create_api, name='task_create_api'),
    path('api/tasks/<int:pk>/update/', views.task_update_api, name='task_update_api'),
    path('api/tasks/<int:pk>/delete/', views.task_delete_api, name='task_delete_api'),
]