from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ItemInfoUpdateForm, ItemPaymentsUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .models import Daily
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import datetime


import csv, io
from csv_to_table.models import People
from datetime import date



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

        # items info
        list_items = Daily.objects.order_by('callback_time')
        table_status = False
        for item in list_items:
            if item.is_not_called():
                table_status = True
        table_date = Daily.objects.get(id = 1)
        table_date = table_date.request_date.strftime("%d/%m")

        # items payments
        list_payments = Daily.objects.order_by('total_payment')
        payment_status = False
        for item in list_items:
            if item.is_called():
                payment_status = True

        
        # creating all data list
        context = {
        "n_form":n_form,
        "list_items":list_items,
        "table_date":table_date,
        "table_status":table_status,
        "list_payments":list_payments,
        "payment_status":payment_status,
        }
        # dispaly page
        return render(request,"staff.html",context)

class ItemInfoUpdate(LoginRequiredMixin, UpdateView):
    model = Daily
    template_name = 'info_update.html'
    form_class = ItemInfoUpdateForm
    success_url='/ok/'

    comments = model.comments
    def form_valid(self, form):
        cleaned = form.save(commit=False)
        cleaned.comments=form.cleaned_data['comments']+'\nsubmitted in '+str(datetime.now().strftime('%d/%m/%Y %H:%M'))
        return super().form_valid(form)

class ItemPaymentsUpdate(LoginRequiredMixin, UpdateView):
    model = Daily
    template_name = 'info_update.html'
    form_class = ItemPaymentsUpdateForm
    success_url='/ok/'

    comments = model.comments
    def form_valid(self, form):
        cleaned = form.save(commit=False)
        cleaned.comments=form.cleaned_data['comments']+'\nsubmitted in '+str(datetime.now().strftime('%d/%m/%Y %H:%M'))
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
        list_items = Daily.objects.order_by('callback_time')
        table_date = Daily.objects.get(id = 1)
        table_date = table_date.request_date.strftime("%d/%m")

        n_form = UserUpdateForm(instance=request.user)
        
        context = {
        "n_form":n_form,
        "list_items":list_items,
        "table_date":table_date,
        }
        return render(request,"groups.html",context)

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
        _, created = People.objects.update_or_create(
            name            = col[0],
            phone           = col[1],
            email           = col[2],
            course          = col[3],
            country         = col[4],
            university      = col[5],
            work            = col[6],
            where_from      = col[7],
        )
    return render(request, template)

#CSV_TO_FILE COMMIT 
@login_required
def today_table(request):
    template = "today_table.html"
    today_people = People.objects.filter(date=date.today())
    #today_people = People.objects.filter(date=date.today())
    return render(request, template, context={'today_people': today_people})



'''if request.method == 'POST':
        # u_form = UserUpdateForm(request.POST)
        if u_form.is_valid:
            # u_name = u_form.cleaned_data['username']
            # u_pass = u_form.cleaned_data['password']
            # # u = User.objects.get(username = request.user)
            # u = request.user
            # # submit = User(
            # #     username=u_name,
            # # )
            # # submit.save()
            # u.set_username(u_name)
            # u.set_password(u_pass)
            u_form.save
            messages.success(request, f'Data has been updated!')
            return redirect('staff')
    u_form = UserUpdateForm()
            # instance=request.user
    forms = {
        'u_form': u_form,
    }

    return render(request, 'staff.html', forms)'''