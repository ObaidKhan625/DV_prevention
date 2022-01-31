import geocoder

from django.db import models


mapbox_access_token = 'pk.eyJ1IjoiZXBoaXJhbS1yZW5haXMiLCJhIjoiY2t5ajZ1aTVoMWk4ZTJvcG1nNzRjaWY0MiJ9.ipIanO9ZaafvcgugtuZAFg'

class Address(models.Model):
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_access_token)
        print(g)
        g = g.latlng  # returns => [lat, long]
        self.lat = g[0]
        self.long = g[1]
        return super(Address, self).save(*args, **kwargs)
