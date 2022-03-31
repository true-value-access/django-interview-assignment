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
]
