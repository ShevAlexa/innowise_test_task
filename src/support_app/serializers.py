from rest_framework import serializers
from support_app.models import UserTicket, Message, TicketStatus


class UserTicketSerializer(serializers.ModelSerializer):
    author = serializers.CharField(default=serializers.CurrentUserDefault(),
                                   read_only=True)
    status = serializers.CharField(default=TicketStatus.objects.get(id=1))

    class Meta:
        model = UserTicket
        fields = "__all__"


class CreateTicketSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    status = serializers.HiddenField(default=TicketStatus.objects.get(id=1))

    class Meta:
        model = UserTicket
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    author = serializers.CharField(default=serializers.CurrentUserDefault(),
                                   read_only=True)

    class Meta:
        model = Message
        fields = ('author', 'text', 'data', 'id')


class StatusesSerializer(serializers.ModelSerializer):
    ticket_status = serializers.PrimaryKeyRelatedField(many=True,
                                                       read_only=True)

    class Meta:
        model = TicketStatus
        fields = "__all__"
