# 할 일 Model & ORM

# 1번
Todo.objects.create(content='실습 제출', priority='5', completed='False', deadline='2023-03-28')

# 2번
Todo.objects.create(content='데일리 설문(오후) 제출', deadline='2023-03-28')

# 3번
Todo.objects.create(content='스터디 모임', deadline='2023-03-28')
Todo.objects.create(content='스터디 리뷰 남기기', priority='2', deadline='2023-03-28')
Todo.objects.create(content='알고리즘 문제풀이', deadline='2100-01-01')
Todo.objects.create(content='콩이 화장실 청소', priority='6', deadline='2023-03-28')
Todo.objects.create(content='노래 듣기', priority='7', deadline='2023-03-28')

# 4번
Todo.objects.order_by('pk')

# 5번
Todo.objects.order_by('-priority')

# 6번
Todo.objects.get(pk=1)

# --------------------------------------------------------------

# 신문 Model & ORM

# 1번
pk1 = Newspaper.objects.get(pk=1)
pk1.journalist

# 2번
laney = Newspaper.objects.filter(journalist='Laney Mccullough')
len(laney)

# 3번
Newspaper.objects.order_by('-pk')

# 4번
Newspaper.objects.order_by('-created_at')

# 5번
len(Newspaper.objects.filter(journalist__contains='Britney'))

# 6번
a = len(Newspaper.objects.filter(journalist__contains='Britney Mahoney'))
b = len(Newspaper.objects.filter(journalist__contains='Arianna Walls'))
c = len(Newspaper.objects.filter(journalist__contains='Carl Short'))
a+b+c

# 7번
len(Newspaper.objects.filter(created_at__gte='2000-01-01'))

# 8번
last = Newspaper.objects.get(pk=10000)
print(f'title : {last.title}')
print(f'content : {last.content}')
print(f'journalist : {last.journalist}')

