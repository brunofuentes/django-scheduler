from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Request
from .tasks import http_request

@receiver(post_save, sender=Request)
def create_request(sender, created, **kwargs):
    req = Request.objects.latest('pk')
    if created or req.status is None:
        http_request.apply_async(args=[req.id], eta=req.start_on)
        return 'Done'

    else:
        return 'no new request was added, row only updated'