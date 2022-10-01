from django.shortcuts import render, redirect, get_object_or_404

from guest_book_app import DEFAULT_STATUS
from guest_book_app.forms import RecordForm
from guest_book_app.models import GuestBookRecord


# Create your views here.
def index_view(request):
    records = GuestBookRecord.objects.all().order_by("created_at").filter(status=DEFAULT_STATUS)
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
                text=form.cleaned_data["text"])
            new_record.save()
            return redirect("index")
        else:
            return render(request, "add_record.html", context={"form": form})


def update_view(request, pk):
    record = get_object_or_404(GuestBookRecord, pk=pk)
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            record.author = form.cleaned_data["author"]
            record.email = form.cleaned_data["email"]
            record.text = form.cleaned_data["text"]
            record.save()
            return redirect("index")
    elif request.method == "GET":
        form = RecordForm(instance=record)
        return render(request, "update_record.html", context={"form": form})


def delete_view(request, pk):
    record = get_object_or_404(GuestBookRecord, pk=pk)
    return render(request, "confirm_delete.html", context={"record": record})


def confirm_delete_view(request, pk):
    record = get_object_or_404(GuestBookRecord, pk=pk)
    record.delete()
    return redirect("index")
