from django.forms import ModelForm

from guest_book_app.models import GuestBookRecord


class RecordForm(ModelForm):
    class Meta:
        model = GuestBookRecord
        fields = [
            "author",
            "email",
            "text",
        ]
