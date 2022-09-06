from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Request(models.Model):

    REQUEST_TYPES = (
        ("GET", "GET"),
        ("POST", "POST")
    )

    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(choices=REQUEST_TYPES ,default="GET", max_length=100)
    url = models.CharField(null=False, default='' ,max_length=500)
    start_on = models.DateTimeField(null=False)
    status = models.TextField(max_length=50, null=True)
    res_status = models.TextField(max_length=500)
    res_body = models.JSONField(default=dict)

    def __str__(self):
        return self.title


