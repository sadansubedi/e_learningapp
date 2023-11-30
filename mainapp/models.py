# from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes.fields import GenericForeignKey
# #  from .fields import OrderField
# from django.template.loader import render_to_string
# """
# for example C- programing =course  
#                 pointer =  subject
# we have a Subject the contain courses and every course contain modules
#     - subject has:
#         1. title(pointer)
#         2. slug
#             * order by title
#     - course has :
#         1. owner(a User)
#         2. subject(a Subject)
#         3. title
#         4. slug
#         5. overview
#         6. created date
#             * order by created (des)
#     - module has :
#         1. course (a course)
#         2. title
#         3. description 
#         4. order
# -----------------------
# the Content model can be of different types so we use a generic relation to point to the Content object 
#     - Content:
#         1. module (belongs to a module)
#         2. content_type (foreign key to the ContentType) --> used for the generic relation
#         3. object_id (th e key for the elated object)
#         4. item (does not exists in the database but build on the other columns)
#         5. order
#     **note: learn more about generic relation in Django**
# -----------------------
# the ItemBase model is an abstract model that is inherited in the content types (text, file, image, video)
#     - ItemBase :
#         1. owner (user)
#         *. title, created, updated
#     * the files are uploaded to 'files', the images to 'images and the videos store the urls
# ----------------------
# """


# class Subject(models.Model):
#     title = models.CharField(max_length=200)
#     slug = models.SlugField(max_length=200, unique=True)

#     class Meta:
#         ordering = ['title']

#     def __str__(self):
#         return self.title


# class Course(models.Model):
#     owner = models.ForeignKey(User, related_name="courses_created", on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject, related_name="courses", on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     overview = models.TextField()
#     slug = models.CharField(max_length=200, unique=True)
#     created = models.DateTimeField(auto_now_add=True)
#     students = models.ManyToManyField(User, related_name="courses_joined", blank=True)

#     class Meta:
#         ordering = ['-created']

#     def __str__(self):
#         return self.title


# class Module(models.Model):
#     course = models.ForeignKey(Course, related_name="modules", on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#     # order = OrderField(blank=True, for_fields=['course'])

#     class Meta:
#         ordering = ['title']

#     def __str__(self):
#         # return f'{self.order}, {self.title}'
#         return self.title


# class Content(models.Model):
#     module = models.ForeignKey(Module, related_name="contents", on_delete=models.CASCADE)
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in': (
#         'text', 'video', 'image', 'file')})
#     object_id = models.PositiveIntegerField()
#     item = GenericForeignKey('content_type', 'object_id')
#     # order = OrderField(blank=True, for_fields=['module'])

#     class Meta:
#         # ordering = ['order']
#          ordering = ['object_id']


# class ItemBase(models.Model):
#     owner = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
#     title = models.CharField(max_length=250)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True

#     def __str__(self):
#         return self.title

#     def render(self):
#         return render_to_string(
#             f'courses/content/{self._meta.model_name}.html', {'item': self}
#         )


# class Text(ItemBase):
#     content = models.TextField()


# class File(ItemBase):
#     file = models.FileField(upload_to='files')


# class Image(ItemBase):
#     image = models.ImageField(upload_to='images')


# class Video(ItemBase):
#     url = models.URLField()


'''
# According to phind.AI 
from django.db import models

class Student(models.Model):
   student_id_no = models.IntegerField(primary_key=True)
   last_name = models.CharField(max_length=255)
   first_name = models.CharField(max_length=255)

class LessonCategory(models.Model):
   category_name = models.CharField(max_length=255)
   description = models.CharField(max_length=255)

class Lesson(models.Model):
   lesson_name = models.CharField(max_length=255)
   content = models.TextField()
   category = models.ForeignKey(LessonCategory, on_delete=models.CASCADE)

class LessonVideo(models.Model):
   lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
   video_file = models.CharField(max_length=255)

class LessonPDF(models.Model):
   lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
   pdf_file = models.CharField(max_length=255)

class Quiz(models.Model):
   question = models.TextField()
   correct_answer = models.CharField(max_length=255)
   answer1 = models.CharField(max_length=255)
   answer2 = models.CharField(max_length=255)
   answer3 = models.CharField(max_length=255)
   answer4 = models.CharField(max_length=255)
   lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

class Result(models.Model):
   student = models.ForeignKey(Student, on_delete=models.CASCADE)
   lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
   score = models.IntegerField()
   total_item = models.IntegerField()
   date_recorded = models.DateField()
 
'''

# According to phind.AI  updated version
from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
   course_name = models.CharField(max_length=255,null=True)
   description = models.CharField(max_length=255,null=True)

   def __str__(self):
        return str(self.course_name)

class Chapter(models.Model):
   chapter_name = models.CharField(max_length=255)
   content = models.TextField()
   course = models.ForeignKey(Course, on_delete=models.CASCADE)

   def __str__(self):
        return str(self.chapter_name)

class ChapterVideo(models.Model):
   chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
   # video_file = models.CharField(max_length=255)
   # video_file = models.FileField(upload_to='videos/')
   video_file = models.URLField()

   def __str__(self):
        return str(self.id)

class ChapterPDF(models.Model):
   chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
   # pdf_file = models.CharField(max_length=255)
   pdf_file = models.FileField(upload_to='pdfs/')

   def __str__(self):
        return str(self.id)

# class Quiz(models.Model):
#    question = models.TextField()
#    correct_answer = models.CharField(max_length=255)
#    answer1 = models.CharField(max_length=255)
#    answer2 = models.CharField(max_length=255)
#    answer3 = models.CharField(max_length=255)
#    answer4 = models.CharField(max_length=255)
#    lesson = models.ForeignKey(Chapter, on_delete=models.CASCADE)

# class Result(models.Model):
#    student = models.ForeignKey(User, on_delete=models.CASCADE)
#    lesson = models.ForeignKey(Chapter, on_delete=models.CASCADE)
#    score = models.IntegerField()
#    total_item = models.IntegerField()
#    date_recorded = models.DateField()
 