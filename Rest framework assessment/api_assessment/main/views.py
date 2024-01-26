from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Example
from .serializers import ExampleSerializer

class ExampleListView(APIView):
    def get(self, request, pk=None):
        if pk is not None:   
            instance = get_object_or_404(Example, pk=pk)
            serializer = ExampleSerializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
            
        instances = Example.objects.all()
        serializer = ExampleSerializer(instances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ExampleSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        instance = get_object_or_404(Example, pk=pk)
        serializer = ExampleSerializer(instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        instance = get_object_or_404(Example, pk=pk)
        serializer = ExampleSerializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        instance = get_object_or_404(Example, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
