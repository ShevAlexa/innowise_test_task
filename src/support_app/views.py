from django.http import HttpResponse
from rest_framework.permissions import IsAdminUser
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from support_app.models import UserTicket, TicketStatus, Message
from support_app.permissions import IsOwnerOrReadOnly
from support_app.serializers import UserTicketSerializer, MessageSerializer,\
    CreateTicketSerializer, StatusesSerializer
from support_app.tasks import send_message


class AuthenticatedUserView(mixins.CreateModelMixin,
                            GenericViewSet):
    queryset = UserTicket.objects.all()
    serializer_class = CreateTicketSerializer


class AdminAPIView(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.UpdateModelMixin,
                   GenericViewSet):

    queryset = UserTicket.objects.all().order_by('status')
    serializer_class = UserTicketSerializer
    permission_classes = (IsAdminUser,)


class ShowTicket(APIView):
    def get(self, request, ticket_id):
        ticket = UserTicket.objects.get(id=ticket_id)
        if request.user == ticket.author or request.user.is_superuser:
            messages_list = Message.objects.filter(ticket_id=ticket_id)
            ticket_information = UserTicketSerializer(ticket).data
            ticket_information['messages'] = MessageSerializer(messages_list,
                                                               many=True).data
            return Response({'ticket': ticket_information})
        raise Exception('access closed')

    def post(self, request, ticket_id):
        ticket = UserTicket.objects.get(id=ticket_id)
        if request.user == ticket.author or request.user.is_superuser:
            send_message(request, ticket_id)
            return HttpResponse('message sent')
        raise Exception('access closed')


class MessageUpdateOrDeleteAPIView(mixins.DestroyModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.RetrieveModelMixin,
                                   GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class MessagesAPIView(mixins.ListModelMixin,
                      GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAdminUser,)


class StatusesAPIView(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    queryset = TicketStatus.objects.all()
    serializer_class = StatusesSerializer
    permission_classes = (IsAdminUser,)
