from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def StudentApi(request,pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu)
            return Response (serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu ,many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    if request.method == 'PUT':
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data updated Completely'})
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'PATH':
        id = pk
        if id is not None:
            stu = Student.objects.get(pk=id)
            serializer = StudentSerializer(stu,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data updated partially'})
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
        
    if request.method == 'DELETE':
            id = pk 
            if id is not None:
                stu = Student.objects.get(pk=id)
                stu.delete()
                return Response({'msg':'Data Deleted!!!'})