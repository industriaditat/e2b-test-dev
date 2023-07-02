```python
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponse("User logged in")
            else:
                return HttpResponse("Account not active")
        else:
            return HttpResponse("Invalid login details")
    else:
        return HttpResponse("Invalid method")

@csrf_exempt
def user_logout(request):
    logout(request)
    return HttpResponse("Logged out")

@login_required
def index(request):
    return render(request, 'app/index.html', {})
```