from django.contrib import admin

from .models import Category,Task,Taskusers,Appect_user

admin.site.register(Category)
admin.site.register(Task)
admin.site.register(Taskusers)
admin.site.register(Appect_user)
