from django.shortcuts import render,redirect
from.models import User
def form (request):
    return render(request ,'index.html')
def handle(request):
    User.creat_user(first=request.POST['fname'],last=request.POST['lname'], email=request.POST['email1'],age=request.POST['age1'])
    
    
    return redirect('/form')
def result(request):
    context={
        'allusers':User.all_user()
    }
    return render(request,'index.html', context )

# Create your views here.
