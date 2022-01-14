from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Verification)
admin.site.register(Report)
admin.site.register(Contact_Request)
admin.site.register(Contact_Permission)
admin.site.register(Complaint_Request)