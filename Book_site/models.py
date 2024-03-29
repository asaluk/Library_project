from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Series(models.Model):
    series_name = models.CharField(max_length=200)

    def __str__(self):
        return self.series_name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books")
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)])
    cover = models.ImageField(upload_to="covers")
    slug = models.SlugField(default='')
    tome = models.IntegerField(default="", blank=True, null=True)
    series = models.ForeignKey(
        Series, on_delete=models.CASCADE, blank=True, null=True, related_name="books", default="")

    def __str__(self):
        return f"{self.title} {self.author}"

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def generate_slug(self):
        if not self.slug:
            self.slug = slugify(self.title)

    def save(self, *args, **kwargs):
        self.generate_slug()
        super().save(*args, **kwargs)
