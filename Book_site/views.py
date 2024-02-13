from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Book
from django.views import View
from django.db.models import Q
# Create your views here.


class MainPageView(ListView):
    model = Book
    template_name = "book_site/main_page.html"
    ordering = ["title"]
    context_object_name = "books"


class BookDetailView(DetailView):
    model = Book
    template_name = "book_site/book_detail.html"
    context_object_name = "book"


class SearchedView(View):
    def get(self, request):
        return render(request, "book_site/searched.html")

    def post(self, request):
        searched = request.POST["search"]
        searched_books = Book.objects.filter(Q(author__first_name__contains=searched) | Q(author__last_name__contains=searched)
                                             | Q(title__contains=searched) | Q(series__series__contains=searched))
        context = {
            "searched": searched,
            "searched_books": searched_books,
        }
        return render(request, "book_site/searched.html", context)
