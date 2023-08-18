from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    create_date = models.DateTimeField()

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField(upload_to='files/', blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    create_date = models.DateTimeField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(default="답변 대기", max_length=10 )

class File(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='attached_files')
    file = models.FileField(upload_to='files/', blank=True, null=True)

class Answer(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField()
    file = models.FileField(upload_to='files/', blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)