from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib import auth

from .models import StudentExam
from pages.models import Student, Exam

def home(request):
    
    exams = Exam.objects.all()
    
    
    if request.method == "POST":
        student_code= request.POST['student_code']
        student_name= request.POST['student_name']
        student_email= request.POST['student_email']
        exam_name= request.POST['exam_name']
        
        student = Student.objects.filter(student_email=student_email)
        
        if(len(student)==0):
            print('Not Enrolled')
            
        else:
            
        
        #exam_to_write = Exam.objects.filter(exam_name=exam_name)
        
        #context={
        #    "student":student,
        #    "exam_to_write":exam_to_write
        #}
        
            return render(request, 'student/gateway.html', {"course":exam_name})
        
    return render(request, 'student/student_login.html', {"exams":exams})
    
    
    

def exam(request):
    
    exams=Exam.objects.filter(exam_name='')
        
    if request.method == "POST":
        question_number=''
        answer=''
        has_finished=''
        
        if has_finished:
            return redirect()
        
        return
            
    return


