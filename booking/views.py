from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render , redirect
from .models import Subject, Register
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'booking/index.html', {
        'booking' : Subject.objects.filter(status=True)
    })    

def subject(request, subject_id):
    user = User.objects.get(pk=request.user.id)
    subject = Subject.objects.get(pk=subject_id)
    regist = Register.objects.filter(user=user ,subject=subject)
    seat = len(Register.objects.filter(subject_id = subject_id).all())
    return render(request, 'booking/subject.html', {
        'regist': regist,
        'subject': subject,
        'seat': seat
    })

def enrollment(request, subject_id):
    student_data = User.objects.get(pk=request.user.id)
    subject_data = Subject.objects.get(pk=subject_id)
    check_regist = Register.objects.filter(user=student_data, subject=subject_data)
    quota = subject_data.quota
    if(len(check_regist) <= 0):
        count_student = Register.objects.filter(subject=subject_data)
        if(len(count_student) >= quota ):
            return redirect('/booking')
        else:
            enrollment = Register.objects.create(user=student_data, subject=subject_data)
            seat = len(Register.objects.filter(subject_id = subject_id).all())
            subject = Subject.objects.get(pk=subject_id)
            subject.student = seat
            subject.save()
            return redirect('/booking')
    else:
        return redirect('/booking')

def enroll_list(request):
    enroll_list = Register.objects.filter(user_id=request.user.id).all()
    return render(request, 'booking/enroll.html', {
        'enroll_list': enroll_list
    })
    
def unenrollment(request , subject_id):
    student_data = User.objects.get(pk=request.user.id)
    subject_data = Subject.objects.get(pk=subject_id)
    unenrollment = Register.objects.filter(user=student_data, subject=subject_data).delete()
    seat = len(Register.objects.filter(subject_id = subject_id).all())
    subject = Subject.objects.get(pk=subject_id)
    subject.student = seat
    subject.save()
    return redirect('/booking')





