from django.db import models

# Create your models here.
from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200) #CharField : 글자 수 제한
    content = models.TextField() #글자수 제한 없음
    create_date = models.DateTimeField() #날짜, 시간 관련 속성 = DateTimeField


    #데이터 조회 시 id가 아닌 제목을  표시
    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # ForeignKey = 다른 클래스(모델)과의 연결
    # Class Question을 속성으로 가짐
    # on_delete=models.CASCADE는 답변에 연결된 질문이 삭제되면 답변도 함께 삭제하라는 의미
    content = models.TextField()
    create_date = models.DateTimeField()
    def __str__(self):
        return self.question


