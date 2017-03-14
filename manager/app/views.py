from django.shortcuts import render
from django.contrib import auth
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from app import models
# Create your views here.
def index(request):
    return render(request, 'app/index.html')


def test(request):
    return render(request, 'app/test.html')


def signin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username, password=password)
    if user:
        auth.login(request, user)
    return HttpResponseRedirect('/')
    #     JsonResponse({'status': True, 'message':'登录成功'})
    # else:
    #     JsonResponse({'status':False, 'message' : "用户名或密码错误"})

def logout(request):
    auth.logout(request)
    return render(request, 'app/index.html')

def supervision(request):
    supervisor = models.Supervision.objects.all()
    return render(request, 'app/supervision.html' , {'data' : supervisor})