from django.contrib import admin
from .models import Contact


# Register your models here.
admin.site.register(Contact)
admin.site.register(Event)
admin.site.register(Attendance)

