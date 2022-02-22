from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Complaint)
admin.site.register(Complaint_Document)
admin.site.register(Message)
admin.site.register(Investigation)