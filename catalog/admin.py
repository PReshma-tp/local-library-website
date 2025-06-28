from django.contrib import admin
from .models import Author, Book, BorrowedBook, Genre
# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BorrowedBook)
admin.site.register(Genre)
