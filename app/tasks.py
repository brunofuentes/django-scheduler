from celery import shared_task
from datetime import datetime
from .models import Request
import json
import requests


@shared_task(bind=True)
def sample_task(self):
    for i in range(10):
        print(i)
    return 'Done'

@shared_task(bind=True)
def http_request(self, req_id):

    res = Request.objects.get(pk=req_id)
    url = res.url
    req_type = res.type
    try:

        if res is None:
            return 'Request not found'

        if req_type == 'GET':
            r = requests.get(url)
        if req_type == 'POST':
            r = requests.post(url, data={'key': 'post request is working'})

        if r.ok: 
            statusText = 'SUCCESS'
        else:
            statusText = 'FAILED'

        res.status = statusText
        res.res_body = {
            'body': r.text,
            }
        res.res_status = r.status_code
        res.url = url
        res.save()

        print(statusText + ', Saved to requests table.')
        return req_type + ' http request, done'

    except Exception as e:
        statusText = 'FAILED'
        res.status = statusText
        res.res_body = {
            'error': str(e)
        }
        res.save()
        return 'Did not work'