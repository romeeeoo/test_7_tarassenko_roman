from django.urls import path, include

from guest_book_app.views import index_view

urlpatterns = [
    path('', index_view, name='index')
]
