from django.shortcuts import render
import random

# Create your views here.

def today_dinner(request):
    foods = ['치킨', '삼겹살', '마라탕', '샤브샤브', '짜장면', '보쌈', '초밥']
    random_food = random.choice(foods)

    context = {
        'foods' : random_food,
    }

    return render(request, 'today_dinner.html', context)

# -----------------------------------------------------------

def throw(request):
    return render(request, 'throw.html')


def catch(request):
    data = request.GET.get('message')

    context = {
        'data': data,
    }

    return render(request, 'catch.html', context)

# -----------------------------------------------------------

def lotto_create(request):
    return render(request, 'lotto_create.html')


def lotto(request):
    data = int(request.GET.get('message'))

    number = []
    
    for i in range(data):
        number.append(sorted(random.sample(range(1, 46), 6)))

    context = {
        'number' : number     
    }

    return render(request, 'lotto.html', context)
