from django.shortcuts import render

# Create your views here.

def detail (request, num):
    # num 변수로 DB에서 몇 번 글을 조회하는지 검색할 때 사용 

    context = {
        'num' : num,
    }
    return render(request, 'detail.html', context)


# ''누구''님 안녕하세요! 출력 코드
def detail_name (request, name):

    context = {
        'name' : name,
    }
    return render(request, 'detail_name.html', context)