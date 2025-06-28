from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from catalog.models import Book, BorrowedBook, Author, Genre
from django.views import generic

def index(request):
    num_books = Book.objects.count()
    num_instances = BorrowedBook.objects.count()
    num_instances_available = BorrowedBook.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context)

class BookListView(generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book
