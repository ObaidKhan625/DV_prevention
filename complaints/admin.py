from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Complaint)
admin.site.register(Complaint_Document)
admin.site.register(Message)
admin.site.register(Investigation)
admin.site.register(TagComplaint)

from django.contrib.sessions.models import Session
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
admin.site.register(Session, SessionAdmin)