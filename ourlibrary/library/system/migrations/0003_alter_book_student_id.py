# Generated by Django 3.2.7 on 2021-09-21 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_book_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='student_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Student'),
        ),
    ]
