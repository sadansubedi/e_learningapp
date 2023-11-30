from django.contrib import admin
# from .models import Subject, Course, Module
'''
# admin.site.index_template = 'memcache_status/admin_index.html';

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {"slug": ('title',)}


class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]
'''
from . models import Course, Chapter, ChapterPDF,ChapterVideo
@admin.register(Course)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ['id','course_name','description']

@admin.register(Chapter)
class ChapterModelAdmin(admin.ModelAdmin):
    list_display = ['id','chapter_name','content','course']

@admin.register(ChapterVideo)
class ChapterVideoModelAdmin(admin.ModelAdmin):
    list_display = ['id','chapter','video_file']


@admin.register(ChapterPDF)
class ChapterPDFModelAdmin(admin.ModelAdmin):
    list_display = ['id','chapter','pdf_file']
