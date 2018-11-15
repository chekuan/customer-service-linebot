from django.contrib import admin
from .models import  Program, UnableToHandleMsg


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'program_id')


class UnableToHandleMsgAdmin(admin.ModelAdmin):
    list_display = ('poster', 'msg', 'timestamp')

admin.site.register(Program, ProgramAdmin)
admin.site.register(UnableToHandleMsg, UnableToHandleMsgAdmin)
