from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer, TodoCompletedSerializer


@api_view(['GET', 'POST'])
def todoList(request):
    if request.method == 'GET':
        tasks = Todo.objects.all().order_by('-id')
        serializer = TodoSerializer(tasks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['DELETE', 'PATCH'])
def todoListUpdate(request, pk):
    if request.method == 'DELETE':
        task = Todo.objects.get(id=pk)
        m = task.delete()
        return Response('deleted')

    elif request.method == 'PATCH':
        task = Todo.objects.get(id=pk)
        serializer = TodoCompletedSerializer(task, data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)