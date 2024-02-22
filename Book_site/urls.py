from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainPageView.as_view(), name="main-page"),
    path('book/<slug:slug>', views.BookDetailView.as_view(), name="book-detail"),
    path('searched', views.SearchedView.as_view(), name="searched"),
    path('shelf', views.AddToShelfView.as_view(), name="shelf"),
    path('add_book', views.AddBook.as_view(), name="add-book")
]
