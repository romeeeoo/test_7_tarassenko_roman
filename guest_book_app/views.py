from django.shortcuts import render

from guest_book_app.models import GuestBookRecord


# Create your views here.
def index_view(request):
    records = GuestBookRecord.objects.all().order_by("created_at").filter(status=1)
    return render(request, "index.html", context={"records": records})
