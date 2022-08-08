from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'GET':
        return render(request, template_name='userapp/login.html')
    elif request.method == 'POST':
        user = request.POST.get('user')
        password = request.POST.get('password')
        user = authenticate(request, username=user, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        5/0
