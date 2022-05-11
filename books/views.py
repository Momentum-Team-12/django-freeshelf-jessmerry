from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .models import Category

# Create your views here.


def list_book(request):
    books = Book.objects.all()
    return render(request, "books/list_book.html",
                {"books": books})


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, "books/book_detail.html", {"book": book})


def books_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    books = Book.objects.filter(category=category)

    return render(request, 'books/category.html', {'books': books, 'category': category})
