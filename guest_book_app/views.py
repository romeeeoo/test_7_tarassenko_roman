from django.shortcuts import render, redirect, get_object_or_404

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


# def update_view(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             task.description = form.cleaned_data['description']
#             task.detailed_description = form.cleaned_data['detailed_description']
#             task.status = form.cleaned_data['status']
#             task.deadline = form.cleaned_data['deadline']
#             task.save()
#             return redirect('detailed_task', pk=task.pk)
#     elif request.method == 'GET':
#         form = TaskForm(initial={
#             'description': task.description,
#             'detailed_description': task.detailed_description,
#             'status': task.status,
#             'deadline': task.deadline
#         })
#         return render(request, 'update_task.html', context={'task': task, 'form': form})

def update_view(request, pk):
    record = get_object_or_404(GuestBookRecord, pk=pk)
    print(record)
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
