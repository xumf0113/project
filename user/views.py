from django.shortcuts import render, redirect
from django.urls import reverse


def login(request):
    """登录页面"""
    return render(request, 'user/login.html')


def register(request):
    """注册页面"""
    return render(request, 'user/register.html')


def login_out(request):
    user = request.user
    del request.session[user]
    return redirect(reverse('user:login'))


def login_handle(request):
    """注册处理"""
    post = request.POST
    username = post.get('username')
    password = post.get('username')
    username = post.get('username')

    return redirect(reverse('blog:index'))
