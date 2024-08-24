from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


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


# def register(request):
    
#     context = {}
#     return render(request, "ayth/register.html", context)
