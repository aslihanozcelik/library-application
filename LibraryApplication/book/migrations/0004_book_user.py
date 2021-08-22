# Generated by Django 3.2.6 on 2021-08-22 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20210822_1751'),
        ('book', '0003_remove_book_edition'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='book', to='members.member'),
            preserve_default=False,
        ),
    ]
