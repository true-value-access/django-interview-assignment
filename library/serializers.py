from rest_framework import serializers

from library.models import Book, MyUser

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'