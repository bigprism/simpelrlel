from django.http import JsonResponse

from .models import Task



def task_list_api(request):
    tasks = Task.objects.all()
    data = []
    for task in tasks:
        data.append({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'priority': task.priority,
            'status': task.status,
        })
    return JsonResponse(data, safe=False)



def task_detail_api(request, pk):
    task = Task.objects.get(pk=pk)
    data = {
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'priority': task.priority,
        'status': task.status,
    }
    return JsonResponse(data)



def task_create_api(request):
    if request.method == 'POST':
        data = request.POST.dict()
        task = Task.objects.create(**data)
        return JsonResponse({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'priority': task.priority,
            'status': task.status,
        })
    return JsonResponse({'error': 'Invalid request method'})



def task_update_api(request, pk):
    if request.method == 'PUT':
        data = request.PUT.dict()
        task = Task.objects.get(pk=pk)
        for key, value in data.items():
            setattr(task, key, value)
        task.save()
        return JsonResponse({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'priority': task.priority,
            'status': task.status,
        })
    return JsonResponse({'error': 'Invalid request method'})



def task_delete_api(request, pk):
    if request.method == 'DELETE':
        task = Task.objects.get(pk=pk)
        task.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request method'})