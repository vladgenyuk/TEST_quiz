from django.contrib import admin
from .models import Task, TaskSet, TaskSetSet, Answer, Profile

admin.site.register(Task)
admin.site.register(TaskSet)
admin.site.register(TaskSetSet)
admin.site.register(Answer)
admin.site.register(Profile)
