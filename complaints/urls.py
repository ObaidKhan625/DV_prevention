from django.urls import path
from . import views
app_name = 'complaints'

urlpatterns = [
	path('', views.exploreComplaints, name='explore-complaints'),
	path('?sort_by=<str:sorting_parameter>/', views.exploreComplaints, name='explore-complaints-by-parameter'),
	path('investigate/<str:complaint_id>/', views.investigateComplaint, name='investigate-complaint'),
	path('request-history/<str:user_id>/', views.complaintStatus, name='request-history'),
	path('create-complaint/', views.createComplaint, name='create-complaint'),
	path('<str:complaint_id>/', views.showComplaintDetail, name='show-complaint-detail'),
	path('<str:complaint_id>/<str:message_type>/', views.addMessage, name='update-complaint'),
	path('<str:complaint_id>/vote_change/upvote/', views.complaintUpvote, name='upvote-complaint'),
	path('<str:complaint_id>/vote_change/downvote/', views.complaintDownvote, name='downvote-complaint'),
	path('<str:complaint_id>/<str:message_type>/', views.addMessage, name='update-complaint'),
]
