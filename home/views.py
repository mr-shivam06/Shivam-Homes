from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "variable1":"//Shivam is GREAT//",
        "variable2":"//Greatness comes from heart//"
    }
    # messages.success(request, "This is a test message.")
    return render(request, 'index.html',context)
    # return HttpResponse("Welcome to the home page.")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("Information about us....")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("Here are the things you can do.")

def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        description=request.POST.get("description")
        contact=Contact(name=name,email=email,phone=phone,description=description,date=datetime.today())
        contact.save()
        messages.success(request, "YOUR MESSAGE HAS BEEN SENT. THANK YOU FOR YOUR RESPONSE!")
    return render(request, 'contact.html')
    # return HttpResponse("Mention your problems.")

