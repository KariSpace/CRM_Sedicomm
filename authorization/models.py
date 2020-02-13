from django.db import models
from datetime import datetime
from jsonfield import JSONField



class Course(models.Model):
    
    name     = models.CharField(max_length=100, blank=True)
    price    = JSONField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_related(self):
        return Group.objects.filter(course__pk=self.pk)

    def get_price(self, currency):
        price = self.price.get(currency)
        if price:
            return price
        return self.price.get("USD")

        


class Group(models.Model):
    
    name            = models.CharField(max_length=100, blank=True)
    created_date    = models.DateTimeField(blank=True, null=True)
    course          = models.ForeignKey(Course, on_delete=models.DO_NOTHING, null=True)
    active          = models.BooleanField(default=True)
    time_start      = models.DateTimeField(blank=True, null=True)
    time_end        = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.name

    def get_related(self):
        li = People.objects.filter(group = self)
        return li

    def is_active(self):
        return self.active

    def dell(self):
        self.active = False
        self.save()
        people = People.objects.filter(group = self)
        for person in people:
            person.request_status = "удален"
            person.save()



    

    
class Daily(models.Model):
    # from csv
    request_date    = models.DateTimeField(blank=True, null=True)
    name            = models.CharField(max_length=100, blank=True)
    phone           = models.CharField(max_length=100, blank=True)
    email           = models.CharField(max_length=100, blank=True)
    course          = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    country         = models.CharField(max_length=100, blank=True)
    university      = models.CharField(max_length=100, blank=True)
    work            = models.CharField(max_length=100, blank=True)
    where_from      = models.CharField(max_length=100, blank=True)

    # from cvs auto
    currency        = models.CharField(max_length=100, blank=True)
    course_price    = models.IntegerField(blank=True, null=True)

    # from call form
    comments        = models.TextField(blank=True)
    wishes          = models.TextField(blank=True)
    callback_time   = models.DateTimeField(blank=True, null=True)
    group           = models.ForeignKey(Group, on_delete=models.DO_NOTHING, null=True, blank=True)
    request_status  = models.CharField(max_length=100, blank=True)

    # from payment form
    need_confirm  = models.BooleanField(blank=True, null=True)
    payment_history = models.TextField(blank=True)
    total_payment   = models.IntegerField(blank=True, default=0)
    payment_source  = models.CharField(max_length=100, blank=True)
    obligation      = models.IntegerField(blank=True, null=True)
    
        

    def save(self, **kwargs):
        self.obligation = self.course_price - self.total_payment
        return super().save(**kwargs)
 

    def __str__(self):
        return self.name
    
    def is_not_called(self):
        if self.request_status != 'оплачено частично' and self.request_status != 'ожидаем оплату' and self.request_status != 'отказ' and self.request_status != 'оплачено' and self.request_status != 'перемещен в группы':
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
    
    def is_allready_in(self):
        obj = People.objects.filter(email = self.email)
        l = []
        if obj:
            for i in obj:
                l.append(i.group)
            return l
        else: 
            return False






class People(models.Model):
    # from csv
    add_date        = models.DateTimeField(blank=True, null=True)
    name            = models.CharField(max_length=100, blank=True)
    phone           = models.CharField(max_length=100, blank=True)
    email           = models.CharField(max_length=100, blank=True)
    course          = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    country         = models.CharField(max_length=100, blank=True)
    university      = models.CharField(max_length=100, blank=True)
    work            = models.CharField(max_length=100, blank=True)
    where_from      = models.CharField(max_length=100, blank=True)

    # from cvs auto
    currency        = models.CharField(max_length=100, blank=True)
    course_price    = models.IntegerField(blank=True, null=True)

    # from call form
    comments        = models.TextField(blank=True)
    wishes          = models.TextField(blank=True)
    callback_time   = models.DateTimeField(blank=True, null=True)
    group           = models.ForeignKey(Group, on_delete=models.DO_NOTHING, null=True, blank=True)
    # group           = JSONField(blank=True)
    request_status  = models.CharField(max_length=100, blank=True)

    # from payment form
    need_confirm  = models.BooleanField(blank=True, null=True)
    first_payment_date   = models.DateTimeField(blank=True, null=True)
    full_payment_date  = models.DateTimeField(blank=True, null=True)
    payment_history = models.TextField(blank=True)
    total_payment   = models.IntegerField(blank=True, null=True)
    obligation      = models.IntegerField(blank=True, null=True)

    def save(self, **kwargs):
        self.obligation = self.course_price - self.total_payment
        self.add_date = datetime.now()
        return super().save(**kwargs)

    def __str__(self):
        return self.name

    def is_called(self):
        if self.request_status == 'оплачено частично' or self.request_status == 'ожидаем оплату' or self.request_status == 'оплачено':
            return True
        else:
            return False

    def call_status(self):
        if self.request_status != 'перезвонить':
            return False
        else :
            return True

    def is_full_payed(self):
        return (self.request_status == 'оплачено')

    def is_particaly_payed(self):
        return (self.request_status == 'оплачено частично')

    def is_not_payed(self):
        return (self.request_status == 'ожидаем оплату')

    def is_need_confirm(self):
        return (self.need_confirm)
    
    def is_not_deleted(self):
        return (self.request_status != "удален")

    def dell(self):
        self.request_status = "удален"
        self.save()
        
    

def get_daily_payments():
    return People.objects.filter(add_date = datetime.now())
    