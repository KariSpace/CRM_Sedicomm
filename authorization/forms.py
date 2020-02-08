from django import forms
from django.contrib.auth.models import User
from .models import Daily, Group, People



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
    # group = forms.ModelMultipleChoiceField(required=False,queryset = Group.objects.all(), widget=forms.CheckboxSelectMultiple)
    need_confirm = forms.BooleanField(widget=forms.CheckboxInput, required=False)

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
                "total_payment",
                
                'course_price',
                'group',
                'payment_history',
                
                'wishes',
                'comments',
                
                'request_status',
                'callback_time',
                'need_confirm',]
    
   
        
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
    # group = forms.ModelMultipleChoiceField(required=False,queryset = Group.objects.all(), widget=forms.CheckboxSelectMultiple)
    need_confirm = forms.BooleanField(widget=forms.CheckboxInput, required=False)

    class Meta:
        model = People
        fields = [
                'name',
                'phone',
                'email',
                'course',
                'group',
                'currency',
                'need_confirm',
                'total_payment',
                'course_price',
                'obligation',
                'payment_history',
                'comments',
                'callback_time',
                ]    
        # fields = '__all__'

class ItemGroupsUpdateForm(forms.ModelForm):

    '''group = forms.ModelChoiceField(
                    required=False,
                    queryset = Group.objects.all(),
                    widget=forms.Select())'''

    callback_time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], required=False)
    # request_status = forms.CharField(widget=forms.Select(choices=STATUS_CHOICES))
    # group = forms.ModelMultipleChoiceField(required=False,queryset = Group.objects.all(), widget=forms.CheckboxSelectMultiple)
    need_confirm = forms.BooleanField(widget=forms.CheckboxInput, required=False)



    class Meta:
        model = Daily
        fields = [
                
                'total_payment',
                'need_confirm',
                'course_price',
                'obligation',
                'currency',
                'course',
                'group',
                
                'payment_history',
                'comments',
                'callback_time',]                   

class GroupCreateForm(forms.ModelForm):

    time_start = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], required=False)
    time_end = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], required=False)

    class Meta:
        model = Group
        fields = ['name', 'course', 'time_start', 'time_end']


class DailyCreateForm(forms.ModelForm):

    

    class Meta:
        model = Daily
        fields = ['name', 'phone', 'email', 'course', 'country', 'university', 'work', 'where_from', 'currency', 'course_price']




