from django.contrib import admin
from .models import Book, Author, Series

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_separator = "|"
    list_display = ["title", "author", "rating", "tome", "series"]
    list_filter = ["author", "rating", "series"]
    prepopulated_fields = {"slug": ("title", )}
    search_fields = ("title", "author__first_name",
                     "author__last_name", "series__series")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name"]


class SeriesAdmin(admin.ModelAdmin):
    list_display = ["series"]


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Series, SeriesAdmin)
