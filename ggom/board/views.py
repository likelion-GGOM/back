from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import QuestionForm, AnswerForm, CommentForm
from django.views.decorators.csrf import csrf_protect


# 질문 작성 페이지와 질문 작성 처리
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES) # POST 데이터와 파일을 함께 처리
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.create_date = timezone.now()
            new_question.save()
            return render(request, 'question_create.html') # 작성 성공시 표시될 페이지
    else:
        form = QuestionForm() 
    return render(request, 'question_new.html', {'form': form}) # 작성 폼 페이지

# 질문 상세 보기
def question_detail(request, question_id):
    question = get_object_or_404(QuestionForm, pk=question_id)
    return render(request, 'board/question_detail.html', {'question': question})


# 질문에 답변 작성
def answer_create(request, question_id):
    if request.method == 'POST':
        form = AnswerForm(request.POST, request.FILES) # POST 데이터와 파일을 함께 처리
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = get_object_or_404(QuestionForm, pk=question_id)
            answer.author = request.user
            answer.save()
            return redirect('question_detail', question_id=question_id) # 답변 작성 후 질문 상세 페이지로 이동
    else:
        form = AnswerForm()
    return render(request, 'question_detail.html', {'form': form})




# 질문 수정
def question_edit(request, question_id):
    question = get_object_or_404(QuestionForm, pk=question_id)
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