from django.urls import path
from . import views
app_name = 'complaints'

urlpatterns = [
	path('', views.exploreComplaints, name='explore-complaints'),
	path('request-history/<str:user_id>/', views.complaintStatus, name='request-history'),
	path('create-complaint/<str:user_id>/', views.createComplaint, name='create-complaint'),
]