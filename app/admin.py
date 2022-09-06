from django.contrib import admin
from . import models
from django.contrib.auth.models import Group

# Register your models here.

class RequestAdmin(admin.ModelAdmin):
    fields = ('title', 'requester', 'type', 'url', 'start_on')
    list_display = ('id', 'title', 'requester', 'type', 'url', 'start_on', 'status', 'res_status', 'res_body')

admin.site.register(models.Request, RequestAdmin)
admin.site.unregister(Group)
