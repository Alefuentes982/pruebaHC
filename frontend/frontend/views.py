from django.shortcuts import render
import requests


def landing_page(request):
    return render(request, "frontend/landing_page.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        response = requests.post(
            "http://localhost:9010/api/login/",
            data={"username": username, "password": password},
        )
        if response.status_code == 200:
            tokens = response.json()
            request.session["access"] = tokens["access"]
            request.session["refresh"] = tokens["refresh"]
            return redirect("landing_page")
        else:
            return render(
                request, "frontend/login.html", {"error": "Invalid credentials"}
            )
    return render(request, "frontend/login.html")


def register_view(request):
    if request.method == "POST":
        form_data = {
            "username": request.POST["username"],
            "password1": request.POST["password1"],
            "password2": request.POST["password2"],
        }
        response = requests.post("http://localhost:9010/api/register/", data=form_data)
        if response.status_code == 201:
            tokens = response.json()
            request.session["access"] = tokens["access"]
            request.session["refresh"] = tokens["refresh"]
            return redirect("login")
        else:
            return render(request, "frontend/register.html", {"error": response.json()})
    return render(request, "frontend/register.html")
