from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),

]
