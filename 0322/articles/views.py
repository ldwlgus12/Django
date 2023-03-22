from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'name' : 'Harry',
    }
    return render(request, 'index.html', context)


def dinner(request):
    foods = ['치킨', '닭갈비', '볶음밥', '샤브샤브',]
    context = {
        'foods' : foods
    }
    return render(request, 'dinner.html', context)


def search(request):
    return render(request, 'search.html')


def throw(request):
    return render(request, 'throw.html')


def catch(request):
    # print(request)
    # print(type(request))
    # print(dir(request))
    # print(request.GET)
    # print(request.GET.get('message'))

    data = request.GET.get('message')

    context = {
        'data' : data,
    }

    return render(request, 'catch.html', context)