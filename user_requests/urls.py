from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'user_requests'

urlpatterns = [
	path('verify-user/<str:profile_id>/', views.verifyUser,name = 'verify-user'),
	path('report-user/<str:profile_id>/', views.reportUser,name = 'report-user'),
	path('request-contact-info/<str:profile_id>/', views.requestContactInfo,name = 'request-contact-info'),
	path('request-complaint/<str:profile_id>/<str:complaint_id>/', views.requestComplaint,name = 'request-complaint'),
	path('show-contact-requests/', views.showContactRequests, name = 'show-contact-requests'),
	path('show-complaint-requests/', views.showComplaintRequests, name = 'show-complaint-requests'),
	path('contact-request-action/<str:request_id>/<int:action>/', views.requestContactInfoAction, name = 'request-contact-info-action'),
	path('complaint-request-action/<str:profile_id>/', views.requestComplaintAction, name = 'request-complaint-action'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,
	document_root = settings.MEDIA_ROOT)