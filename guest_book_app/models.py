from django.db import models

from guest_book_app import DEFAULT_STATUS


# Create your models here.
class RecordStatus(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.status)


class GuestBookRecord(models.Model):
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=500)
    text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(RecordStatus, on_delete=models.CASCADE, default=DEFAULT_STATUS)

    def __str__(self):
        return "{}. {}".format(self.pk, self.text, self.status)
