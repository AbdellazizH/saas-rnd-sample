from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.contrib.auth import get_user_model

User = get_user_model()


def login_view(request):
    page_title = "Login Page"
    if request.method == "POST":
        username = request.POST.get("username") or None
        password = request.POST.get("password") or None
        if all([username, password]):
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("Login here!")
                                    
                return redirect("/")
    
    context = {"page_title": page_title}
    return render(request, "auth/login.html", context)


def register_view(request):
    page_title = "Regiter Page"
    if request.method == "POST":
        username = request.POST.get("username") or None
        email = request.POST.get("email") or None
        password = request.POST.get("password") or None
        # Django Forms
        # user_exists_qs = User.objects.filter(username__iexact=username).exists()
        # email_exists_qs = User.objects.filter(email__iexact=email).exists()
        try:
            User.objects.create_user(username=username, email=email, password=password)
        except:
            pass
        # if all([username, email, password]):
        #     user = authenticate(request, username=username, email=email, password=password)
        #     if user is not None:
        #         login(request, user)
        #         print("Register here!")
                                    
                # return redirect("/")
    
    context = {"page_title": page_title}
    return render(request, "auth/register.html", context)
