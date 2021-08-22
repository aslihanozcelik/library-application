# Generated by Django 3.2.6 on 2021-08-22 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tc', models.IntegerField(max_length=11)),
                ('phone', models.IntegerField(max_length=11)),
                ('address', models.CharField(max_length=240)),
            ],
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
