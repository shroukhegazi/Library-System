from django.contrib import admin
from system.models import Book,Student
# Register your models here.

admin.site.site_header= "Library Admin Panel"
admin.site.site_title="Library Admin Panel"


class Student_admin(admin.ModelAdmin):
    list_display = ('id','username','email','is_staff','date_joined')
    list_display_links = ['id']
    list_editable = ['username','email']
    list_filter = ['date_joined']
    search_fields = ['id']


class Book_admin(admin.ModelAdmin):
    list_display = ['id', 'book_name', 'active', 'student_id','return_date']
    list_display_links = ['book_name']
    list_editable = ['active', 'student_id','return_date']
    list_filter = ['category_name','active']
    search_fields = ['id','book_name','category_name']




admin.site.register(Book,Book_admin)
admin.site.register(Student,Student_admin)


