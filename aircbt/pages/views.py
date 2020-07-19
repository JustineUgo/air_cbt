from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib import auth

from .models import Question, Option, Examiner, Exam, Student
from student.models import StudentExam
#storing questons and answers in time
question_field = []
answer_field=[]

#make a class based view
#show exam | accept answer | score and save
def exam(request, course):
    global question_field
    global answer_field
    
    questions = Question.objects.filter(question_exam_name=course)
    options = Option.objects.filter(option_exam_name=course)
    
    paginator = Paginator(questions, 1)
    page = request.GET.get('page')
    paged_questions = paginator.get_page(page)
    
    context = {
        
        'questions':paged_questions,
        'options':options,
        'course':course
    }
    

    
    if request.method == "POST":
        
        question_type = request.POST.get('question_type')
        question_code= request.POST.get('question_code')
        finish = request.POST.get('finish')
        exam_name = request.POST.get('exam_name')
        
        if  question_type == "essay":
            essay_answer = request.POST.get('essay_text', False)
            
            if essay_answer != '' or essay_answer != False:
                answer_field.append(str(essay_answer))
                question_field.append(str(question_code))
            
        else:
            option_answer = request.POST.get('options', False)
            
            if option_answer != False:
                answer_field.append(str(option_answer))
                question_field.append(str(question_code))
                
        
        if finish == "finish":
            print("DOne HEre")
            student_exam = StudentExam(student_exam_name=course, student_code="AF/01", student_name="Ogaraku", student_question_code=str(question_field), student_options_answer=str(answer_field), score=int(0))
            student_exam.save()
            
            answer_field=[]
            question_field=[]
            
        print(answer_field, question_field)
        print(finish)
    
    
    return render(request, 'pages/exam.html', context)



#add lecturer and course
def admin_login(request):
    
    #Save Examiner and Exam
    if request.method == "POST":
        examiner_name = request.POST['name']
        examiner_code = request.POST['examiner_code']
        
        exam_name = request.POST['exam_name']
        exam_code = request.POST['exam_code']
        
        
        try:
            exam = Exam(exam_examiner_name=examiner_name, exam_name=exam_name, exam_code=exam_code)
            examiner = Examiner(name=examiner_name, examiner_code=examiner_code)
            exam.save()
            examiner.save()
            
            print('Successfully Submitted. Thank You')
        except:
            
            print('Something went wrong. Please try again.')
        
        return redirect('admin_home')
    
    else:
        return render(request, 'pages/admin_login.html')


#add question for exam
def admin_home(request):
    
    exams = Exam.objects.all()
        
    context = {
        "exams":exams
    }
    
    #Save Question and Options to obj questions
    if request.method == "POST":
        question_exam_name = request.POST['question_exam_name']
        question_code = request.POST['question_code']
        question_text = request.POST['question_text']
        date_created = request.POST['date_created']
        question_type = request.POST['question_type']
        
        if question_type == "Objective":
        
            option_question_code = request.POST['question_code']
            option_text_one = request.POST['option1']
            option_text_two = request.POST['option2']
            option_text_three = request.POST['option3']
            option_text_four = request.POST['option4']
            
            option_one_status = request.POST.get('option_one', "0") if request.POST.get('option_one', "0")=="0" else "1"
            option_two_status = request.POST.get('option_two',"0") if request.POST.get('option_two', "0")=="0" else "1"
            option_three_status = request.POST.get('option_three', "0") if request.POST.get('option_three', "0")=="0" else "1"
            option_four_status = request.POST.get('option_four', "0") if request.POST.get('option_four', "0")=="0" else "1"
            
            
            try:
                #Saving the Questions and options
                question = Question(question_exam_name=question_exam_name, question_code=question_code, question_text=question_text, date_created=date_created, question_type=question_type)
                question.save()
                
                option_one =Option(option_question_code=option_question_code, option_id="a", option_text=option_text_one, status=option_one_status)
                option_two =Option(option_question_code=option_question_code, option_id="b", option_text=option_text_two, status=option_two_status)
                option_three =Option(option_question_code=option_question_code, option_id="c", option_text=option_text_three, status=option_three_status)
                option_four =Option(option_question_code=option_question_code, option_id="d", option_text=option_text_four, status=option_four_status)
                option_one.save()
                option_two.save()
                option_three.save()
                option_four.save()
                
                print('Successfully Submitted. Thank You')
            except :
                
                print('Something went wrong. Please try again.')
        else:
            try:
                #Saving the Essay Question 
                question = Question(question_exam_name=question_exam_name, question_code=question_code, question_text=question_text, date_created=date_created, question_type=question_type)
                question.save()
                
                print('Successfully Submitted. Thank You')
            except :
                
                print('Something went wrong. Please try again.')
        
        return redirect('admin_home')
    
    
    else:
        return render(request, 'pages/admin_home.html', context)

#######################################################################################################################


#register a lecturer and upload info to Examiner Table
def register(request):
    
    if request.method == "POST":
        examiner_name= request.POST["examiner_name"]
        examiner_code = request.POST["examiner_code"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        
        #check if password is same
        if password == password2:
            #check if user exists
            if User.objects.filter(username=examiner_name).exists():
                print('User with that name already exists.')
            else:
                #register lecturer and upload info to examiner table
                user = User.objects.create_user(username=examiner_name, password=password)
                user.save()
                examiner = Examiner(examiner_name=examiner_name, examiner_code=examiner_code)
                examiner.save()
                print("Successfully registered")
                
                return redirect('login')
                
        else:
            print("Password doesnt match")
    
    return render(request, 'pages/lecturer_register.html')
    
    
#logs in user and redirect to dashboard
def login(request):
    
    if request.method == "POST": 
        name = request.POST["examiner_name"]
        password = request.POST["password"]
        
        user = auth.authenticate(username=name, password=password)
        if user is not None:
            auth.login(request, user)
            print("Logged in successfully")
            
            return redirect('dashboard')
            
        else:
            print("Unsuccesful, verify credentials")
    
    return render(request, 'pages/lecturer_login.html')
    
    
    
def logout(request):
    
    auth.logout(request)
    print("Logged Out Successfully")
    
    return redirect('login')
    
    

#displays courses(exams) [DASHBOARD VIEW]
def display_exams(request):
    
    exams = Exam.objects.all()
    
    context = {
        "exams":exams
    }
    
    return render(request, 'pages/dashboard.html', context)



#toggle course(exam) availability
def toggle(request, course):
    
    exam = Exam.objects.get(exam_name=course)
    
    if exam.is_published:
        exam.is_published = False
    else:
        exam.is_published = True
        
    exam.save()
    
    print('Updated!')
    

    return redirect('dashboard')



#create a course(exam)[EXAM VIEW]
def create_exam(request):
    
    #if method is post; i.e to create a course(exam)
    if request.method == "POST":
        if request.user.is_authenticated:
            exam_examiner_name=request.user.username
            exam_name= request.POST["exam_name"]
            exam_code=request.POST["exam_code"]
        
            #make an exam(course) object and save
            exam = Exam(exam_examiner_name=exam_examiner_name, exam_name=exam_name, exam_code=exam_code)
            exam.save()
        
            return render(request, 'pages/create_exam.html')
        else:
            print("Not registered user")
        
    return render(request, 'pages/create_exam.html')
    
    
    


#enrol students[ENROLLMENT VIEW]
def enroll(request):
        
    if request.method == 'POST':
        student_name= request.POST["student_name"]
        student_code= request.POST["student_code"]
        student_email= request.POST["student_email"]
        student_rank= request.POST["student_rank"]
        student_level= request.POST["student_level"]
            
        #make a student object and save
        student = Student(student_name=student_name, student_code=student_code, student_email=student_email, student_level=student_level, student_rank=student_rank)
        student.save()
        
        print("Student Successfully Added")
        return render(request, 'pages/enroll.html')
    
    return render(request, 'pages/enroll.html')
        
        
        
#view enrolled students
def enrolled(request):
    
    students = Student.objects.all()
    
    context = {
        "students":students
    }
    
    return render(request, 'pages/students.html', context)



#LONGCUT Save Questions
def create_question(request, course):
    
    
    #get exams model to update number of questions
    exam = Exam.objects.get(exam_name=course)
    
    
    #get questions of exam for display
    questions = Question.objects.filter(question_exam_name=course)
    context = {
        "questions":questions,
        "course":course
    }
    
    #get question field for creation of question
    if request.method == "POST":
            
        question_type= request.POST['question_type']
        question_text= request.POST['question_text']
        question_exam_name = course
            
        question = Question(question_exam_name=question_exam_name, question_text=question_text, question_type=question_type)
        question.save()
        
        #update exam questions
        exam.number_of_questions+=1
        print(exam.number_of_questions)
        exam.save()
        print("Question created!")
            
        #get options allocated to question and save options to OBJ question
        if question_type == "objective":
            
            #list of options text
            options=[]
            
            option_text_one = request.POST.get('option_one')
            option_text_two = request.POST.get('option_two')
            option_text_three = request.POST.get('option_three')
            option_text_four = request.POST.get('option_four')
            
            #add options text to list
            options.append(option_text_one)
            options.append(option_text_two)
            options.append(option_text_three)
            options.append(option_text_four)
            
            #correct answer's index in list to question
            correct_option = request.POST.get('correct')
            
            #get options status(correct 1 or not 0)
            option_one_status = 1 if  options[int(correct_option)]==option_text_one else 0 
            option_two_status = 1 if  options[int(correct_option)]==option_text_two else 0 
            option_three_status = 1 if  options[int(correct_option)]==option_text_three else 0 
            option_four_status = 1 if  options[int(correct_option)]==option_text_four else 0 
            
            
            #save option object
            option1 = Option(option_exam_name=course, option_question_text=question_text, option_id="A", option_text=option_text_one,status=option_one_status)
            option2 = Option(option_exam_name=course, option_question_text=question_text, option_id="B", option_text=option_text_two,status=option_two_status)
            option3 = Option(option_exam_name=course, option_question_text=question_text, option_id="C", option_text=option_text_three,status=option_three_status)
            option4 = Option(option_exam_name=course, option_question_text=question_text, option_id="D", option_text=option_text_four,status=option_four_status)
            
            option1.save();option2.save();option3.save();option4.save()    
            
            print("Options Saved!")
            
        return render(request, 'pages/questions.html', context)


#create Exam(Course) Questions
def display_questions(request, course):
    
    
    #get questions for display
    questions = Question.objects.filter(question_exam_name=course)
    context = {
        "questions":questions,
        "course":course
    }
    
    
    return render(request, 'pages/questions.html', context)



#Exams submitted with responses
def submitted(request):
    
    responses = StudentExam.objects.filter(student_exam_name='')
    
    context = {
        "responses":responses
    }
    
    return render(request, 'pages/exams_submitted.html', context)    
    
        


#Students who responded to an exam
def exam_responses(request):
    
    responses = StudentExam.objects.all()
    
    context = {
        "responses":responses
    }
    
    return render(request, 'pages/exam_responses.html', context)


#A student responce and scoring of exam
def student_response(request):
    
    responses = StudentExam.objects.all()
    
    context = {
        "responses":responses
    }
    
    return render(request, 'pages/student_response.html', context)



        
        
