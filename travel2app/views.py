from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def home2(request):
    return render(request,'home2.html')
def login(request):
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')
def budget(request):
    return render(request,'budget.html')
def india(request):
    return render(request,'india.html')
def book(request):
    return render(request,'book.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')