from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm



from django.shortcuts import render
import csv, io
from authorization.models import Daily, Course
from datetime import date

from django.db.models import F, Sum
from django.db.models import Q
from django.db.models import Count
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import datetime


def todo(request):
    todo_list = Todo.objects.order_by('id')

    form = TodoForm()

    search_text = str(date.today().strftime('%d/%m/%Y')) 
    print("\n" ,type(search_text), search_text)
    today_wishes  = Daily.objects.filter( Q(wishes__contains = search_text))
    today_comments = Daily.objects.filter( Q(comments__contains = search_text))
    print(today_comments)
    today_pay  = Daily.objects.filter( Q(payment_history__contains = search_text))


    context = {'todo_list' : todo_list,
                'form' : form,
                "today_wishes":today_wishes,
                "today_comments": today_comments,
                "today_pay" : today_pay,

     }

    return render(request, 'todo/todo.html', context)

@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()

    return redirect('todo')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('todo')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('todo')

def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('todo')