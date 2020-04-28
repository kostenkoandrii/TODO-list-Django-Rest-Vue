from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer, TodoCompletedSerializer

from .models import Todo


# Create your views here.
@api_view(['GET'])
def todoList(request):
    tasks = Todo.objects.all().order_by('-id')
    serializer = TodoSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def todoCreate(request):
    serializer = TodoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def todoDelete(request, pk):
    task = Todo.objects.get(id=pk)
    m = task.delete()

    return Response('deleted')


@api_view(['POST'])
def todoComletedUpdate(request, pk):
    task = Todo.objects.get(id=pk)
    serializer = TodoCompletedSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)