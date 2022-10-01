from django.urls import path, include

from guest_book_app.views import index_view, add_view, update_view

urlpatterns = [
    path("", index_view, name="index"),
    path("add/", add_view, name="add_record"),
    path("<int:pk>/update", update_view, name="update_record"),
]
