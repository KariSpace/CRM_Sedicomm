from django import forms
from django.contrib.auth.models import User
from .models import Daily
from django.utils import timezone

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username',]
    
class ItemInfoUpdateForm(forms.ModelForm):

    STATUS_CHOICES = [
        ('ожидаем оплату', 'ожидаем оплату'),
        ('перезвонить', 'перезвонить'),
        ('отказ', 'отказ'),
    ]

    callback_time = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], required=False)
    request_status = forms.CharField(widget=forms.Select(choices=STATUS_CHOICES))

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







    '''request_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    course = models.CharField(max_length=100, blank=True)
    country  = models.CharField(max_length=100, blank=True)
    university = models.CharField(max_length=100, blank=True)
    work = models.CharField(max_length=100, blank=True)
    where_from = models.CharField(max_length=100, blank=True)
    comments = models.TextField(blank=True)
    currency = models.CharField(max_length=100, blank=True)
    course_price = models.IntegerField(blank=True, null=True)
    request_status = models.CharField(max_length=100, blank=True)
    callback_time = models.DateTimeField(blank=True, null=True)
    payment_history = models.TextField(blank=True)
    total_payment = models.IntegerField(blank=True, null=True)
    payment_source = models.CharField(max_length=100, blank=True)
    obligation = models.CharField(max_length=100, blank=True)
    group = models.CharField(max_length=100, blank=True)
    wishes = models.TextField(blank=True)'''