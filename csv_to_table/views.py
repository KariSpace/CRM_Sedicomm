from django.shortcuts import render
import csv, io
from authorization.models import Daily
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
        messages.success(request, "Data was uploaded")

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for col in csv.reader(io_string, delimiter=';', quotechar='|'):
        _, created = Daily.objects.update_or_create(
            name            = col[0],
            phone           = col[1],
            email           = col[2],
            course          = col[3],
            country         = col[4],
            university      = col[5],
            work            = col[6],
            where_from      = col[7],
            currency        = choseMoney(col[4]),
            course_price    = choseCourse(choseMoney(col[4]), col[3]),
        )
    return render(request, template)

@login_required
def today_table(request):
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

    context = {
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

def choseCourse(currency, course):
    if currency == 'UAH':
        if course == "CCNA1":
            prise = 1500
        elif course == "CCNA2":
            prise = 1000
        elif course == "Linux":
            prise = 1400
        elif course == "ITN":
            prise = 3000
        else:
            prise = 0
    if currency == 'RUB':
        if course == "CCNA1":
            prise = 1500
        elif course == "CCNA2":
            prise = 1000
        elif course == "Linux":
            prise = 1400
        elif course == "ITN":
            prise = 3000
        else:
            prise = 0
    elif currency == 'USD':
        if course == "CCNA1":
            prise = 15
        elif course == "CCNA2":
            prise = 7
        elif course == "Linux":
            prise = 14
        elif course == "ITN":
            prise = 10
        else:
            prise = 0
    elif currency == 'KZT':
        if course == "CCNA1":
            prise = 5000
        elif course == "CCNA2":
            prise = 4000
        elif course == "Linux":
            prise = 3000
        elif course == "ITN":
            prise = 10000
        else:
            prise = 0
    else:
        prise = 0
    return(prise)

