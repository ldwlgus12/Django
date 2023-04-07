from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserChangeForm, CustomUserCreationForm
from posts.models import Post
from posts.forms import PostForm



# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:base')
    else:
        form = AuthenticationForm()

    all_cnt = Post.objects.all().count()
    dev_cnt = Post.objects.filter(category='개발').count()
    cs_cnt = Post.objects.filter(category='CS').count()
    new_cnt = Post.objects.filter(category='신기술').count()
    context = {
        'form': form,
        'all_cnt': all_cnt,
        'dev_cnt': dev_cnt,
        'cs_cnt': cs_cnt,
        'new_cnt': new_cnt,
    }
    return render(request, 'accounts/login.html', context)


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:base')
    else:
        form = CustomUserCreationForm()      
    all_cnt = Post.objects.all().count()
    dev_cnt = Post.objects.filter(category='개발').count()
    cs_cnt = Post.objects.filter(category='CS').count()
    new_cnt = Post.objects.filter(category='신기술').count()
    context = {
        'form': form,
        'all_cnt': all_cnt,
        'dev_cnt': dev_cnt,
        'cs_cnt': cs_cnt,
        'new_cnt': new_cnt,
    }
    return render(request, 'accounts/signup.html', context)

    


def logout(request):
    auth_logout(request)
    return redirect('posts:base')


def delete(request):
    request.user.delete()
    return redirect('posts:base')


def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('posts:base')
    else:
        form = CustomUserChangeForm(instance=request.user)
    all_cnt = Post.objects.all().count()
    dev_cnt = Post.objects.filter(category='개발').count()
    cs_cnt = Post.objects.filter(category='CS').count()
    new_cnt = Post.objects.filter(category='신기술').count()
    context = {
        'form': form,
        'all_cnt': all_cnt,
        'dev_cnt': dev_cnt,
        'cs_cnt': cs_cnt,
        'new_cnt': new_cnt,
    }
    return render(request, 'accounts/update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('accounts:base')
    else:
        form = PasswordChangeForm(request.user)
    all_cnt = Post.objects.all().count()
    dev_cnt = Post.objects.filter(category='개발').count()
    cs_cnt = Post.objects.filter(category='CS').count()
    new_cnt = Post.objects.filter(category='신기술').count()
    context = {
        'form': form,
        'all_cnt': all_cnt,
        'dev_cnt': dev_cnt,
        'cs_cnt': cs_cnt,
        'new_cnt': new_cnt,
    }
    return render(request, 'accounts/change_password.html', context)


def detail(request):
    all_cnt = Post.objects.all().count()
    dev_cnt = Post.objects.filter(category='개발').count()
    cs_cnt = Post.objects.filter(category='CS').count()
    new_cnt = Post.objects.filter(category='신기술').count()
    context = {
        'all_cnt': all_cnt,
        'dev_cnt': dev_cnt,
        'cs_cnt': cs_cnt,
        'new_cnt': new_cnt,
    }
    return render(request, 'accounts/detail.html', context)