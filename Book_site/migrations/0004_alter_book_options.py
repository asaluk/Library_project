# Generated by Django 4.2.7 on 2024-02-13 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book_site', '0003_alter_book_author_alter_book_series'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name_plural': 'Series'},
        ),
    ]