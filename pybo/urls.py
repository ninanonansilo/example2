from django.urls import path
from .import views

app_name = 'pybo'
urlpatterns = [
    path('', views.index, name = 'index'), #/pybo/는 index라는 URL 별칭

    ## id = 2인 거 조회 할때는 밑에 url 매핑
    path('<int:question_id>/' , views.detail, name = 'detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    ## 질문 만들기 버튼에 대한 URL
    path('question/create/', views.question_create, name='question_create'),
    path('video/', views.video, name='video'),


]