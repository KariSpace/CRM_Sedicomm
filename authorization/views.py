from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView, CreateView, DeleteView

from django.db.models import F, Sum
from django.db.models import Q
from django.db.models import Count

from datetime import datetime, date, timedelta

from django.utils import timezone

from .forms import UserUpdateForm, ItemInfoUpdateForm, ItemPaymentsUpdateForm, ItemGroupsUpdateForm, GroupCreateForm, DailyCreateForm

from .models import Daily, Group, People, get_daily_payments

from .forms import DateForm

@login_required
def staff(request):

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
        # username form
        n_form = UserUpdateForm(instance=request.user)

        # list of group tables
        list_items = Daily.objects.order_by('callback_time', 'email', 'course')

        # values = set(Daily.objects.values_list('course', flat=True))
        

        # items info
        table_status = False
        for item in list_items:
            if item.is_not_called():
                table_status = True

        # items payments
        list_payments = People.objects.filter(add_date__contains = date.today()).order_by('request_status')
        # payment_status = False
        # for item in list_items:
        #     if item.is_called():
        #         payment_status = True
        

        # creating all data list
        context = {
        "n_form":n_form,
        "list_items":list_items,
        #"table_date":table_date,
        "table_status":table_status,
        "list_payments":list_payments,
        # "payment_status":payment_status,

        }
        # dispaly page
        return render(request,"staff.html",context)



@login_required
def groups(request):

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
        # username form
        n_form = UserUpdateForm(instance=request.user)

        li = set(Group.objects.all())



        # creating all data list
        context = {
        "n_form":n_form,
        "li":li,
        }
        # dispaly page
        return render(request,"groups.html",context)


@login_required
def groups_payments(request):

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
        # username form
        n_form = UserUpdateForm(instance=request.user)

        list_payments = People.objects.order_by('request_status','group', 'obligation', )
        
        
        # #########################################################################################################
        money_all = list_payments.filter(Q(request_status='оплачено') | 
                                            Q(request_status='оплачено частично') | 
                                            Q(request_status='ожидаем оплату')).aggregate(money_all=Sum(F('course_price')))

        money_all_num = money_all['money_all']
        print(money_all_num, "все деньги")

        money_paid = list_payments.filter(Q(request_status='оплачено') | 
                                                Q(request_status='оплачено частично') | 
                                                Q(request_status='ожидаем оплату')).aggregate(money_paid=Sum(F('total_payment')))

        money_paid_num = money_paid['money_paid']

        print(money_paid_num, "Заплатили")

        if money_all_num == None:
            money_all_num = 0

        if  money_paid_num == None:
                money_paid_num = 0

        money_will_num =  money_all_num - money_paid_num
        print(money_will_num ,"Заплатят")


        people_done = list_payments.filter(Q(request_status='оплачено')).count()
        people_partially = list_payments.filter(Q(request_status='оплачено частично')).count()

        people_waiting = list_payments.filter(Q(request_status='ожидаем оплату')).count()

        people_all_num =  people_done + people_partially + people_waiting

        print(people_done)
        print(people_partially)
        print(people_waiting)

        

        # creating all data list
        context = {
        "n_form":n_form,
        "list_payments":list_payments,

        ##################################################


        "money_all_num" : money_all_num,
        "money_paid_num" : money_paid_num,
        "money_will_num":money_will_num,

        "people_done" : people_done,
        "people_partially" : people_partially,
        "people_waiting" : people_waiting,
        "people_all_num" : people_all_num,

      

       
        }
        # dispaly page
        return render(request,"groups_payments.html",context)


def pay_filter(request, pk):
    list_payments = People.objects.order_by('request_status','group', 'obligation', )
    formcheck = 1

    submitbutton= request.POST.get("submit")

    start_date = date.today()
    end_date = 0

    form = DateForm(request.POST or None)

    if form.is_valid():
            start_date = form.cleaned_data.get("start_date")
            end_date = form.cleaned_data.get("end_date")


    if start_date == None:
        start_date = datetime.now() - timedelta(minutes=60*24*12000)

    if  end_date == None:
            end_date = datetime.now()
    
    if submitbutton:
        print("submit")
        # #MONEY
        list_payments = list_payments.filter(Q(add_date__gte = start_date) &  Q(add_date__lte= end_date) )


    if pk == 1:  #today
        now = datetime.today() - timedelta(minutes=60)
        print(now)
        list_payments = list_payments.filter(Q(add_date__gte = now))
        print(list_payments)
    elif pk == 2:  #7 days
        now = datetime.today() - timedelta(minutes=60*24*7)
        list_payments = list_payments.filter(Q(add_date__gte = now))
    elif pk == 3:  # 30 days
        now = datetime.today() - timedelta(minutes=60*24*30)
        list_payments = list_payments.filter(Q(add_date__gte = now))
    elif pk == 5:
        formcheck = 2
    elif pk == 6:
        formcheck = 1



    # #MONEY
    money_all = list_payments.filter(Q(request_status='оплачено') | 
                                            Q(request_status='оплачено частично') | 
                                            Q(request_status='ожидаем оплату')).aggregate(money_all=Sum(F('course_price')))

    money_all_num = money_all['money_all']
    print(money_all_num, "все деньги")

    money_paid = list_payments.filter(Q(request_status='оплачено') | 
                                            Q(request_status='оплачено частично') | 
                                            Q(request_status='ожидаем оплату')).aggregate(money_paid=Sum(F('total_payment')))

    money_paid_num = money_paid['money_paid']

    print(money_paid_num, "Заплатили")

    if money_all_num == None:
        money_all_num = 0

    if  money_paid_num == None:
            money_paid_num = 0

    money_will_num =  money_all_num - money_paid_num
    print(money_will_num ,"Заплатят")


    people_done = list_payments.filter(Q(request_status='оплачено')).count()
    people_partially = list_payments.filter(Q(request_status='оплачено частично')).count()

    people_waiting = list_payments.filter(Q(request_status='ожидаем оплату')).count()

    people_all_num =  people_done + people_partially + people_waiting

    print(people_done)
    print(people_partially)
    print(people_waiting)
    
    context = {
        "list_payments":list_payments,

        'formcheck': formcheck,

        "money_all_num" : money_all_num,
        "money_paid_num" : money_paid_num,
        "money_will_num" : money_will_num,

        "people_done" : people_done,
        "people_partially" : people_partially,
        "people_waiting" : people_waiting,
        "people_all_num" : people_all_num,

        'form': form,
        'start_date': start_date, 
        'end_date':end_date, 
    }

    return render(request,"groups_payments.html",context)





class ItemInfoUpdate(LoginRequiredMixin, UpdateView):
    model = Daily
    template_name = 'info_update.html'
    form_class = ItemInfoUpdateForm
    success_url='/ok/'

    def form_valid(self, form):
        cleaned = form.save(commit=False)
        comments = Daily.objects.get(id = cleaned.id).comments
        if(cleaned.comments != comments):
            cleaned.comments=form.cleaned_data['comments']+'\n'+str(datetime.now().strftime('%d/%m/%Y %H:%M'))+'\n'
        if form.cleaned_data['group']:
                print('mooved to groups')

                if (cleaned.request_status == "оплачено частично"):
                    first_payment_date = datetime.now()
                    full_payment_date = None
                elif(cleaned.request_status == "оплачено"):
                    first_payment_date = full_payment_date = datetime.now()
                else:
                    first_payment_date = full_payment_date = None

                People.objects.update_or_create(
                name            = cleaned.name,
                phone           = cleaned.phone,
                email           = cleaned.email,
                course          = form.cleaned_data['course'],
                country         = cleaned.country,
                university      = cleaned.university,
                work            = cleaned.work,
                where_from      = cleaned.where_from,
                currency        = cleaned.currency,
                course_price    = cleaned.course_price,
                comments        = cleaned.comments,
                wishes          = cleaned.wishes,
                group           = form.cleaned_data['group'],
                request_status        = cleaned.request_status,
                payment_history        = cleaned.payment_history,
                total_payment        = cleaned.total_payment,
                # payment_source        = cleaned.payment_source,
                obligation        = cleaned.obligation,
                add_date      = datetime.now(),
                first_payment_date = first_payment_date,
                full_payment_date = full_payment_date,
                need_confirm = form.cleaned_data['need_confirm']
                )
                cleaned.request_status = "перемещен в группы"
                # for i in for_del:
                #     i.request_status = "перемещен в группы"
                #     i.save()
                objects = People.objects.filter(name = cleaned.name,phone= cleaned.phone,email= cleaned.email,)
                for obj in objects:
                    obj.comments = obj.comments + cleaned.comments
                    obj.wishes = obj.wishes + cleaned.wishes
                    obj.save()
                # for gr in form.cleaned_data['group']:
                # obj.group.add(form.cleaned_data['group'])
        return super().form_valid(form)



class GroupPaymentsUpdate(LoginRequiredMixin, UpdateView):
    model = People
    template_name = 'info_update.html'
    form_class = ItemPaymentsUpdateForm
    success_url='/ok/'


    def form_valid(self, form):
        cleaned = form.save(commit=False)
        comments = People.objects.get(id = cleaned.id).comments
        old_total_payment = People.objects.get(id = cleaned.id).total_payment
        # toHex = lambda x:"".join([hex(ord(c))[2:].zfill(2) for c in x])
        # print()
        # print('"'+cleaned.comments+'"')
        # print()
        # print('"'+comments+'"')
        # print()
        # print(toHex(cleaned.comments))
        # print()
        # print(toHex(comments))
        # print()
        # print(cleaned.comments == comments)
        # print()
        if(cleaned.comments != comments):
            cleaned.comments=form.cleaned_data['comments']+'->'+datetime.now().strftime('%d/%m/%Y %H:%M')

        if (cleaned.total_payment > old_total_payment):
            cleaned.first_payment_date = datetime.now()
            if(cleaned.total_payment == cleaned.course_price):
                cleaned.full_payment_date = datetime.now()
                cleaned.request_status = "оплачено"
            else:
                cleaned.request_status = "оплачено частично"

        objects = People.objects.filter(name = cleaned.name,phone= cleaned.phone,email= cleaned.email,)
        for obj in objects:
            obj.comments = cleaned.comments
            obj.wishes = cleaned.wishes
            obj.save()

        return super().form_valid(form)


class ItemGroupsUpdate(LoginRequiredMixin, UpdateView):
    model = People
    template_name = 'info_update.html'
    form_class = ItemGroupsUpdateForm
    success_url='/ok/'


    def form_valid(self, form):
        cleaned = form.save(commit=False)
        comments = People.objects.get(id = cleaned.id).comments
        old_total_payment = People.objects.get(id = cleaned.id).total_payment

        if(cleaned.comments != comments):
            cleaned.comments=form.cleaned_data['comments']+'\n'+str(datetime.now().strftime('%d/%m/%Y %H:%M'))+'\n'

        if (cleaned.total_payment > old_total_payment):
            cleaned.first_payment_date = datetime.now()
            if(cleaned.total_payment == cleaned.course_price):
                cleaned.full_payment_date = datetime.now()
                cleaned.request_status = "оплачено"
            else:
                cleaned.request_status = "оплачено частично"
        objects = People.objects.filter(name = cleaned.name,phone= cleaned.phone,email= cleaned.email,)
        for obj in objects:
            obj.comments = cleaned.comments
            obj.wishes = cleaned.wishes
            obj.save()        
        return super().form_valid(form)



class CreateNewDaily(LoginRequiredMixin, CreateView):
    model = Daily
    template_name = 'group_create.html'
    success_url='/ok/'
    form_class = DailyCreateForm
    

    # ide = People.objects.get(email = 'guigiug@mail')
    # print(ide.id)

    def form_valid(self, form):
        cleaned = form.save(commit=False)
        cleaned.request_date=str(datetime.now())
        return super().form_valid(form)





class CreateNewGroup(LoginRequiredMixin, CreateView):
    model = Group
    template_name = 'group_create.html'
    success_url='/ok/'
    form_class = GroupCreateForm

    def form_valid(self, form):
        cleaned = form.save(commit=False)
        cleaned.created_date=str(datetime.now())
        return super().form_valid(form)



class DeletePeople(LoginRequiredMixin, DeleteView):
    model = People

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        client = self.kwargs['pk']
        client = People.objects.get(id = client)
        client.dell()
        return HttpResponseRedirect('/groups_payments/')

class DeleteGroups(LoginRequiredMixin, DeleteView):
    model = People

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        client = self.kwargs['pk']
        client = People.objects.get(id = client)
        client.dell()
        return HttpResponseRedirect('/groups/')

class DeleteGroup(LoginRequiredMixin, DeleteView):
    model = Group

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        client = self.kwargs['pk']
        client = Group.objects.get(id = client)
        client.dell()
        return HttpResponseRedirect('/groups/')


@login_required
def start(request):
    return redirect('staff')


@login_required
def OkView(request):
    return render(request,"ok.html")

def login(request):
    return render(request, 'login.html')


@login_required
def ChangePassword(request):
    if request.method == 'POST':
        u_form = PasswordChangeForm(data=request.POST, user=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Data has been updated!')
            return redirect('staff')
    else:
        u_form = PasswordChangeForm(user=request.user)
        context = {
        "u_form":u_form,
        }
        return render(request,"pass_change.html",context)