from django.urls import path, include
from . import views
from complaints.views import exploreComplaints
app_name = 'user-auth'

urlpatterns = [
	path('', exploreComplaints),
	path('register/', views.registerPage, name='register'),
	path('login/', views.loginPage, name='login'),
	path('logout/', views.logoutUser, name='logout'),
]