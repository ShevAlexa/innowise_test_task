from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView,\
    TokenRefreshView, TokenVerifyView
from support_app.views import AuthenticatedUserView, AdminAPIView, \
    MessageUpdateOrDeleteAPIView, MessagesAPIView, \
    StatusesAPIView, MessageCreateAPIView, ShowTicketAPIView
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'ticket/create', AuthenticatedUserView)
router.register(r'tickets', AdminAPIView)
router.register(r'ticket/message', MessageUpdateOrDeleteAPIView)
router.register(r'message/create', MessageCreateAPIView)
router.register(r'ticket/messages', MessagesAPIView)
router.register(r'status', StatusesAPIView)
router.register(r'ticket', ShowTicketAPIView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')
]
