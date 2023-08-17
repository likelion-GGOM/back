from django import forms
from .models import Question, Comment 

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content', 'image', 'author', 'status']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'author', 'question']