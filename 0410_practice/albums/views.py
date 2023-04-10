from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm

# Create your views here.

def create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('albums:create')
    else:
        form = AlbumForm()

    creates = Album.objects.order_by('pk')
    context = {
        'form' : form,
        'creates' : creates,
    }

    return render(request, 'create.html', context)