from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Book
from django.views import View
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
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


class AddToShelfView(View):
    def get(self, request):
        stored_books = request.session.get("stored_books")

        context = {}

        if stored_books is None or len(stored_books) == 0:
            context["books"] = []
            context["has_books"] = False
        else:
            books = Book.objects.filter(id__in=stored_books)
            context["books"] = books.order_by("title")
            context["has_books"] = True

        return render(request, "book_site/shelf.html", context)

    def post(self, request):
        stored_books = request.session.get("stored_books")

        if stored_books is None:
            stored_books = []

        book_id = int(request.POST["book_id"])

        if book_id not in stored_books:
            stored_books.append(book_id)
        else:
            stored_books.remove(book_id)

        request.session["stored_books"] = stored_books

        return HttpResponseRedirect("shelf")
