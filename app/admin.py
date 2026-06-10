from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.MakeOrder)
admin.site.register(models.DeliveryOrder)
admin.site.register(models.Review)