from django import forms
from django.contrib.auth.models import User
from .models import Daily, Group, People
from django.utils import timezone


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username',]
    
class ItemInfoUpdateForm(forms.ModelForm):

    STATUS_CHOICES = [
        ('ожидаем оплату', 'ожидаем оплату'),
        ('оплачено частично', 'оплачено частично'),
        ('оплачено', 'оплачено'),
        ('перезвонить', 'перезвонить'),
        ('отказ', 'отказ'),
    ]

    # values = set(Group.objects.values_list('name', flat=True))
    # values_list = []

    # for value in values:

    #     li = []
    #     li.append(value)
    #     li.append(value)

    #     values_list.append(li)

    # print(values)
    # print(values_list)

    # GROUP_CHOICES = values_list

    callback_time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], required=False)
    request_status = forms.CharField(widget=forms.Select(choices=STATUS_CHOICES))
    # group = forms.CharField(widget=forms.Select(choices=GROUP_CHOICES), required=False)
    group = forms.ModelChoiceField(
                    required=False,
                    queryset = Group.objects.all(),
                    widget=forms.Select())

    class Meta:
        model = Daily
        fields = [
                'request_date',
                'name',
                'phone',
                'email',
                'course',
                'country',
                'currency',
                'course_price',
                'group',
                'wishes',
                'comments',
                'request_status',
                'callback_time',]
    
    # def __init__(self):
    #     self.comments = self.cleaned_data['comments']+'\n'+str(timezone.now())
        
class ItemPaymentsUpdateForm(forms.ModelForm):

    STATUS_CHOICES = [
        ('оплачено частично', 'оплачено частично'),
        ('оплачено', 'оплачено'),
    ]

    callback_time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], required=False)
    request_status = forms.CharField(widget=forms.Select(choices=STATUS_CHOICES))

    class Meta:
        model = Daily
        fields = [
                
                'total_payment',
                'course_price',
                'obligation',
                'currency',
                'payment_source',
                'course',
                'payment_history',
                'callback_time',]    

class GroupCreateForm(forms.ModelForm):

    time_start = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], required=False)
    time_end = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], required=False)

    class Meta:
        model = Group
        fields = ['name', 'time_start', 'time_end']






