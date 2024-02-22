from django.forms import ModelForm
from .models import Book, Author, Series


class BookForm(ModelForm):
    class Meta:
        model = Book
        exclude = ["slug", "author", "series"]
        labels = {
            "rating": "Your rating:",
        }


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
        labels = {
            "first_name": "Author's first name",
            "last_name": "Author's last name",
        }


class SeriesForm(ModelForm):
    class Meta:
        model = Series
        fields = "__all__"
        labels = {
            "series": "Series name:",
        }
