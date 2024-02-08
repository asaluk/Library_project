from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Book  
# Create your views here.


class IndexView(ListView):
    model = Book
    template_name = "book_site/index.html"
    ordering = ["title"]
    context_object_name = "books"
    


class BookDetailView(DetailView):
    pass