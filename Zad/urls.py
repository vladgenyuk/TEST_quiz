from django.urls import path
from . import views


urlpatterns = [
    path('tasksetset/<int:task_pk>/', views.Question, name='tasklistlist'),
    path('taskset/<int:list_num>/', views.TaskList.as_view(), name='tasklist'),
    path('', views.TaskListList.as_view(), name='main'),
    path('answer/', views.answer, name='answer'),
    path('reg/', views.RegUser.as_view(), name='register'),
    path('login/', views.LogUser.as_view(), name='login'),
]
