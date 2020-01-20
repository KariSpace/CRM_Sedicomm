from django.db import models


class Daily(models.Model):
    # from csv
    request_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    course = models.CharField(max_length=100, blank=True)
    country  = models.CharField(max_length=100, blank=True)
    university = models.CharField(max_length=100, blank=True)
    work = models.CharField(max_length=100, blank=True)
    where_from = models.CharField(max_length=100, blank=True)

    # from cvs auto
    currency = models.CharField(max_length=100, blank=True)
    course_price = models.IntegerField(blank=True, null=True)

    # from call form
    comments = models.TextField(blank=True)
    wishes = models.TextField(blank=True)
    callback_time = models.DateTimeField(blank=True, null=True)
    group = models.CharField(max_length=100, blank=True)
    request_status = models.CharField(max_length=100, blank=True)

    # from payment form
    payment_history = models.TextField(blank=True)
    total_payment = models.IntegerField(blank=True, null=True)
    payment_source = models.CharField(max_length=100, blank=True)
    obligation = models.IntegerField(blank=True, null=True)
    
    

    def __str__(self):
        return self.name
    
    def is_not_called(self):
        if self.request_status != 'оплачено частично' and self.request_status != 'ожидаем оплату' and self.request_status != 'отказ' and self.request_status != 'оплачено':
            return True
        else:
            return False
    
    def call_status(self):
        if self.request_status != 'перезвонить':
            return False
        else :
            return True

    def is_called(self):
        if self.request_status == 'оплачено частично' or self.request_status == 'ожидаем оплату' or self.request_status == 'оплачено':
            return True
        else:
            return False
