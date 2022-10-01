from django.shortcuts import render, redirect

from guest_book_app.forms import RecordForm
from guest_book_app.models import GuestBookRecord, RecordStatus


# Create your views here.
def index_view(request):
    records = GuestBookRecord.objects.all().order_by("created_at").filter(status=1)
    return render(request, "index.html", context={"records": records})


def add_view(request):
    if request.method == "GET":
        form = RecordForm()
        return render(request, "add_record.html", context={"form": form})
    elif request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            new_record = GuestBookRecord(
                author=form.cleaned_data["author"],
                email=form.cleaned_data["email"],
                text=form.cleaned_data["text"],
                status=RecordStatus(1))
            new_record.save()
            return redirect("index")
        else:
            return render(request, "add_record.html", context={"form": form})
