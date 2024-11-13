from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import *
# Register your models here.

admin.site.register(ServiceCatogarys)
admin.site.register(users)
admin.site.register(workers)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(ServiceRequests)
admin.site.register(Response)
admin.site.register(Feedback)
admin.site.register(Profile)
admin.site.register(LogEntry)