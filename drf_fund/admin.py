from django.contrib import admin

from drf_fund import models

admin.site.register(models.Profile)
admin.site.register(models.Group)
admin.site.register(models.Transaction)
admin.site.register(models.ProfileGroup)
admin.site.register(models.RegisteredGroup)

