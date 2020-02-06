from django.contrib import admin
from .models import Daily, People , Group

# Register your models here.



@admin.register(Daily)
class DailyAdmin(admin.ModelAdmin):
   #date_hierarchy = 'date' #for sorting people by date into admin
   list_display = ("name", "phone", "email")


admin.site.register(People)
admin.site.register(Group)