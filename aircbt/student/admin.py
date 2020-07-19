from django.contrib import admin

from .models import StudentExam

class StudentExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_name', 'score' )
    list_display_links = ('id', 'student_name')
    list_per_page = 50
    

admin.site.register(StudentExam, StudentExamAdmin)


