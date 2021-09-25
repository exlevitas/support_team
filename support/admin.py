from django.contrib import admin

# Register your models here.
from support.models import *


class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'status')
    ordering = ['status', 'created']
    search_fields = ('status', 'created')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('ticket_comment', 'name_comment', 'position_comment',
                    'text_comment', 'created_comment')
    list_filter = ('ticket_comment', 'position_comment', 'created_comment')
    search_fields = ('ticket_comment', 'name_comment', 'text_comment')


admin.site.register(Comment, CommentAdmin)
admin.site.register(Ticket, TicketAdmin)