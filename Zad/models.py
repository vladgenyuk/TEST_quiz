from django.contrib.auth.models import User
from django.db import models


class TaskSetSet(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class TaskSet(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(TaskSetSet, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=255)
    q1 = models.CharField(max_length=63)
    q2 = models.CharField(max_length=63)
    q3 = models.CharField(max_length=63)
    q4 = models.CharField(max_length=63)
    set = models.ForeignKey(TaskSet, on_delete=models.PROTECT)
    ans = models.CharField(max_length=63)

    def __str__(self):
        return f'{self.pk}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user.name


class Answer(models.Model):
    task = models.CharField(max_length=255)
    score = models.IntegerField()
    max_score = models.IntegerField()
    answerer = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
