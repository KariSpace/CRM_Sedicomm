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

    callback_time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], required=False)
    request_status = forms.CharField(widget=forms.Select(choices=STATUS_CHOICES))
    group = forms.ModelMultipleChoiceField(required=False,queryset = Group.objects.all(), widget=forms.CheckboxSelectMultiple)

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

    # STATUS_CHOICES = [
    #     ('оплачено частично', 'оплачено частично'),
    #     ('оплачено', 'оплачено'),
    # ]

    '''group = forms.ModelChoiceField(
                    required=False,
                    queryset = Group.objects.all(),
                    widget=forms.Select())'''

    callback_time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], required=False)
    # request_status = forms.CharField(widget=forms.Select(choices=STATUS_CHOICES))
    group = forms.ModelMultipleChoiceField(required=False,queryset = Group.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Daily
        fields = [
                
                'total_payment',
                'course_price',
                'obligation',
                'currency',
                'course',
                'group',
                'payment_history',
                'callback_time',]    

class ItemGroupsUpdateForm(forms.ModelForm):

    '''group = forms.ModelChoiceField(
                    required=False,
                    queryset = Group.objects.all(),
                    widget=forms.Select())'''

    callback_time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], required=False)
    # request_status = forms.CharField(widget=forms.Select(choices=STATUS_CHOICES))
    group = forms.ModelMultipleChoiceField(required=False,queryset = Group.objects.all(), widget=forms.CheckboxSelectMultiple)



    class Meta:
        model = Daily
        fields = [
                
                'total_payment',
                'course_price',
                'obligation',
                'currency',
                'course',
                'group',
                'payment_history',
                'callback_time',]                   

class GroupCreateForm(forms.ModelForm):

    time_start = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], required=False)
    time_end = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], required=False)

    class Meta:
        model = Group
        fields = ['name', 'time_start', 'time_end']


class DailyCreateForm(forms.ModelForm):

    

    class Meta:
        model = Daily
        fields = ['name', 'phone', 'email', 'course', 'country', 'university', 'work', 'where_from', 'currency', 'course_price']




