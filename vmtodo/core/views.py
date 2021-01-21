import json
from django.forms import model_to_dict
from django.http import JsonResponse
from vmtodo.core.models import Tasks, TaskForm


def get_post_tasks(request):
    if request.method == 'GET':
        obj = list(Tasks.objects.all().values())
        return JsonResponse(obj, safe=False)  # safe=False porque obj não esta 100% JSON
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse(data=form.data, status=201)
        else:
            return JsonResponse(data={'message': 'Invalid format'}, status=400)


def get_delete_put_task_detail(request, pk):
    if request.method == 'GET':
        try:
            obj = model_to_dict(Tasks.objects.get(pk=pk))
            return JsonResponse(data=obj, safe=False)
        except Tasks.DoesNotExist:
            return JsonResponse(data={'message': 'Tasks not found'}, status=404)
    elif request.method == 'DELETE':
        obj = Tasks.objects.filter(pk=pk).delete()
        if obj[0]:
            data = {'message': 'Object was delete with success!'}
        else:
            data = {'message': 'Object does not found!'}
        return JsonResponse(data=data, status=204)
    elif request.method == 'PUT':
        task = Tasks.objects.get(pk=pk)
        put_data = json.loads(request.body)
        put_data['id'] = pk
        form = TaskForm(instance=task, data=put_data)
        if form.is_valid():
            form.save()
            return JsonResponse(data=form.data, status=204)
        else:
            return JsonResponse(data={'message': 'Invalid format'}, status=400)
