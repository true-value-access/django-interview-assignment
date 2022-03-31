from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken

from library.models import MyUser, Book

# Create your views here.

@api_view(['POST'])
def register(request):
    data = request.data
    username = data['username']
    password = make_password(data['password'])
    role = data['role']

    try:
        user = MyUser.objects.create(
            username = username,
            password = password,
        )
        user.role = role
        user.save()
        refresh = RefreshToken.for_user(user)

        res = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    except: 
        res = {'message': 'username already exists'}
    
    return Response(res)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addBook(request):
    if request.user.role == 'MEMBER':
        return Response({'message':"You don't have permission to do this"})
    data = request.data
    Book.objects.create(
        name = data['name']
    )
    return Response({'message': 'Book Created Successfully'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateBook(request):
    if request.user.role == 'MEMBER':
        return Response({'message':"You don't have permission to do this"})
    data = request.data
    Book.objects.create(
        name = data['name']
    )
    return Response({'message': 'Book updated Successfully'})