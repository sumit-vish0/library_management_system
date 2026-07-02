from django.urls import path
from . import views

urlpatterns =[
    path('',views.home_view ,name ='home'),
    path('books/all/', views.all_books_view, name='all_books'),
    path('book-details/<int:book_id>',views.book_details_view, name = 'details' ),
    path('about/',views.about_view,name='about'),
    path('contact/',views.contact_view,name='contact')
]

