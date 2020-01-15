from django import forms
from django.contrib.auth.models import User
from .models import Daily



class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username',]
    
class DailyUpdateForm(forms.ModelForm):

    class Meta:
        model = Daily
        fields = [
                'name',
                'phone',
                'email',
                'course',
                'country',
                'comments',
                'currency',
                'course_price',
                'request_status',
                'callback_time',
                'group',
                'wishes',]

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