from django.contrib.auth.models import User
from django.db import models


class TicketStatus(models.Model):
    status = models.CharField("Status", max_length=50)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"


class UserTicket(models.Model):
    author = models.ForeignKey(User, related_name="ticket_author", on_delete=models.CASCADE)
    status = models.ForeignKey(TicketStatus, related_name="ticket_status", on_delete=models.CASCADE)
    text = models.TextField("Text", null=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"


class Message(models.Model):
    author = models.ForeignKey(User, related_name="message_author", on_delete=models.CASCADE)
    text = models.TextField("Message text")
    ticket = models.ForeignKey(UserTicket, on_delete=models.CASCADE, related_name="messages")
    data = models.DateTimeField(auto_now_add=True)
