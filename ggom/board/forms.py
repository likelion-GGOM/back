from django import forms
from .models import Question, Comment, Answer, QuestionImage
from django.forms import modelformset_factory


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content', 'status']



class ImageForm(forms.ModelForm):
    class Meta:
        model = QuestionImage
        fields = ('image',)
        
ImageFormSet = modelformset_factory(QuestionImage, form=ImageForm, extra=10) # 10개의 이미지 필드

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content', 'question']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['title','content', 'file', 'image', 'question']