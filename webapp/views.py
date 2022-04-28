from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import student
from .forms import studentForm,studentFormOne

# Create your views here.
def index(request):
    return render(request,'index.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            #return render(request,'actual.html')
            return redirect('home')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    
    else:
        return render(request,'login.html')

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['emailid']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            #return render(request,'Project.html')
            return redirect('home')
            #return redirect('')
        else:
            messages.info(request,'invalid credentials')
            return redirect('adminlogin')
    
    else:
        return render(request,'adminlogin.html')

def actual(request):
    submitted = False
    if request.method == "POST":
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"index.html")
    else:
        form = studentForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request,'actual.html',{'form':form})
'''def actual(request):

    if request.method == 'POST':
        print("Hi")
        if request.POST.get('name') and request.POST.get('rollno') and request.POST.get('Residence') and request.POST.get('phoneNo') and request.POST.get('year') and request.POST.get('description') and request.POST.get('prefer'):
            print("Hi")
            post=student()
            post.name = request.POST.get('name')
            post.rollnumber = request.POST.get('rollno')
            post.Residence = request.POST.get('Residence')
            post.phoneNo = request.POST.get('phoneNo')
            post.year = request.POST.get('year')
            post.description = request.POST.get('description')
            post.prefer = request.POST.get('prefer')
            post.save()
            print(request.POST.get('prefer'))

            # return HttpResponseRedirect("http://127.0.0.1:8000/")
            return render(request,"index.html")
            #return redirect('home')
    else:
        # messages.info(request,"Invalid Credentials")
        return render(request,'actual.html')  
        # return redirect('home')
        #return redirect("actual")
'''
def display(request):
    stds = student.objects.all()
    return render(request,'display.html',{'stds' : stds})


def update_student(request, student_id):
    stud = student.objects.get(pk=student_id)
    form = studentFormOne(request.POST or None, instance=stud)
    if form.is_valid():
        form.save()
        return redirect('display')

    return render(request, 'update_student.html',{'stud' : stud,'form':form})

def result(request,student_id):
    stds = student.objects.get(pk=student_id)
    return render(request,'result.html',{'stds': stds})