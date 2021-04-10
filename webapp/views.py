from django.shortcuts import render

from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employees
from .serialisers import employeesSerializer
import json


# Create your views here.
#    what we have to display when we hit the API.
#    We have to request the API and get json data back
def welcome(request):
    return HttpResponse("<h1>Welcome to My First Django Rest API</h1>")

class employeeList(APIView):
    # get fun to read data
    def get(self, request):
        emp = employees.objects.all()
        serializer = employeesSerializer(emp, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = employeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class employeeDetail(APIView):
        """
        Retrieve, update or delete a snippet instance.
        """

        def get_object (self, pk):
            try:
                return employees.objects.get(pk=pk)
            except employees.DoesNotExist:
                raise Http404

        def get (self, request, pk, format=None):
            emp = self.get_object(pk)
            serializer = employeesSerializer(emp)
            return Response(serializer.data)

        def put (self, request, pk, format=None):
            emp = self.get_object(pk)
            serializer = employeesSerializer(emp, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def delete (self, request, pk, format=None):
            emp = self.get_object(pk)
            emp.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

