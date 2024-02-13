from django.forms import ModelForm
from .models import Book, Author, Series


class BookForm(ModelForm):
    class Meta:
        model = Book
        exclude = ["slug", ]
        labels = {
            "rating": "Your rating:",
        }


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = "__all__"


class SeriesForm(ModelForm):
    class Meta:
        model = Series
        fields = "__all__"
