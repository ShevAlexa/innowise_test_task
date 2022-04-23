from django.contrib import admin

from support_app.models import Message, UserTicket, TicketStatus


class MessageAdmin(admin.StackedInline):
    extra = 1
    model = Message
    readonly_fields = ['text', 'author', 'ticket']


class UserTicketAdmin(admin.ModelAdmin):
    inlines = [MessageAdmin]
    readonly_fields = ['author', 'data']


class TicketStatusAdmin(admin.ModelAdmin):
    readonly_fields = ["status"]


admin.site.register(UserTicket, UserTicketAdmin)
admin.site.register(TicketStatus, TicketStatusAdmin)
