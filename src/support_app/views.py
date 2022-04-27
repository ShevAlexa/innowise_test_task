from rest_framework.permissions import IsAdminUser
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from support_app.models import UserTicket, TicketStatus, Message
from support_app.permissions import IsOwnerOrReadOnly
from support_app.serializers import UserTicketSerializer, MessageSerializer, \
    CreateTicketSerializer, StatusesSerializer, CreateMessageSerializer


class AuthenticatedUserView(mixins.CreateModelMixin,
                            GenericViewSet):
    queryset = UserTicket.objects.all()
    serializer_class = CreateTicketSerializer


class AdminAPIView(mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.UpdateModelMixin,
                   GenericViewSet):

    queryset = UserTicket.objects.all().order_by('status')
    serializer_class = UserTicketSerializer
    permission_classes = (IsAdminUser,)


class ShowTicketAPIView(mixins.RetrieveModelMixin,
                        GenericViewSet):
    queryset = UserTicket.objects.all()
    serializer_class = UserTicketSerializer
    permission_classes = (IsAdminUser, IsOwnerOrReadOnly)


class MessageUpdateOrDeleteAPIView(mixins.DestroyModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.RetrieveModelMixin,
                                   GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class MessageCreateAPIView(mixins.CreateModelMixin,
                           GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser)


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
