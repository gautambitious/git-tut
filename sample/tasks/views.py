from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

from .models import CustomUser, Task

@method_decorator(csrf_exempt, name='dispatch')
class SaveTaskView(View):

    def get(self, request):
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        user = CustomUser.objects.get(pk=data.get('user_id'))
        try:
            if 'username' in data:
                user.username = data.get('username')
            if 'password' in data:
                user.password = data.get('password')
            user.save()
            return JsonResponse({'status': 'ok'}, status=201)
        except Exception as e:
            return JsonResponse({'status': 'error', 'error': str(e)}, status=400)
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        tasks = Task()
        if 'user_id' in data:
            try:
                user = CustomUser.objects.filter(pk=data['user_id']).first()
                tasks.user = user
            except Exception as e:
                print(e)
                return JsonResponse({'status': 'error'})
        tasks.task_name = data.get('name', 'Default Name')
        tasks.task_description = data.get('description', 'Default Description')
        try:
            tasks.save()
            print("Task Saved Successfully")
        except Exception as e:
            print("Error: ", e)
        return JsonResponse({'status': 'success'})
    
@method_decorator(csrf_exempt, name='dispatch')
class GetTaskView(View):

    def get(self, request, user_id):
        user = CustomUser.objects.get(pk=user_id)
        tasks = Task.objects.filter(user=user)
        response = {}
        response['tasks'] = []
        for task in tasks:
            task_json = {}
            task_json['id'] = task.pk
            task_json['name'] = task.task_name
            task_json['description'] = task.task_description
            task_json['is_completed'] = task.task_completed
            response['tasks'].append(task_json)
        return JsonResponse(response, status=200)
    
    def post(self, request, user_id):
        data = json.loads(request.body.decode('utf-8'))
        user = CustomUser.objects.get(pk=user_id)
        try:
            user.delete()
            print("User Deleted")
        except Exception as e:
            print("Error: ", e)
        return JsonResponse({'status': 'success'})
