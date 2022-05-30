from email.message import Message
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

#from .tasks import wish
from django.contrib import messages
from datetime import date
from wisher.models import Birth, prop, orig, orga
#from django.db.models.query_utils import DeferredAttribute

# Superuser test uhhhh

from django.contrib.admin.views.decorators import staff_member_required

# End of super user test uhhhhhh

def supa(user):
    x = False
    if user.is_superuser:
        x = True
    return x

# Create your views here.
def login (request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('profile')
        
        else:
            messages.error(request,"Invalid credentials")
            return redirect('login')
        
    
    return render(request, 'login.html')

def logout (request):
    auth_logout(request)
    return redirect('/')

def signup (request):
    
    if request.method == "POST":
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        copass = request.POST['copass']
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username Already Exists")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email Already Exists")
            return redirect ('signup')
            

        if len(username)>25:
            messages.error(request,"Username is too Long")
            return redirect('signup')   

        if len(username)<4:
            messages.error(request,"Username is too short")
            return redirect('signup')  
                  
        if password !=copass:
            messages.error(request,"Passwords Does not match")
            return redirect('signup')  
            
        if not username.isalnum():
            messages.error(request,"Username should only consist of Alpha-Numeric characters")
            return redirect('signup')  
            
        user = User.objects.create_user(username, email , password)
        user.is_active = True
        user.save()
        messages.success(request, "Account created Sucessfully ")
        return redirect('signup')

          
    
    return render(request, 'signup.html')

@user_passes_test(supa, login_url='sus')
def addb (request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        bday = request.POST['bday']
        team = request.POST['team']
        adder = Birth(name=name, email=email, bday=bday, team=team)
        adder.save()
        messages.success(request, " Birthday of a Member added Sucessfully ")
        return redirect('addb')
        
        
    return render(request, 'addb.html')


@user_passes_test(supa, login_url='sus')
def updm (request):
    if request.method == "POST":
        newmes = request.POST['newmes']
        messi = prop.objects.get(id=5)
        messi.greet = newmes
        messi.save()
        messages.success(request, " Birthday Wish Updated Sucessfully ")
        return redirect('updm')
    return render(request, 'updm.html')


@user_passes_test(supa, login_url='sus')
def updex (request):
    if request.method == "POST":
        numa = request.POST['numa']
        rex = orga.objects.get(id=1)
        rex.ex = numa
        rex.save()
        messages.success(request, " Executive's email was Updated Sucessfully ")
        return redirect('updex')
    return render(request, 'updex.html')


def ui (request):
    B = date.today()
    Wishs = prop.objects.only('greet')
    for Prop in Wishs:
        X = Prop.greet
    print(Birth.objects, "Birthday")
    print(date.today(), "Today")
    #print(W, "Messages")

    births = Birth.objects.filter(bday = B )
    print(births)
    for birth in births:
        #from wisher.models import prop
        #print(W)
        print(birth.bday , birth.name)
        messages.success(request, "Happy Birthday, " + birth.name)
        print("happy birthday", birth.bday, birth.name)
        
    return render(request, 'ui.html')

@login_required(login_url='login')   
def profile (request):
    Wishs = prop.objects.only('greet')
    Inc = orga.objects.only('ex')
    Bi = date.today()   
    bir = Birth.objects.filter(bday = Bi )
    
    
    return render(request, 'profile.html', {
        'Wishs':Wishs ,
        'Inc': Inc,
        'bir': bir,
    })
    

def sus(request):
    return render(request, 'error.html')

def appro(request):
    return render(request, 'appro.html')