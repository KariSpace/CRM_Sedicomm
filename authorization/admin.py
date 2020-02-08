from django.contrib import admin
from .models import Daily, People , Group, Course

# Register your models here.



@admin.register(Daily)
class DailyAdmin(admin.ModelAdmin):
   #date_hierarchy = 'date' #for sorting people by date into admin
   list_display = ("name", "phone", "email","request_status")

@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
   #date_hierarchy = 'date' #for sorting people by date into admin
   list_display = ("name", )

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
   #date_hierarchy = 'date' #for sorting people by date into admin
   list_display = ("name",)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
   #date_hierarchy = 'date' #for sorting people by date into admin
   list_display = ("name",)
