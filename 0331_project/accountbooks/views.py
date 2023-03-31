from django.shortcuts import render, redirect
from .models import AccountBook

# Create your views here.
def index(request):
    acounts = AccountBook.objects.all()
    context = {
        'acounts': acounts,
    }
    return render(request, 'accountbooks/index.html', context)


def new(request):
    return render(request, 'accountbooks/new.html')


def create(request):
    note = request.POST.get('note')
    category = request.POST.get('category')
    amount = request.POST.get('amount')
    date = request.POST.get('date')
    description = request.POST.get('description')

    acount = AccountBook(note=note, category=category, amount=amount, date=date, description=description)
    acount.save()

    return redirect('accountbooks:index')


def detail(request, pk):
    account = AccountBook.objects.get(pk = pk)
    context = {
        'account' : account
    }

    return render(request, 'accountbooks/detail.html', context)


def edit(request, pk):
    account = AccountBook.objects.get(pk = pk)
    context = {
        'account' : account
    }

    return render(request, 'accountbooks/edit.html', context) 


def update(request, pk):
    account = AccountBook.objects.get(pk = pk)
    
    account.note = request.POST.get('note')
    account.category = request.POST.get('category')
    account.amount = request.POST.get('amount')
    account.date = request.POST.get('date')
    account.description = request.POST.get('description')

    account.save()

    return redirect('accountbooks:detail', account.pk)


def delete(request, pk):
    account = AccountBook.objects.get(pk = pk)
    account.delete()

    return redirect('accountbooks:index')


def copy(request, pk):
    account = AccountBook.objects.get(pk=pk)

    # 방법 1
    # copy_account = AccountBook.objects.create(
    #     note = account.note,
    #     category = account.category,
    #     amount = account.amount,
    #     date = account.date,
    #     description = account.description,
    # )

    # 방법 2
    note = account.note
    category = account.category
    amount = account.amount
    date = account.date
    description = account.description
    

    account = AccountBook(note=note, category=category, amount=amount, date=date, description=description)
    

    account.save()

    return redirect('accountbooks:index')