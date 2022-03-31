from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from library.models import Book, MyUser

class BookSerializer(serializers.ModelSerializer):
    status = SerializerMethodField()
    class Meta:
        model = Book
        fields = '__all__'
    
    def get_status(self, obj):
        return 'BORROWED' if obj.status else 'AVALIABLE'
    
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'