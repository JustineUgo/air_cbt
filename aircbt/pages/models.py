from django.db import models
from datetime import datetime

class Examiner(models.Model):
    examiner_code = models.CharField(max_length=200)
    examiner_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.examiner_name

class Exam(models.Model):
    exam_examiner_name = models.CharField(max_length=200)#ForeignKey(Examiner, on_delete=models.DO_NOTHING)
    exam_code = models.CharField(max_length=200)
    exam_name = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)
    number_of_questions = models.IntegerField(default=0)

    def __str__(self):
        return self.exam_name

class Student(models.Model):
    student_code = models.CharField(max_length=20)
    student_name = models.CharField(max_length=50)
    student_rank = models.CharField(max_length=20)
    student_level = models.CharField(max_length=20)#, choices=DEPARTMENT_CHOICES, default="CS"
    student_email= models.CharField(max_length=100)

    def __str__(self):
        return self.candidate_code

class Question(models.Model):
    question_exam_name = models.CharField(max_length=200)#ForeignKey(Exam, on_delete=models.DO_NOTHING)
    question_text = models.TextField(blank=True)
    question_type= models.CharField(max_length=20)

    def __str__(self):
        return self.question_exam_name


class Option(models.Model):
    option_exam_name = models.CharField(max_length=50)
    option_question_text = models.TextField(blank=True)#ForeignKey(Question, on_delete=models.DO_NOTHING)
    #QUESTION_CHOICES = (("A","a"),("B","b"),("C","c"),("D","d"))
    option_id= models.CharField(max_length=2, )
    option_text= models.CharField(max_length=50)
    status= models.IntegerField(default=0)


    def __str__(self):
        return self.option_id

class Response(models.Model):
    response_question_code = models.CharField(max_length=200)#ForeignKey(Question, on_delete=models.DO_NOTHING)
    response_id = models.CharField(max_length=20)
    response_text= models.TextField(blank=True)
    status= models.IntegerField(default=0)
    response_candidate_code= models.CharField(max_length=20)#ForeignKey(Candidate, on_delete=models.DO_NOTHING)
    score= models.IntegerField(default=0)

    def __str__(self):
        return self.response_text





