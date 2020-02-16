from django.shortcuts import render
import csv, io
from authorization.models import Daily, Course, People
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


    course_name = str(csv_file.name)[3:-4]

    type1 = "['Submitted', 'Your-Fname', 'Your-Sname', 'Tel-Contact', 'Email-Your', 'checkbox-Nationality', 'text-Speciality', 'text-Work', 'Client-From', 'Your-Message', 'agreement', 'Submitted From']"
    type2 = "['Submitted', 'your-name', 'sName', 'TelNumber', 'email-your', 'Courses', 'checkbox-Nationality', 'text-Speciality', 'client-from', 'your-message', 'agreement', 'Submitted Login', 'Submitted From']"
    type3 = "['Submitted', 'Your-Fname', 'Your-Sname', 'Tel-Contact', 'Email-Your', 'Your-Message', 'agreement', 'submit', 'Submitted From']"




    i=0
    for col in csv.reader(io_string, delimiter=';', quotechar='|'):
        if i == 0:
            if col:
              first_col = str(col)
              print(first_col)
              i += 1
        else:
            if first_col == type1:
                if col:
                    print("111111111111111g")
                    _, created = Daily.objects.update_or_create(
                        name            = str(col[1] +  " "+ col[2]),
                        phone           = col[3],
                        email           = col[4],
                        country         = col[5],
                        university      = col[6],
                        work            = col[7],
                        where_from      = col[8],
                        wishes          = col[9],
                        ip              = col[11],
                        course          = getCourse(course_name),
                        currency        = choseMoney(col[5]),
                        course_price    = getPrice(choseMoney(col[5]), getCourse(course_name))
                    )

            elif first_col == type2:
                 if col:
                    print("2222222222222222")
                    _, created = Daily.objects.update_or_create(
                        name            = str(col[1] +  " "+ col[2]),
                        phone           = col[3],
                        email           = col[4],
                        course          = getCourse(col[5]),
                        country         = col[6],
                        university      = col[7],
                        where_from      = col[8],
                        wishes          = col[9],
                        ip              = col[12],
                        currency        = choseMoney(col[6]),
                        course_price    = getPrice(choseMoney(col[6]), getCourse(course_name))
                    )
            elif first_col == type3:
                 if col:
                    print("3333333333333333333333")
                    _, created = Daily.objects.update_or_create(
                        name            = str(col[1] +  " "+ col[2]),
                        phone           = col[3],
                        email           = col[4],
                        wishes          = col[5],
                        ip              = col[8],
                        course          = getCourse(course_name),
                    )

    # next(io_string)


    
    # for col in csv.reader(io_string, delimiter=';', quotechar='|'):
    #     if col:
    #         print("esiogjiojrg")
    #         _, created = Daily.objects.update_or_create(
    #             name            = str(col[1] + col[2]),
    #             phone           = col[3],
    #             email           = col[4],
    #             country         = col[5],
    #             university      = col[6],
    #             work            = col[7],
    #             where_from      = col[8],
    #             comments        = col[9],
    #             ip              = col[11],
    #             course          = getCourse(course_name),
    #             currency        = choseMoney(col[5]),
    #             course_price    = getPrice(choseMoney(col[5]), getCourse(course_name))
    #         )
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
        
        print(today_wishes)
        print(today_comments)
        print(today_pay)




        # #MONEY
        # money_all = Daily.objects.all().aggregate(money_all=Sum(F('course_price')))
        # money_all_num = money_all['money_all']
        # print(money_all_num)

        # money_paid = Daily.objects.all().aggregate(money_paid=Sum(F('total_payment')))
        # money_paid_num = money_paid['money_paid']
        # print(money_paid_num)

        # money_will_pay = Daily.objects.all().aggregate(money_will_pay=Sum(F('obligation')))
        # money_will_pay_num = money_will_pay['money_will_pay']
        # money_will_num = money_all_num - money_paid_num
        # print(money_will_pay_num)
        # print(money_will_num)

        # people_done = Daily.objects.filter(request_status='оплачено').count()
        # people_partially = Daily.objects.filter(request_status='оплачено частично').count()
        # people_waiting = Daily.objects.filter(request_status='ожидаем оплату').count()
        # people_all_num = people_done + people_partially + people_waiting

        # print(people_done)
        # print(people_partially)
        # print(people_waiting)

        # currency = choseMoney("Ukraine")
        # course = getCourse("Linux")
        # price = getPrice(currency, course)
        # print(price)

    context = {
        "n_form":n_form,

        "today_wishes":today_wishes,
        "today_comments": today_comments,
        "today_pay" : today_pay,

        # "money_all_num" : money_all_num,
        # "money_paid_num" : money_paid_num,
        # "money_will_num":money_will_num,

        # "people_done" : people_done,
        # "people_partially" : people_partially,
        # "people_waiting" : people_waiting,
        # "people_all_num" : people_all_num,
        }
   
    return render(request, template, context)

@login_required
def search(request):
    template = "search.html"
    query = request.GET.get('q')
    search_people = People.objects.filter( 
                            Q(name__icontains = query) | 
                            Q(phone__icontains = query)|
                            Q(email__icontains = query)
                            ) 
    context = {
        "search_people":search_people,
        "s_text":query,
        }
   
    return render(request, template, context)

#CSV_TO_FILE COMMIT 

def choseMoney(country):
    if country == "Украины / Ukraine":
        currency = "UAH"
    elif country == "России / Russia":
        currency = "RUB"
    elif country == "Другое / Other Киргизия":
        currency = "KGS"
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
        c = Course.objects.create(
            name = course,
            price = {
                "UAH":0,
                "RUB":0,
                "USD":0,
            }
        )
        return c

def getPrice(currency, course):
    if course:
        return(course.get_price(currency))
    else:
        return 0

