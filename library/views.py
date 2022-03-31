from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken

from .models import MyUser, Book, Record
from .serializers import BookSerializer, MemberSerializer

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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def viewBooks(request):
    books = Book.objects.all()
    serial = BookSerializer(books, many=True)
    return Response(serial.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def viewBook(request, id):
    book = Book.objects.get(id=id)
    serial = BookSerializer(book)
    return Response(serial.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateBook(request, id):
    if request.user.role == 'MEMBER':
        return Response({'message':"You don't have permission to do this"})
    data = request.data
    book = Book.objects.get(id=id)
    book.name = data['name']
    book.save()
    return Response({'message': 'Book updated Successfully'})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def removeBook(request, id):
    if request.user.role == 'MEMBER':
        return Response({'message':"You don't have permission to do this"})
    book = Book.objects.get(id=id)
    book.delete()
    return Response({'message': 'Book deleted Successfully'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addMember(request):
    if request.user.role == 'MEMBER':
        return Response({'message':"You don't have permission to do this"})
    data = request.data
    username = data['username']
    password = make_password(data['password'])
    try:
        user = MyUser.objects.create(
            username=username,
            password=password
        )
    except:
        return Response({'message':'username already exists'})
    user.first_name = data['fname']
    user.last_name = data['lname']
    user.email = data['email']
    user.role = 'MEMBER'
    user.save()
    return Response({'message':'Member added successfully'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def viewMembers(request):
    if request.user.role == 'MEMBER':
        return Response({'message':"You don't have permission to do this"})
    members = MyUser.objects.filter(role='MEMBER')
    serial = MemberSerializer(members, many=True)
    return Response(serial.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def viewMember(request,id):
    if request.user.role == 'MEMBER':
        return Response({'message':"You don't have permission to do this"})
    member = MyUser.objects.get(id=id)
    serial = MemberSerializer(member)
    return Response(serial.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateMember(request,id):
    if request.user.role == 'MEMBER':
        return Response({'message':"You don't have permission to do this"})
    data = request.data
    user = MyUser.objects.get(id=id)
    user.username = data['username']
    user.password = make_password(data['password'])
    user.first_name = data['fname']
    user.last_name = data['lname']
    user.email = data['email']
    user.role = 'MEMBER'
    user.save()
    return Response({'message':'Member added successfully'})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def removeMember(request,id):
    if request.user.role == 'MEMBER':
        return Response({'message':"You don't have permission to do this"})
    user = MyUser.objects.get(id=id)
    user.delete()
    return Response({'message':'Member removed successfully'})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def borrowBook(request,id):
    book = Book.objects.get(id=id)
    book.status = False
    book.save()
    Record.objects.create(
        book = book,
        user = request.user,
        record_type = 'BORROW'
    )
    return Response({'message':f'You have successfully borrowed {book.name}'})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def returnBook(request,id):
    book = Book.objects.get(id=id)
    book.status = True
    book.save()
    Record.objects.create(
        book = book,
        user = request.user,
        record_type = 'RETURN'
    )
    return Response({'message':f'You have successfully returned {book.name}'})