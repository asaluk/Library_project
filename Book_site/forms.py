from django.forms import ModelForm
from .models import Book, Author, Series
from django import forms


class BookForm(ModelForm):
    author_first_name = forms.CharField(max_length=50)
    author_last_name = forms.CharField(max_length=100)
    series_name = forms.CharField(
        max_length=200, required=False)  

    class Meta:
        model = Book
        fields = ['title', 'author_first_name',
                  'author_last_name', 'rating', 'cover', 'tome']
        labels = {
            "rating": "Your rating:",
        }

    def save(self, commit=True):
        book = super().save(commit=False)
        author, _ = Author.objects.get_or_create(
            first_name=self.cleaned_data['author_first_name'],
            last_name=self.cleaned_data['author_last_name'],
        )
        book.author = author
        book.series = Series.objects.get_or_create(
            series_name=self.cleaned_data.get('series_name', None))[0]
        if commit:
            book.save()
        return book
