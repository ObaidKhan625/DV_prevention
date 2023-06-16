from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse

def auth_or_not(flag):
	def auth_or_not_d(view_func):
		def wrapper_func(request, *args, **kwargs):
			if ((request.user.is_authenticated == False and flag == 0) or (request.user.is_authenticated == True and flag == 1)):
				return view_func(request, *args, **kwargs)
			else:
				return redirect('complaints:explore-complaints')
		return wrapper_func
	return auth_or_not_d