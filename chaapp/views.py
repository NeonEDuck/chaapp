from django.shortcuts import render, redirect
from chaapp.forms import PostForm
from django.contrib.auth import authenticate
from django.contrib import auth

# Create your views here.

def index(request):
    if request.method == 'POST':
        postform = PostForm(request.POST)
        if postform.is_valid():
            username = postform.cleaned_data['username']
            pd = postform.cleaned_data['pd']
            userauth = authenticate(username=username, password=pd)

            if userauth is not None:
                auth.login(request, userauth)
                postform = PostForm()
                return redirect('/manage/')
            else:
                massage = '登入失敗！'
        else:
            message = '驗證碼錯誤！'
    else:
        message = '帳號、密碼及驗證碼都必須輸入！'
        postform = PostForm()
    return render(request, 'index.jinja', locals())

def manage(request):
    return render(request, 'manage.jinja', locals())