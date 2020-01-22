from django.db import models


# Create your models here.
class People(models.Model):
    date            = models.DateField(auto_now_add=True)
    name            = models.CharField(max_length=100, blank=True)
    phone           = models.CharField(max_length=100, blank=True)
    email           = models.CharField(max_length=100, blank=True)
    course          = models.CharField(max_length=20, blank=True)
    country         = models.CharField(max_length=50, blank=True)
    university      = models.CharField(max_length=50, blank=True)
    work            = models.CharField(max_length=50, blank=True)
    where_from      = models.CharField(max_length=50, blank=True)

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
    obligation = models.CharField(max_length=100, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['date',]),
        ]

    def __str__(self):
        return self.name






#https://pypi.org/project/django-phone-field/