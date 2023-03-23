from django.shortcuts import render

# Create your views here.

def calculate (request, num1, num2):
    context = {
        'num1' : num1,
        'num2' : num2,
    }

    return render(request, 'calculate.html', context)