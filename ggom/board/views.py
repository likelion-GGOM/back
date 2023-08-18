from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Question, Answer, Comment, QuestionImage
from .forms import QuestionForm, AnswerForm, CommentForm
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from django.contrib.auth import get_user_model
from .models import Question, QuestionImage


# 질문 작성 페이지와 질문 작성 처리
@login_required()
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.author = request.user
            new_question.save()
            for image_file in request.FILES.getlist('images'):
                QuestionImage.objects.create(question=new_question, image=image_file)
            return redirect('board:question_list')
    else:
        form = QuestionForm()
    return render(request, 'question_new.html', {'form': form})



# 질문 상세 보기
def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    is_author = request.user == question.author # 현재 로그인된 사용자와 글의 작성자 비교
    answer = Answer.objects.filter(question=question_id)
    return render(request, 'question_detail.html', {'question': question})


# 질문에 답변 작성
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST, request.FILES) # POST 데이터와 파일을 함께 처리
        if form.is_valid():
            answer = form.save(commit=False)
            answer.title = request.POST['title']
            answer.create_date = timezone.now()
            answer.question = get_object_or_404(Question, pk=question_id)
            answer.author = request.user
            answer.save()
            print("답변 작성 완료")
            return redirect('board:question_detail', question_id=question_id) # 답변 작성 후 질문 상세 페이지로 이동
    else:
        form = AnswerForm()
    return render(request, 'question_detail.html', {'form': form})


# 질문 게시판 목록
def question_list(request):
    if request.method == 'GET':
        question = Question.objects.all()
    return render(request, 'question_list.html', {'question': question})


# 내 질문 목록
def my_question_list(request):
    if request.method == 'GET':
        question = Question.objects.filter(author=request.user)
    return render(request, 'my_question_list.html', {'question': question})

# 내 답변 목록
def my_answer_list(request):
    if request.method == 'GET':
        answer = Answer.objects.filter(author=request.user)
    return render(request, 'my_answer_list.html', {'answer': answer})


# 질문 수정
def question_edit(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('question_detail', question_id=question.id) # 수정 후 상세 페이지로 이동
    else:
        form = QuestionForm(instance=question)
    return render(request, 'question_edit.html', {'form': form})

# 질문 삭제
def question_delete(request, question_id):
    question = get_object_or_404(QuestionForm, pk=question_id)
    question.delete()
    return redirect('question_list')


# 답변에 댓글 작성
def answer_comment_create(request, question_id):
    question = get_object_or_404(QuestionForm, pk=question_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.create_date = timezone.now()
            comment.question = question
            comment.author = request.user # 현재 로그인된 user를 작성자로 지정
            comment.save()
            return redirect('question_detail', question_id=question.id)
    else:
        form = CommentForm()
    return render(request, 'question_detail.html', {'form': form})