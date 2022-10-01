from django.contrib import admin

from guest_book_app.models import GuestBookRecord, RecordStatus

# Register your models here.
admin.site.register(GuestBookRecord)
admin.site.register(RecordStatus)
