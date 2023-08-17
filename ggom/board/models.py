from django.db import models

# Create your models here.
class UserForm(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    create_date = models.DateTimeField()

class QuestionForm(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField(upload_to='files/', blank=True, null=True)
    create_date = models.DateTimeField()
    author = models.ForeignKey(UserForm, on_delete=models.CASCADE)
    status = models.CharField(max_length=10)

class FileForm(models.Model):
    question = models.ForeignKey(QuestionForm, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/', blank=True, null=True)

class AnswerForm(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(UserForm, on_delete=models.CASCADE)
    question = models.ForeignKey(QuestionForm, on_delete=models.CASCADE)


class CommentForm(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(UserForm, on_delete=models.CASCADE)
    question = models.ForeignKey(QuestionForm, on_delete=models.CASCADE)