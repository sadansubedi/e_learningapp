from rest_framework import serializers
from .models import Course, Chapter, ChapterVideo, ChapterPDF

class CourseSerializer(serializers.ModelSerializer):
   class Meta:
       model = Course
       fields = '__all__'

class ChapterSerializer(serializers.ModelSerializer):
   class Meta:
       model = Chapter
       fields = '__all__'

class ChapterVideoSerializer(serializers.ModelSerializer):
   class Meta:
       model = ChapterVideo
       fields = '__all__'

class ChapterPDFSerializer(serializers.ModelSerializer):
   class Meta:
       model = ChapterPDF
       fields = '__all__'
