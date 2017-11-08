from django.contrib import admin

from .models import AccessData
from .models import MapData
# Register your models here.

admin.site.register(AccessData)
admin.site.register(MapData)
