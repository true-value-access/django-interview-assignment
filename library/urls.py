from django.urls import path
from .views import AddBookView, CheckAllBooksView, DeleteBookView, IssueBookView, UpdateBookView


urlpatterns = [
    path('addbook/', AddBookView.as_view(), name='library-view'),
    path('getbooks/', CheckAllBooksView.as_view(), name='get-books'),
    path('deletebook/', DeleteBookView.as_view(), name='delete-books'),
    path('issuebook/', IssueBookView.as_view(), name='issue-book'),
    path('updatebook/', UpdateBookView.as_view(), name='update-book'),
]