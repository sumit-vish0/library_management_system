from django.shortcuts import render
from .mock_data import BOOKS

def home_view(request):
    query = request.GET.get('search','')

    books_list = list()

    if query:
        for book in BOOKS:
            if query.lower() in book['title'].lower():
                books_list.append(book)
    else:
        books_list = BOOKS

    context ={
        'books':books_list,
    }

    if len(books_list) == 0:
        context = {
        "message": f"Books containing '{query}' were not found."
        }

    return render(request,'home.html',context)

def about_view(request):
    return render(request,'about.html')

def contact_view(request):
    return render(request,'contact.html')