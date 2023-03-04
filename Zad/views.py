from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.core.paginator import Paginator

from .forms import RegisterUserForm, LoginUserForm
from .models import Task, TaskSet, TaskSetSet, Answer


def answer(request):
    request.session['total'] = None
    return render(request, 'answer.html')


def Question(request, task_pk):
    if request.method == 'POST':
        tasks = Task.objects.filter(set=task_pk)
        for q in tasks:
            if q.ans == request.POST.get(q.title):
                request.session["total"] += 1
        context = {
            'total': request.session["total"],
        }
        if request.POST.get('end'):
            if request.user.is_authenticated:
                Answer.objects.create(task=task_pk, score=request.session['total'],
                                  max_score=tasks.count(), answerer=request.user)
            request.session['total'] = 0
        return render(request, 'answer.html', context)
    else:
        tasks = Task.objects.filter(set=task_pk)
        paginator = Paginator(tasks, 1)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'tasks': page_obj,
            'page_obj': page_obj,
        }
        if not request.session['total']:
            request.session['total'] = 0
        return render(request, 'main.html', context)


class TaskList(ListView):
    context_object_name = 'TaskSet'
    template_name = 'taskset.html'

    def get_queryset(self, *args, **kwargs):
        self.request.session['total'] = 0
        return TaskSet.objects.filter(category=self.kwargs['list_num'])


class TaskListList(ListView):
    queryset = TaskSetSet.objects.filter()
    context_object_name = 'TaskSetSet'
    template_name = 'tasksetset.html'


class RegUser(CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')


class LogUser(LoginView):
    form_class = LoginUserForm
    template_name = 'svoy01/login.html'
    success_url = reverse_lazy('home')



