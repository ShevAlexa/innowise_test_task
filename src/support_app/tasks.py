from __future__ import absolute_import
from celery import shared_task
from support_app.models import Message, UserTicket


@shared_task
def send_message(request, ticket_id):
    Message.objects.create(
        author=request.user,
        text=request.data['text'],
        ticket=UserTicket.objects.get(id=ticket_id),
    )
