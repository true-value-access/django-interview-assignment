from django.urls import path
from django.contrib.auth import views as auth_views 
from .views import RegisterView, LoginView, LogoutView, ShowUsersView, DeleteUserView, UpdateMemberView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('allmembers/', ShowUsersView.as_view(), name='members'),
    path('deletemember/', DeleteUserView.as_view(), name='delete-members'),
    path('updatemember/', UpdateMemberView.as_view(), name='update-members')
]