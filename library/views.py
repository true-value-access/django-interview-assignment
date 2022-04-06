from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import Profile
from .models import Books
from .serializers import BooksSerializer
import jwt, datetime


import logging
_logger = logging.getLogger(__name__)

class Authenticate():
    def check_authentication(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            return Response({
                'message': 'Authentication Required'
            })
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({
                'message': 'Authentication Required'
            })
        return payload

    def check_librarian(self, user):
        if not user.is_librarian:
            return Response({
                'message': 'Access Denied ! Un Authorised Operation'
            })

class AddBookView(APIView):
    
    def post(self, request):
        auth = Authenticate()
        payload = auth.check_authentication(request)
        user = Profile.objects.filter(id=payload['id']).first()

        auth.check_librarian(user)
        book = BooksSerializer(data=request.data)
        book.is_valid(raise_exception=True)
        book.save()
        return Response(book.data)

class CheckAllBooksView(APIView):

    def get(self, request):
        auth = Authenticate()
        _ = auth.check_authentication(request)
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data)

class DeleteBookView(APIView):

    def post(self, request):
        auth = Authenticate()
        payload = auth.check_authentication(request)
        user = Profile.objects.filter(id=payload['id']).first()
        
        auth.check_librarian(user)

        book_id = request.data['id']
        book_id = Books.objects.filter(id=book_id)
        book_id.delete()
        return Response({
            'message':'Book deleted successfully'
        })

class IssueBookView(APIView):

    def post(self, request):
        auth = Authenticate()
        payload = auth.check_authentication(request)
        user = Profile.objects.filter(id=payload['id']).first()

        book_id = request.data['id']
        book_id = Books.objects.filter(id=book_id).first()
        if book_id.status == 'BORROWED':
            return Response({
                'message': 'Book already issued, please try later'
            })
        book_id.status = 'BORROWED'
        book_id.issued_by = user
        book_id.save()
        return Response({
            'message': 'Book Issued'
        })

class ReturnBookView(APIView):
    
    def post(self, request):
        auth = Authenticate()
        payload = auth.check_authentication(request)
        user = Profile.objects.filter(id=payload['id']).first()
        book_id = request.data['id']
        book_id = Books.objects.filter(id=book_id).first()
        if user != book_id.issued_by:
            return Response({
                'message': 'Something Went Wrong, User have not issued this book'
            })
        book_id.status = 'AVAILABLE'
        book_id.issued_by = None
        book_id.save()
        return Response({
            'message': 'Returned Successfully',
        })

class UpdateBookView(APIView):

    def post(self, request):
        auth = Authenticate()
        payload = auth.check_authentication(request)
        user = Profile.objects.filter(id=payload['id']).first()
        
        auth.check_librarian(user)
        book_id = Books.objects.filter(id=request.data['id'])
        if not book_id:
            return Response({
                'message': 'No record found'
            })
        vals = {key:request.data[key] for key in request.data.keys()}
        book_id.update(**vals)
        book_id = book_id.first()
        book_id.save()
        return Response({
            'message': 'Update Successfull'
        })

 
        





        



        


