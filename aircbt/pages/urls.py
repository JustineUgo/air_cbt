from django.urls import path
from . import views

urlpatterns = [
    path('examination/<str:course>', views.exam, name="exam"),
    path('admin_login', views.admin_login, name="admin_login"),
    path('admin_home', views.admin_home, name="admin_home"),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('enroll', views.enroll, name='enroll'),
    path('enrolled', views.enrolled, name='enrolled'),
    path('dashboard', views.display_exams, name='dashboard'),
    path('dashboard/toggle/<str:course>', views.toggle, name='toggle'),
    path('exam', views.create_exam, name='create_exam'),
    path('questions/<str:course>', views.display_questions, name='display_questions'),
    path('create_question/<str:course>', views.create_question, name='create_question'),
    path('submitted', views.submitted, name='submitted'),
    path('submitted/responses', views.exam_responses, name='exam_responses'),
    path('submitted/response', views.student_response, name='student_response'),
]


