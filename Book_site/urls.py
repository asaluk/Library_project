from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('book/<slug:slug>', views.BookDetailView.as_view(), name="book-detail")
]
