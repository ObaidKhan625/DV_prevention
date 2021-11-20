from .forms import UpdateUserForm
from .models import User, User_Document
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from user_auth.decorators import auth_or_not

# Create your views here.

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def profileView(request, current_user_id, user_id = None):
	profile = User.objects.get(username = request.user)
	user_documents = User_Document.objects.filter(user_name = profile)
	context = {'profile':profile, 'user_documents':user_documents}
	return render(request, 'accounts/profile.html', context)

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def profileEdit(request, current_user_id, user_id = None):
	profile = User.objects.get(username = request.user)
	form = UpdateUserForm()
	if request.method == "POST":
		form = UpdateUserForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			form.save()
		return redirect('/')
	context = {'profile':profile, 'form':form}
	return render(request, 'accounts/profile_edit_form.html', context)

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def drop_zone_file(request):
	context = {}
	return render(request, 'accounts/drop-zone.html', context)

@login_required(login_url='user_auth:login')
@auth_or_not(1)
def file_upload_view(request):
	if request.method == "POST":
		my_file = request.FILES.get('file')
		if(str(my_file).endswith('jpg') or str(my_file).endswith('jpeg') or str(my_file).endswith('jfif') or str(my_file).endswith('pjpeg') or str(my_file).endswith('pjp') or str(my_file).endswith('png')):
			user_document = User_Document.objects.create(user_name = request.user, user_file = my_file, 
			user_file_thumbnail = my_file)
		else:
			user_document = User_Document.objects.create(user_name = request.user, user_file = my_file)
		return redirect('/')
	return JsonResponse({'post':'false'})