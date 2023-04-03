from django.shortcuts import render, redirect
from .models import Article
from .forms import AritlcleForm

# Create your views here.

def index(request):
    # DB에 전체 게시글 조회를 요청하고 쿼리셋을 응답받아 저장
    articles = Article.objects.all()
    # print(articles)
    context = {
        'articles' : articles
    }

    return render(request, 'articles/index.html', context)



def detail(request, pk):
    # pk=pk에서 왼쪽 pk는 컬럼, 오른쪽은 위 def detail(request, pk):의 pk와 같다.
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article,
    }

    return render(request, 'articles/detail.html', context)




# ========================================
def create(request):
    # HTTP request method POST 라면
    if request.method == "POST":
        form = AritlcleForm(request.POST)

        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
        # context = {
        #     'form' : form,
        # }
        # return render(request, 'articles/new.html', context)

    # POST가 아니라면
    else:
        form = AritlcleForm()

    context = {
        'form' : form,
    }
    return render(request, 'articles/new.html', context)
# ========================================




# def new(request):
#     # 0403 - Form class를 적용한 new로직
#     form = AritlcleForm()
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/new.html', context)



# def create(request):
#     # new에서 보낸 사용자 데이터를 받아서 변수에 할당
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')

#     # ========================================

#     # 0403 - Form class를 적용한 create로직
#     form = AritlcleForm(request.POST)

#     # 통과를 했을 때
#     if form.is_valid():
#         article = form.save()
#         return redirect('articles:detail', article.pk)
    
#     # 통과를 못했을 때
#     context = {
#         'form' : form,
#     }
    
#     return render(request, 'articles/new.html', context)

    # ========================================


    
    # 받은 데이터를 DB에 저장
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2 (가장 적절한 방법)
    # 저장 전에 유효성 검사와 같은 추가 작업을 위해 2번 방법을 택함
    # article = Article(title=title, content=content)
    # article.save()

    # 3
    # Article.objects.create(title=title, content=content)

    # 결과 페이지 반환 
    # return render(request, 'articles/create.html')


# ---------------------------------------------------------------

    # 0330 - redirect()

    # 이동할 주소(url)를 사용자에게 반환
    # return redirect('articles:index')

    # 생성한 글의 단일 조회(detail) 주소(url)로 이동 응답
    # return redirect('articles:detail', article.pk)



def delete(request, article_pk):
    # 삭제할 데이터 조회
    article = Article.objects.get(pk=article_pk)

    # 조회한 데이터 삭제 (DELETE)
    article.delete()

    # 전체 조회 페이지로 이동
    return redirect('articles:index')



# def edit(request, article_pk):
#     # 수정할 데이터 조회
#     article = Article.objects.get(pk=article_pk)

#     # ========================================

#     form = AritlcleForm(instance=article)

#     context = {
#         'article' : article,
#         'form' : form,
#     }

#     # ========================================

#     return render(request, 'articles/edit.html', context)



# def update(request, article_pk):
#     # # 수정 작업 과정
#     # # 1. 데이터 조회
#     # article = Article.objects.get(pk=article_pk)

#     # # 2. 데이터 수정
#     # # 2-1. 사용자가 입력한 form 데이터 저장
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')

#     # # 2-2. 조회한 데이터(article)의 필드 값 변경
#     # article.title = title
#     # article.content = content

#     # # 3. 데이터 저장
#     # article.save()

#     # ========================================

#     article = Article.objects.get(pk=article_pk)
#     form = AritlcleForm(request.POST, instance=article)


#     if form.is_valid():
#         article = form.save()
#         return redirect('articles:detail', article.pk)
    
#     context = {
#         'article' : article,
#         'form' : form,
#     }
    
#     return render(request, 'articles/edit.html', context)



# ========================================

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    if request.method == 'POST':
        form = AritlcleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
        

    else:
        form = AritlcleForm(instance=article)
    context = {
        'article' : article,
        'form' : form,
    }
    return render(request, 'articles/edit.html', context)

