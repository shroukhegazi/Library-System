from pyexpat.errors import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from system.models import Student
from .forms import std_update, br_process
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
import re
from django.contrib.auth.hashers import make_password
from system.models import Book
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.
def home(request):
    bookobjects = Book.objects.all()
    context = {"books": bookobjects}
    return render(request, "system/home.html", context)


def register(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        Password = request.POST['Password']
        Confirm_Password = request.POST['Confirm_Password']
        # check for errorneous input
        if not (Student.objects.filter(username=username).exists()):
            if username.isalnum() and len(username) > 6:
                val = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                match = re.fullmatch(val, email)
                if match:
                    if (Password == Confirm_Password) and ((Password != '') and (Confirm_Password != '')):
                        myuser = Student.objects.create_user(username=username,email=email, first_name= fname, last_name=lname, password=Password)
                        myuser.save()
                        login(request, myuser)
                        messages.success(request, 'Your Account Created successfully')
                        return redirect('libhome')
                    messages.error(request, "enter passwords, Or Re-write the password")
                    return redirect("register")
                messages.error(request, "enter a valid email")
                return redirect("register")
            messages.error(request, "username should be more than 6 letters with no space")
            return redirect("register")
        messages.error(request, "username already exists")
        return redirect("register")

    return render(request, "system/register.html")


def loginuser(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        Password = request.POST['Password']
        myuser = authenticate(username=username, password=Password)
        if myuser is not None:
            login(request, myuser)
            return redirect("libhome")
        messages.error(request, "Invalid credentials! Please try again")
        return redirect("loginuser")
    return render(request, "system/login_user.html")


def Logoutueser(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('loginuser')

def about(request):
    return render(request, "system/about.html")

@login_required(login_url='loginuser')
def allbooks(request):
    search = Book.objects.all()
    book_name = None
    if 'search_name' in request.GET:
        book_name = request.GET['search_name']
        if book_name:
            search = search.filter(book_name__icontains=book_name)

    bookobjects = search
    context = {"books": bookobjects}
    return render(request, "system/allbooks.html", context)

def book(request, id):
    book = Book.objects.get(pk=id)
    context = {"book": book}
    return render(request, "system/book.html", context)


@login_required(login_url='loginuser')
def borrowed(request):
    bookobjects = Book.objects.all()
    context = {"books": bookobjects}
    return render(request, "system/borrowed.html", context)


@login_required(login_url='loginuser')
def process(request, id):
    student = request.user
    book = get_object_or_404(Book, pk=id)
    form = br_process(instance=book)
    if request.method == 'POST':
        form = br_process(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('libhome')

        else:
            form = br_process()
    book.active = False
    book.student_id = student
    book.save()
    context = {'book': book, 'form': form}
    return render(request, "system/br_process.html", context)


@login_required(login_url='loginuser')
def return_Book(request, id):
    book = get_object_or_404(Book, pk=id)
    book.active = True
    book.student_id = None
    book.return_date = None
    book.save()
    return redirect('myboard')
    context = {"book": book}
    return render(request, "system/return.html", context)


@login_required(login_url='loginuser')
def myboard(request):
    student = request.user
    books = Book.objects.filter(student_id=student)
    context = {"std": student, "books": books}
    return render(request, "system/myboard.html", context)


@login_required(login_url='loginuser')
def setting(request):
    file_date = request.FILES
    student = request.user
    students = Student.objects.filter(username=student).first()
    form = std_update(instance=students)
    if request.method == 'POST':
        form = std_update(request.POST, file_date, instance=students)
        if form.is_valid():
            form.save()
            return redirect('myboard')
        else:
            form = std_update()
    context = {"std": students, 'form': form}
    return render(request, "system/setting.html", context)

@login_required(login_url='loginuser')
def std_delete(request):
    student = request.user
    students = Student.objects.filter(username=student)
    bookofcurrent = Book.objects.filter(student_id=student)
    for book in bookofcurrent:
        book.active = True
        book.save()
    if request.method == 'POST':
        students.delete()
        return redirect('loginuser')
    context = {"std": students}
    return render(request, "system/std_delete.html", context)