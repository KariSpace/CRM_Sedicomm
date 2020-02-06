from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .models import Daily, Group, People
from django.views.generic import UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import datetime



@login_required
def start(request):
    return redirect('staff')









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
        list_items = Daily.objects.order_by('callback_time', 'course', 'name')

        # values = set(Daily.objects.values_list('course', flat=True))
        
        # li = []
        # for value in values:
        #     li.append(Daily.objects.filter(course = value))
        # print(li)
            
        # print(values)

        # items info
        table_status = False
        for item in list_items:
            if item.is_not_called():
                table_status = True
        #table_date = Daily.objects.get(id = 1)
        #table_date = table_date.request_date.strftime("%d/%m")

        # items payments
        list_payments = Daily.objects.order_by('course')
        payment_status = False
        for item in list_items:
            if item.is_called():
                payment_status = True
        
        # creating all data list
        context = {
        "n_form":n_form,
        "list_items":list_items,
        #"table_date":table_date,
        "table_status":table_status,
        "list_payments":list_payments,
        "payment_status":payment_status,
        }
        # dispaly page
        return render(request,"staff.html",context)






class CreateNewDaily(LoginRequiredMixin, CreateView):
    model = Daily
    template_name = 'group_create.html'
    success_url='/ok/'
    form_class = DailyCreateForm

    def form_valid(self, form):
        cleaned = form.save(commit=False)
        cleaned.request_date=str(datetime.now())
        return super().form_valid(form)









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
        if(cleaned.group != None):
            print('mooved to groups')
            People.objects.update_or_create(
            name            = cleaned.name,
            phone           = cleaned.phone,
            email           = cleaned.email,
            course          = cleaned.course,
            country         = cleaned.country,
            university      = cleaned.university,
            work            = cleaned.work,
            where_from      = cleaned.where_from,
            currency        = cleaned.currency,
            course_price    = cleaned.course_price,
            comments        = cleaned.comments,
            wishes          = cleaned.wishes,
            group           = cleaned.group,
            request_status        = cleaned.request_status,
            payment_history        = cleaned.payment_history,
            total_payment        = cleaned.total_payment,
            payment_source        = cleaned.payment_source,
            obligation        = cleaned.obligation,
            date_added        = str(datetime.now()),
        )
        else:
            cleaned.group=""
        return super().form_valid(form)








class ItemPaymentsUpdate(LoginRequiredMixin, UpdateView):
    model = Daily
    template_name = 'info_update.html'
    form_class = ItemPaymentsUpdateForm
    success_url='/ok/'

    def form_valid(self, form):
        cleaned = form.save(commit=False)
        if(cleaned.group != None):
            print('mooved to groups')
            People.objects.update_or_create(
            name            = cleaned.name,
            phone           = cleaned.phone,
            email           = cleaned.email,
            course          = cleaned.course,
            country         = cleaned.country,
            university      = cleaned.university,
            work            = cleaned.work,
            where_from      = cleaned.where_from,
            currency        = cleaned.currency,
            course_price    = cleaned.course_price,
            comments        = cleaned.comments,
            wishes          = cleaned.wishes,
            group           = cleaned.group,
            request_status        = cleaned.request_status,
            payment_history        = cleaned.payment_history,
            total_payment        = cleaned.total_payment,
            payment_source        = cleaned.payment_source,
            obligation        = cleaned.obligation,
            date_added        = str(datetime.now()),
        )
        else:
            cleaned.group=""
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

        # list of group tables
        # list_items = Group.objects.order_by('group')

        values = set(People.objects.values_list('group', flat=True))
        li = []
        for value in values:
            value = value.strip('"')
            li.append(People.objects.filter(group = value))
    

        # creating all data list
        context = {
        "n_form":n_form,
        "li":li,
        }
        # dispaly page
        return render(request,"groups.html",context)




class ItemGroupsUpdate(LoginRequiredMixin, UpdateView):
    model = People
    template_name = 'info_update.html'
    form_class = ItemGroupsUpdateForm
    success_url='/ok/'

    def form_valid(self, form):
        cleaned = form.save(commit=False)
        
        return super().form_valid(form)









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

