from django.conf import settings
from django.contrib import messages, auth
from django.shortcuts import render, redirect


# Create your views here.


def CreateUser(request):
    if request.user.is_authenticated:
        return redirect('apps:index')

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get('password')
        username = request.POST.get('username') if request.POST.get('username') else email
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        User = settings.AUTH_USER_MODEL

        #         check if username is taken
        if User.objects.filter(username=username).exists():
            messages.error(request, message="Username is already taken")
            return redirect(request.path_info)
        elif User.objects.filter(email=email).exists():
            messages.error(request, message="Email is already taken")
            return redirect(request.path_info)
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            if user:
                user.set_password(password)
                user.save()
                return redirect('/login')
            else:
                messages.error(request, message="Error occurred and your account was not created successfully, "
                                                "let's give it another shot")
                return redirect(request.path_info)

    return render(request, 'profiles/Register.html')


def Login(request):
    if request.user.is_authenticated:
        return redirect('apps:index')

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email == "" or password == "":
            messages.error(request, "Email/Username and password are required")
            return redirect(request.path_info)

        login_attempt = auth.authenticate(
            email=email, password=password)
        if login_attempt is not None:
            auth.login(request, login_attempt)
            messages.success(request, "You are logged in")
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('apps:index')
        else:
            messages.error(request, "No user is associated with the given credentials.")
    return render(request, 'profiles/Login.html')
