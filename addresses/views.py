from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Address


class AddressView(CreateView):
    model = Address
    fields = ['address']
    template_name = 'addresses/home.html'
    success_url = '/address'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mapbox_access_token'] = 'pk.eyJ1IjoiZXBoaXJhbS1yZW5haXMiLCJhIjoiY2t5ajZ1aTVoMWk4ZTJvcG1nNzRjaWY0MiJ9.ipIanO9ZaafvcgugtuZAFg'
        context['addresses'] = Address.objects.all()
        return context