from django.db import models


# Create your models here.
class People(models.Model):
    date            = models.DateField(auto_now=True)
    name            = models.CharField(max_length=100, blank=True)
    phone           = models.CharField(max_length=100, blank=True)
    email           = models.CharField(max_length=100, blank=True)
    course          = models.CharField(max_length=20, blank=True)
    country         = models.CharField(max_length=50, blank=True)
    university      = models.CharField(max_length=50, blank=True)
    work            = models.CharField(max_length=50, blank=True)
    where_from      = models.CharField(max_length=50, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['date',]),
        ]

    def __str__(self):
        return self.name






#https://pypi.org/project/django-phone-field/