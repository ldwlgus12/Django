from django.shortcuts import render

# Create your views here.

def number_print(request, num):
    context = {
        'num' : num,
    }

    return render(request, 'number_print.html', context)