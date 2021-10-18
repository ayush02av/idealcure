from django.shortcuts import render, redirect
from database.models import *
import commonfunctions

from django.views.generic import TemplateView
from django.contrib import auth

class login(TemplateView):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/profile')
        return render(request, 'auth/login.html', {'show_header_footer':True})

    def post(self, request):
        username = request.POST['number']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/dashboard')
        else:
            return redirect('/login')

class logout(TemplateView):
    def get(self, request):
        if request.user.is_authenticated:
            auth.logout(request)
        return redirect('/profile')

class profile(TemplateView):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/dashboard')
        else:
            return redirect('/login')