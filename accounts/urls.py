from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'accounts'

urlpatterns = [
	path('user-dashboard/<str:user_id>/', views.userDashboard, name='user-dashboard'),
	path('profile-view/<str:user_id>/', views.profileView, name='profile-view'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,
	document_root = settings.MEDIA_ROOT)