from django.db import models

# Create your models here.


class StudentExam(models.Model):
    student_exam_name= models.CharField(max_length=50)
    student_code= models.CharField(max_length=20)
    student_name= models.CharField(max_length=50)
    student_question_code = models.TextField(blank=True)
    student_options_answer = models.TextField(blank=True)
    score= models.IntegerField(default=0)

    def __str__(self):
        return self.student_name


