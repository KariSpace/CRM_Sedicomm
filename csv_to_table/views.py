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

from authorization.forms import UserUpdateForm
# Create your views here.

#CSV_TO_FILE COMMIT 
@login_required
def csv_table(request):
    template = "csv_table.html"
    if request.method == "GET":
         return render(request,template)
    
    csv_file = request.FILES['csv_f']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This is not a CSV, try to upload .csv")
        return render(request,template)
    else:
        messages.success(request, " ")

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for col in csv.reader(io_string, delimiter=';', quotechar='|'):
        _, created = Daily.objects.update_or_create(
            name            = col[0],
            phone           = col[1],
            email           = col[2],
            course          = getCourse(col[3]),
            country         = col[4],
            university      = col[5],
            work            = col[6],
            where_from      = col[7],
            currency        = choseMoney(col[4]),
            course_price    = getPrice(choseMoney(col[4]), getCourse(col[3]))
        )
    return render(request, template)

@login_required
def today_table(request):
    if request.method == 'POST':
        n_form = UserUpdateForm(request.POST, instance=request.user)
        if n_form.is_valid():
            n_form.save()
            messages.success(request, f'Data has been updated!')
            return redirect('staff')
        else:
            messages.warning(request, f'Something wrong, maybe this name is allready taken')
            return redirect('staff')
    else:
        n_form = UserUpdateForm(instance=request.user)

        template = "today_table.html"

        search_text = str(date.today().strftime('%m/%d/%Y')) 
        print("\n" ,type(search_text), search_text)
        today_wishes  = Daily.objects.filter( Q(wishes__contains = search_text))
        today_comments = Daily.objects.filter( Q(comments__contains = search_text))
        today_pay  = Daily.objects.filter( Q(payment_history__contains = search_text))
        
        #print(today_wishes)
        #print(today_comments)
        #print(today_pay)

        #MONEY
        money_all = Daily.objects.all().aggregate(money_all=Sum(F('course_price')))
        money_all_num = money_all['money_all']
        #print(money_all_num)

        money_paid = Daily.objects.all().aggregate(money_paid=Sum(F('total_payment')))
        money_paid_num = money_paid['money_paid']
        #print(money_paid_num)

        money_will_pay = Daily.objects.all().aggregate(money_will_pay=Sum(F('obligation')))
        money_will_pay_num = money_will_pay['money_will_pay']
        money_will_num = money_all_num - money_paid_num
        #print(money_will_pay_num)
        #print(money_will_num)

        people_done = Daily.objects.filter(request_status='оплачено').count()
        people_partially = Daily.objects.filter(request_status='оплачено частично').count()
        people_waiting = Daily.objects.filter(request_status='ожидаем оплату').count()
        people_all_num = people_done + people_partially + people_waiting

        #print(people_done)
        #print(people_partially)
        #print(people_waiting)

        currency = choseMoney("Ukraine")
        course = getCourse("Linux")
        price = getPrice(currency, course)
        print(price)

    context = {
        "n_form":n_form,

        "today_wishes":today_wishes,
        "today_comments": today_comments,
        "today_pay" : today_pay,

        "money_all_num" : money_all_num,
        "money_paid_num" : money_paid_num,
        "money_will_num":money_will_num,

        "people_done" : people_done,
        "people_partially" : people_partially,
        "people_waiting" : people_waiting,
        "people_all_num" : people_all_num,
        }
   
    return render(request, template, context)

@login_required
def search(request):
    template = "search.html"
    query = request.GET.get('q')
    search_people = Daily.objects.filter( 
                            Q(name__icontains = query) | 
                            Q(phone__icontains = query)|
                            Q(email__icontains = query)
                            ) 
    context = {
        "search_people":search_people,
        }
   
    return render(request, template, context)

#CSV_TO_FILE COMMIT 
"""@login_required
def today_table(request):
    template = "today_table.html"
    today_people = Daily.objects.filter(wishes__contains = str(date.today()))
    #today_people = People.objects.filter(date=date.today())
    return render(request, template)
""" 

def choseMoney(country):
    if country == "Ukraine":
        currency = "UAH"
    elif country == "Russia":
        currency = "RUB"
    elif country == "Belarussia":
        currency = "BYN"
    elif country == "Kazakhstan":
        currency = "KZT"
    else:
        currency = "USD"
    return(currency)

def getCourse(course):
    c = Course.objects.filter(name = course)
    if c:
        for i in c:
            return i
    else:
        return None

def getPrice(currency, course):
    if course:
        return(course.get_price(currency))
    else:
        return 0

