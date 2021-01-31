from django.shortcuts import render,HttpResponse
from home.models import Contact
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def projects(request):
    return render(request,'projects.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        desc=request.POST['desc']
        #print(name,email,desc)
        ins=Contact(name=name,email=email,desc=desc)
        ins.save()
        print('The data has been written to db')
    return render(request,'contact.html')
