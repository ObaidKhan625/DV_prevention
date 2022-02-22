from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'accounts'

urlpatterns = [
	path('profile/<str:profile_slug>/', views.profileView, name = 'profile-view'),
	path('profile-file-drop/', views.profile_drop_zone_file, name = 'profile-file-drop-zone-view'),
	path('profile-file-drop/upload/', views.profile_file_upload_view, name = 'profile-file-drop-upload-upload-view'),
	path('edit-profile/', views.profileEdit, name = 'profile-edit'),
	path('profile-rate/<str:profile_slug>/', views.profileRate, name='profile-rate'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,
	document_root = settings.MEDIA_ROOT)