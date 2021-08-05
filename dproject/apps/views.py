from django.shortcuts import render,redirect
from apps.forms import StudentForm
from django.contrib.auth.models import User
from apps.models import Student
from django.contrib.sessions.models import Session
from django.contrib import auth




def welcome(request):
    return render(request,'welcome.html')
def studentdata(request):
    data = Student.objects.all()
    return render(request,'studentdata.html',{'data':data})
    


def show_student(request):
    if request.session.has_key('is_logged'):
        data = Student.objects.all()
        return render(request,'show.html',{'data':data})
    return redirect("/login/")

def add_student(request):
    form = StudentForm()
    print(request.POST)
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/show/")
    return render(request,'add.html',{'form':form})


def update_student(request,id):
    obj = Student.objects.get(pk = id)
    form = StudentForm(instance = obj)
    if request.method == "POST":
        form = StudentForm(request.POST,instance = obj)
        if form.is_valid():
            form.save()
            return redirect("/show/")
    return render(request, 'update.html', {'form': form,'obj':obj})

def delete_student(request,id):
    obj = Student.objects.get(pk=id)
    obj.delete()
    return redirect("/show/")


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        password = request.POST['password']
        x=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password)
        x.save()
        print("USER CREATED")
        return redirect('/welcome/')
    return render(request,'signup.html')


def login(request):
    if request.session.has_key('is_logged'):
        return redirect("/show/")
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['password']
        user=auth.authenticate(username=username1,password=password1)
        if user is None:
            return redirect('/login/')
        else:
            request.session['is_logged']=True
            return redirect('/show/')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/welcome/')
