from support_app.models import *
import pytest


class TestShowTicket:
    @pytest.mark.django_db
    def test_1(self):
        status = TicketStatus.objects.create(status="new")
        assert status.status == "new", 'name mistake'

    @pytest.mark.django_db
    def test_2(self):
        user = User.objects.create(username="test_name")
        status = TicketStatus.objects.create(status="frozen")
        UserTicket.objects.create(status=status, author=user, text="test_text")
        ticket = UserTicket.objects.get(text="test_text")
        assert ticket.status.status == "frozen" and ticket.author.username == "test_name", 'quantity mistake'

    @pytest.mark.django_db
    def test_3(self):
        user = User.objects.create(username="test_name", is_superuser=True)
        assert user.is_superuser is True, 'is_superuser mistake'
