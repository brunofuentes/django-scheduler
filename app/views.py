from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from .tasks import sample_task

# Create your views here.
def test(request):
    sample_task.delay()
    return HttpResponse("DONE")
