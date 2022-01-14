from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'accounts'

urlpatterns = [
	path('profile-view/<str:profile_slug>/', views.profileView, name = 'profile-view'),
	path('file-drop-zone/', views.drop_zone_file, name = 'file-drop-zone-view'),
	path('file-drop-zone/upload/', views.file_upload_view, name = 'file-drop-upload-upload-view'),
	path('edit-profile/', views.profileEdit, name = 'profile-edit'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL,
	document_root = settings.MEDIA_ROOT)