# class Math:
#     number = 3

#     def add(self):
#         pass

# a = Math()

# result = a.add()

# a = []
# b = list()

# a.append(1)

# class list:
#     def append(self, *args):
#         pass


from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Article 클래스의 인스턴스 생성
article = Article()

# article 인스턴스에 title과 content 인스턴스 변수에 값을 저장
article.title = '제목'
article.content = '내용'    # 사용자의 입력 값

# 테이블에 레코드 하나 생성을 위해 저장 (인스턴스 메서드 save 호출)
article.save()



# 생성 2번째 방법
article = Article(title='second', content='django!')
article.save()



# 3번째 방법(QuerySet API중에 create 메서드를 활용)
# 이 방법은 save가 내장되어 있는 기능이라 생성된 데이터가 바로 반환된다.
Article.objects.create(title='third', content='django!') 


