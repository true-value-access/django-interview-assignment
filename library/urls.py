from unicodedata import name
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('login/token/', TokenObtainPairView.as_view(), name='login_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', views.register, name="register"),
    
    path('add-book/', views.addBook, name='add_book'),
    path('view-books/', views.viewBooks, name='view_books'),
    path('view-book/<str:id>', views.viewBook, name='view_book'),
    path('update-book/<str:id>', views.updateBook, name='update_book'),
    path('remove-book/<str:id>', views.removeBook, name='remove_book'),

    path('add-member/', views.addMember, name='add_member'),
    path('view-members/', views.viewMembers, name='view_members'),
    path('view-member/<str:id>', views.viewMember, name='view_member'),
    path('update-member/<str:id>', views.updateMember, name='update_member'),
    path('remove-member/<str:id>', views.removeMember, name='remove_member'),

    path('borrow-book/<str:id>', views.borrowBook, name='borrow_book'),
    path('return-book/<str:id>', views.returnBook, name='return_book'),

    path('view-records/', views.viewRecords, name='view_records')
]
