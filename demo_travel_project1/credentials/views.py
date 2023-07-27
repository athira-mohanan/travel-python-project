from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['passwd']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return render(request,"login.html")
def fun_registration(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email_id = request.POST['email_id']
        username = request.POST['username']
        passwd = request.POST['passwd']
        confirmpwd = request.POST['confirmpwd']

        if passwd == confirmpwd:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('fun_registration')
            elif User.objects.filter(email=email_id).exists():
                messages.info(request, "Email id Taken")
                return redirect('fun_registration')
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email_id,
                                                username=username, password=passwd)
                user.save()
                return redirect('login')

        else:
            messages.info(request, "Password not matching")
            return redirect('fun_registration')

    return render(request, "register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')