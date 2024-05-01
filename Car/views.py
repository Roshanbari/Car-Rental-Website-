from django.shortcuts import render
from django.http import HttpResponse
from Car.models import Contact ,Signup,Login,Book

# Create your views herev python function

def home(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message') 
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
    return render(request, 'homepage.html')

def login(request):
    if request.method == "POST":
        login = Login()
        email = request.POST.get('email')
        password = request.POST.get('password') 
        login.email = email
        login.password = password
        login.save()
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        signup = Signup()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password') 
        signup.name = name
        signup.email = email
        signup.phone = phone
        signup.password = password
        signup.save()
    return render(request, 'signup.html')

def book(request):
    if request.method == "POST":
        book = Book()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        car = request.POST.get('car')
        pdate = request.POST.get('pickup_date')
        rdate = request.POST.get('return_date')
        book.name = name
        book.email = email
        book.phone = phone
        book.pickup_date = pdate
        book.return_date = rdate
        book.car = car
        book.save()
    return render(request, 'book.html')
