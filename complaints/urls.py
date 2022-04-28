from django.urls import path
from . import views
app_name = 'complaints'

urlpatterns = [
	path('', views.exploreComplaints, name='explore-complaints'),
	path('request-history/', views.requestHistory, name = 'request-history'),
	path('find-nearest-helpers/', views.findNearestActivist, name='complaint-request-nearest-activist'),
	path('complaint-file-drop/', views.complaint_drop_zone_file, name = 'complaint-file-drop-zone-view'),
	path('complaint-file-drop/upload/', views.complaint_file_upload_view, name = 'complaint-file-drop-upload-upload-view'),
	path('investigate/<str:complaint_id>/', views.investigateComplaint, name='investigate-complaint'),
	path('mark-as-done/<str:complaint_id>/', views.markComplaintAsDone, name='mark-as-done'),
	path('create-complaint/', views.createComplaint, name='create-complaint'),
	path('delete_complaint/<str:complaint_id>/', views.deleteComplaint, name='delete-complaint'),
	path('<str:complaint_id>/', views.showComplaintDetail, name='show-complaint-detail'),
	path('<str:complaint_id>/<str:message_type>/', views.addMessage, name='update-complaint'),
	path('<str:complaint_id>/vote_change/upvote/', views.complaintUpvote, name='upvote-complaint'),
	path('<str:complaint_id>/vote_change/downvote/', views.complaintDownvote, name='downvote-complaint'),
	path('<str:complaint_id>/<str:message_type>/', views.addMessage, name='update-complaint'),
]
