from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

class TodoListCreateAPIView(APIView):

    def get(self,request):
        todos= Todo.objects.all()
        serializer = TodoSerializer(todos,many= True)
        return Response(serializer.data)
    

    def post(self,request):
        serializer= TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= 201)
        return Response(serializer.errors,status=400)


