from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render
from catalog.models import Book, BookInstance, Author, Genre
from django.views import generic

@login_required
def index(request):
    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_visits = request.session.get('num_visits',0)
    num_visits += 1
    request.session['num_vists'] = num_visits

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context)

class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book

class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book
