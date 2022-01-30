from django.contrib.auth.signals import user_logged_in
from django.shortcuts import render
from .forms import Student_entryForm
from  .models import StudentAttend 
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import logout,authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail,BadHeaderError

# Create your views here.
def index(request):
    return render(request,'classroom/index.html')

def home(request):
    return render(request,'classroom/home.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def student_entry (request):
    if request.method == "POST":
       form = Student_entryForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect(reverse('index'))
    else:
        form = Student_entryForm()
    return render(request,'classroom/student_entry.html',{'form':form})

def register(request):
   if request.method == "POST":
       form = UserCreationForm(request.POST)
       if form.is_valid():
           new_user = form.save()
           authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
           login(request, authenticated_user)
           return HttpResponseRedirect(reverse('index'))
   else:
        form = UserCreationForm()
   return render(request,'classroom/register.html',{'form':form})

def your_attendance(request):
    student = StudentAttend.objects.all()
    return render(request,'classroom/your_attendance.html',{'student':student})

def sendmail(request):
    student = StudentAttend.objects.filter(attendence ="A")
    recipient_list = []
    for data in student:
        recipient_list.append(data.email)
    subject = 'absent'
    message = 'you were absent today. please contact your department to verify reason for absent'
    email_from = 'puja.ray8176@gmail.com'
    try:
        send_mail( subject, message, email_from, recipient_list ) 
    except BadHeaderError:
        return HttpResponse('Invalid error found')
    return HttpResponse('email was send succefully')
    