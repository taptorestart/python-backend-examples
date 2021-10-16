from django.http import JsonResponse
from celery.result import AsyncResult
import json
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from task.tasks import add


class TaskView(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(TaskView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        json_data = json.loads(request.body)
        number1 = json_data["number1"]
        number2 = json_data["number2"]
        task = add.delay(number1, number2)
        return JsonResponse({"task_id": task.id}, status=202)

    def get(self, request, *args, **kwargs):
        task_id = request.GET.get("task_id")
        task_result = AsyncResult(task_id)
        result = {
            "task_id": task_id,
            "task_status": task_result.status,
            "result": task_result.result
        }
        return JsonResponse(result, status=200)