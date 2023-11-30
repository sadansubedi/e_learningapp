from django.shortcuts import render
from . models import Course, Chapter, ChapterVideo, ChapterPDF
from .serializers import CourseSerializer,ChapterSerializer,ChapterPDFSerializer,ChapterVideoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

class CourseViewSet(viewsets.ModelViewSet):
   queryset = Course.objects.all()
   serializer_class = CourseSerializer

class ChapterViewSet(viewsets.ModelViewSet):
   queryset = Chapter.objects.all()
   serializer_class = ChapterSerializer

class ChapterVideoViewSet(viewsets.ModelViewSet):
   queryset = ChapterVideo.objects.all()
   serializer_class = ChapterVideoSerializer

class ChapterPDFViewSet(viewsets.ModelViewSet):
   queryset = ChapterPDF.objects.all()
   serializer_class = ChapterPDFSerializer


'''
@api_view(['GET'])
# @api_view(['GET','POST','PUT','PATCH','DELETE'])
def course_api(request,pk=None):#here pk value comes from url.py
    if request.method == 'GET':
        id=pk                       
        if id is not None:
            course = Course.objects.get(id=id)
            serializer = CourseSerializer(course)
            return Response(serializer.data) #it return with json format
        else:
            course = Course.objects.all()# if requested for all data from DB
            serializer = CourseSerializer(course,many=True)
            return Response(serializer.data) 

'''
# coz we think student dont allow post put patch so below code is commented ok
'''
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data deleted'})

'''