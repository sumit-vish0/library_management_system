from django.shortcuts import render
from core.mock_data import BOOKS




def all_books_view(request):
    context = {
        'books': BOOKS
    }
    return render(request, 'all_books.html', context)


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

