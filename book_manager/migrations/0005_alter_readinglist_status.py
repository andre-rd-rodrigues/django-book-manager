# Generated by Django 4.2.11 on 2024-12-03 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_manager', '0004_book_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readinglist',
            name='status',
            field=models.CharField(choices=[('to_read', 'To Read'), ('reading', 'Reading'), ('finished', 'Finished'), ('removed', 'Removed')], default='to_read', max_length=20),
        ),
    ]
