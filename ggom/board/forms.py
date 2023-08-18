from django import forms
from .models import Question, Comment, Answer 

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['id', 'title', 'content', 'file', 'image', 'status']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'question']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['title','content', 'file', 'image', 'question']