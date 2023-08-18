from django.db import models
from accounts.models import CustomUser



class Question(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField(upload_to='files/', blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default="답변 대기", max_length=10 )

    def __str__(self):
        return self.title

class QuestionImage(models.Model):
    question = models.ForeignKey(Question, related_name='question_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


class File(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='attached_files')
    file = models.FileField(upload_to='files/', blank=True, null=True)


class Answer(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_date = models.DateTimeField()
    file = models.FileField(upload_to='files/', blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)