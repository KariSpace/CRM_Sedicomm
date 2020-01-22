from django.contrib import admin

from .models import People
# Register your models here.

@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
   date_hierarchy = 'date'

#admin.site.register(People)
