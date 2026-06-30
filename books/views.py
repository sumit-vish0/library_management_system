from django.shortcuts import render
from .mock_data import BOOKS

def home_view(request):
    context ={
        'books':BOOKS,
    }
    return render(request,'home.html',context)


def book_details_view(request, book_id):
    data =None

    for book in BOOKS:
        if book['id']==book_id:
            data = book
            break
    context ={
        'book': data
    }
    return render(request,'book-details.html',context)

def about_view(request):
    return render(request,'about.html')

def contact_view(request):
    return render(request,'contact.html')