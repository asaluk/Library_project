from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views import View

from .forms import BookForm
from .models import Book
from django.db.models import Q
# Create your views here.


class AddBook(TemplateView):
    template_name = "book_site/add_book.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book_form"] = BookForm()

        return context

    def post(self, request):
        book_form = BookForm(request.POST, request.FILES)

        if book_form.is_valid():
            book_form.save()
            return HttpResponseRedirect("shelf")
        else:
            return render(request, self.template_name, {'book_form': book_form})


class MainPageView(ListView):
    model = Book
    template_name = "book_site/main_page.html"
    ordering = ["title"]
    context_object_name = "books"


class BookDetailView(View):
    def is_stored_books(self, request, book_id):
        stored_books = request.session.get("stored_books")
        if stored_books is not None:
            is_in_your_shelf = book_id in stored_books
        else:
            is_in_your_shelf = False
        return is_in_your_shelf

    def get(self, request, slug):
        book = Book.objects.get(slug=slug)

        context = {
            "book": book,
            "saved_in_shelf": self.is_stored_books(request, book.id)
        }
        return render(request, "book_site/book_detail.html", context)


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
