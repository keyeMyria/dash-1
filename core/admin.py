from django.contrib import admin

from .models import Attachment


@admin.register(Attachment)
class AttachmentModelAdmin(admin.ModelAdmin):
    pass
