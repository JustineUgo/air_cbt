from django.contrib import admin

from .models import Examiner, Exam, Question, Option, Response, Student

class ExaminerAdmin(admin.ModelAdmin):
    list_display = ('id', 'examiner_name', 'examiner_code')
    list_display_links = ('id', 'examiner_name')
    list_per_page = 50

class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'exam_code', 'exam_name', 'number_of_questions','exam_examiner_name')
    list_display_links = ('id', 'exam_code', 'exam_name')
    list_editable = ('exam_examiner_name', )
    list_per_page = 50

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_type', 'question_exam_name')
    list_display_links = ('id', 'question_type', 'question_exam_name')
    list_per_page = 50

class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'option_id', 'option_text', 'status', 'option_exam_name',)
    list_display_links = ('id', 'option_id')
    list_editable = ('option_text','status', )
    list_per_page = 50

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'response_id', 'status', 'score', 'response_candidate_code', 'response_question_code')
    list_display_links = ('id', 'response_id')
    list_editable = ('status', 'score')
    list_per_page = 50

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_name', 'student_code', 'student_email')
    list_display_links = ('id', 'student_code', 'student_name')
    list_per_page = 50
    


admin.site.register(Examiner, ExaminerAdmin)
admin.site.register(Exam, ExamAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Response, ResponseAdmin)


