from .serializers import ProfileSerializers
from rest_framework.response import Response
from django.contrib.auth import authenticate
from library.views import Authenticate
from rest_framework.views import APIView
import jwt, datetime
from .models import Profile

import logging

_logger = logging.getLogger(__name__)


class RegisterView(APIView):
    def post(self, request):
        serializer = ProfileSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        user = Profile.objects.filter(username=username).first()
        if not user :
            return Response({'message': 'Incorrect Username !'})
        if not user.password == password:
            return Response({'message': 'Incorrect password !'})
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'message': 'Login Successfull for {}'.format(user.username)
        }
        return response

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Logout successfully !'
        }
        return response

class ShowUsersView(APIView):
    
    def post(self, request):
        auth = Authenticate()
        payload = auth.check_authentication(request)
        user = Profile.objects.filter(id=payload['id']).first()

        auth.check_librarian(user)

        member_ids = Profile.objects.all()
        res = []
        for member in member_ids:
            if member.is_librarian:
                continue
            profile_serializer = ProfileSerializers(member)
            res.append(profile_serializer)
        return Response({
            'Members':res
        })

class DeleteUserView(APIView):
    def post(self, request):
        auth = Authenticate()
        payload = auth.check_authentication(request)
        user = Profile.objects.filter(id=payload['id']).first()
        try:
            if request.data['username'] != user.username and not user.is_librarian:
                return Response({
                    'message': 'UnAtuhorised access'
                })
        except Exception as e:
            return Response({
                'message': 'Something Went Wrong'
            })
        user_id = Profile.objects.filter(username=request.data['username']).first()
        user_id.delete()
        return Response(
            {'message': 'User Deleted Successfully'}
        )

class UpdateMemberView(APIView):

    def post(self, request):
        auth = Authenticate()
        payload = auth.check_authentication(request)
        user = Profile.objects.filter(id=payload['id']).first()
        auth.check_librarian(user)
        
        user = Profile.objects.filter(username=request.data['username'])
        if not user:
            return Response({
                'message': 'No record found'
            })
        vals = {key:request.data[key] for key in request.data.keys()}
        user.update(**vals)
        user = user.first()
        user.save()
        return Response({
            'message': 'Update Successfull'
        })



