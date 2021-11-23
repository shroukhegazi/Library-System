from django.db import models
from django.contrib.auth.models import AbstractUser


class Student(AbstractUser):
    photo = models.ImageField(default='user.png', upload_to='photos', null=True, blank=True)

    def __str__(self):
        return self.username


class Book(models.Model):
    book_name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    book_photo = models.ImageField(upload_to='photos', null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    summary = models.TextField(null=True, blank=True)
    category_name = models.CharField(max_length=250)
    return_date = models.DateField(null=True, blank=True)
    student_id = models.ForeignKey(Student, verbose_name=("Student"), on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.book_name
