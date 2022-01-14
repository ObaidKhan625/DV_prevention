from django.urls import path
from . import views
app_name = 'complaints'

urlpatterns = [
	path('', views.exploreComplaints, name='explore-complaints'),
	path('request-history/<str:user_id>/', views.complaintStatus, name='request-history'),
	path('create-complaint/', views.createComplaint, name='create-complaint'),
	path('<str:complaint_slug>/', views.showComplaintDetail, name='show-complaint-detail'),
	path('<str:complaint_id>/<str:message_type>', views.addMessage, name='update-complaint'),
]