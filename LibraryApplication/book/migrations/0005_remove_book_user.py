# Generated by Django 3.2.6 on 2021-08-22 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_book_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
    ]