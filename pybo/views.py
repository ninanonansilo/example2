from django.shortcuts import render, get_object_or_404, redirect
from .forms import QuestionForm, AnswerForm

# Create your views here.
from django.http import HttpResponse

from .models import Question
from django.utils import timezone

def video(request):
    return render(request, 'pybo/video.html')

def index(request):

  ## config.urls -> pybo.urls ->  path ' ' 를 통해서 ##
    question_list = Question.objects.order_by('-create_date')
  ## question_list = 템플릿
    context = {'question_list': question_list}

  ##화면에 출력할 수 있는 render 함수##
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    # request = 사용자가 전달한 데이터를 확인할 때 사용
    question = get_object_or_404(Question, pk = question_id)
    context = {'question':question}
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # 등록 후에 다시 question_detail.html로 가야지 정상적임
    return redirect('pybo:detail', question_id=question.id)

def question_create(request):
    """
    pybo 질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)

def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
# ---------------------------------- [edit] ---------------------------------- #
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)