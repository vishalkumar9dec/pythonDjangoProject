from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        uname = request.POST['userName']
        password = request.POST['password']

        user = auth.authenticate(username=uname,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invaild Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        fname = request.POST['firstName']
        lname = request.POST['lastName']
        uname = request.POST['userName']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'Username already available')
                print('Username Not Available')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already available')
                print('Email already available')
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=password1)
                user.save();
                print('User Created Successfully')
                return redirect('login')
        else:
            print('Password Not Matching')
            return redirect('register')

    else:
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

# def Jaipur(request):
#     return render(request,'Jaipur.html')

