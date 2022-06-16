from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from .decorators import unauthenticatedUser


@unauthenticatedUser
def loginView(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('course:enrol_list')
        else:
            messages.info(
                request, 'Password is case sensitive and/or password does not match email address')

    return render(request, 'accounts/login.html')


def logoutView(request):
    logout(request)
    return redirect('/')


