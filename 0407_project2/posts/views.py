from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

# Create your views here.
def base(request):
    posts = Post.objects.order_by('-pk')
    all_cnt = Post.objects.all().count()
    dev_cnt = Post.objects.filter(category='개발').count()
    cs_cnt = Post.objects.filter(category='CS').count()
    new_cnt = Post.objects.filter(category='신기술').count()
    context = {
        'posts': posts,
        'all_cnt': all_cnt,
        'dev_cnt': dev_cnt,
        'cs_cnt': cs_cnt,
        'new_cnt': new_cnt,
        'subject': '전체',
    }
    return render(request, 'posts/base.html', context)


def category(request, subject):
    posts = Post.objects.filter(category=subject).order_by('-pk')
    all_cnt = Post.objects.all().count()
    dev_cnt = Post.objects.filter(category='개발').count()
    cs_cnt = Post.objects.filter(category='CS').count()
    new_cnt = Post.objects.filter(category='신기술').count()
    context = {
        'posts' : posts,
        'all_cnt': all_cnt,
        'dev_cnt': dev_cnt,
        'cs_cnt': cs_cnt,
        'new_cnt': new_cnt,
        'subject': subject,
    }
    return render(request, 'posts/base.html', context)
    


def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    all_cnt = Post.objects.all().count()
    dev_cnt = Post.objects.filter(category='개발').count()
    cs_cnt = Post.objects.filter(category='CS').count()
    new_cnt = Post.objects.filter(category='신기술').count()
    context = {
        'post': post,
        'all_cnt': all_cnt,
        'dev_cnt': dev_cnt,
        'cs_cnt': cs_cnt,
        'new_cnt': new_cnt,
    }
    return render(request, 'posts/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:base')
    else:
        form = PostForm()
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
    return render(request, 'posts/create.html', context)


@login_required
def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:base')
    else:
        form = PostForm(instance=post)
    all_cnt = Post.objects.all().count()
    dev_cnt = Post.objects.filter(category='개발').count()
    cs_cnt = Post.objects.filter(category='CS').count()
    new_cnt = Post.objects.filter(category='신기술').count()
    context = {
        'post': post,
        'form': form,
        'all_cnt': all_cnt,
        'dev_cnt': dev_cnt,
        'cs_cnt': cs_cnt,
        'new_cnt': new_cnt,
    }
    return render(request, 'posts/update.html', context)


@login_required
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('posts:base')