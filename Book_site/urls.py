from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('book/<slug:slug>', views.BookDetailView.as_view(), name="book-detail")
]
