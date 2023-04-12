from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Review, Comment
from .forms import ReviewForm, CommentForm

# Create your views here.

def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/index.html', context)



def detail(request, pk):
    reviews = Review.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = reviews.comment_set.all()
    context = {
        'reviews': reviews,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'reviews/detail.html', context)



@login_required
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            reviews = form.save(commit=False)
            reviews.user = request.user
            reviews.save()
            return redirect('reviews:detail', reviews.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form,
    }
    return render(request, 'reviews/create.html', context)



@login_required
def delete(request, review_pk):
    reviews = Review.objects.get(pk=review_pk)
    if request.user == reviews.user:
        reviews.delete()
    return redirect('reviews:index')



@login_required
def update(request, review_pk):
    reviews = Review.objects.get(pk=review_pk)
    if request.user == reviews.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=reviews)
            if form.is_valid():
                form.save()
                return redirect('reviews:detail', reviews.pk)
        else:
            form = ReviewForm(instance=reviews)
    else:
        return redirect('reviews:detail', reviews.pk)
    
    context = {
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'reviews/update.html', context)



@login_required
def comments_create(request, review_pk):
    reviews = Review.objects.get(pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = reviews
        comment.user = request.user
        comment.save()
        return redirect('reviews:detail', review_pk)
    context = {
        'reviews' : reviews,
        'comment_form' : comment_form,
    }
    return render(request, 'reviews/detail.html', context)



@login_required
def comments_delete(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('reviews:delete', review_pk)
