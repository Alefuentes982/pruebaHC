from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.landing_page, name="landing_page"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
]
