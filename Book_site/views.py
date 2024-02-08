from django.shortcuts import render
from django.views.generic import DetailView
# Create your views here.


def index(request):
    return render(request, "book_site/index.html")

class BookDetailView(DetailView):
    pass