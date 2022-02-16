from django.urls import path, include
from . import views
app_name = 'user-auth'

urlpatterns = [
	path('', views.loginPage),
	path('register/', views.registerPage, name='register'),
	path('login/', views.loginPage, name='login'),
	path('logout/', views.logoutUser, name='logout'),
]