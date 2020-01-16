from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ItemInfoUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from .models import Daily
from django.views.generic import UpdateView
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
        list_items = Daily.objects.order_by('callback_time')
        table_date = Daily.objects.get(id = 1)
        table_date = table_date.request_date.strftime("%d/%m")

        n_form = UserUpdateForm(instance=request.user)
        
        context = {
        "n_form":n_form,
        "list_items":list_items,
        "table_date":table_date,
        }
        return render(request,"staff.html",context)

class ItemInfoUpdate(LoginRequiredMixin, UpdateView):
    model = Daily
    template_name = 'info_update.html'
    form_class = ItemInfoUpdateForm
    success_url='/ok/'
    def form_valid(self, form):
        cleaned = form.save(commit=False)
        cleaned.comments=form.cleaned_data['comments']+'\n'+str(datetime.now().strftime('%d/%m/%Y %H:%M'))
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