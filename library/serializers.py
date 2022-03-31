from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from library.models import Book, MyUser, Record

class BookSerializer(serializers.ModelSerializer):
    status = SerializerMethodField()
    class Meta:
        model = Book
        fields = '__all__'
    
    def get_status(self, obj):
        return 'AVAILABLE' if obj.status else 'BORROWED'
    
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'
    
class RecordSerializer(serializers.ModelSerializer):
    date_time_stamp = SerializerMethodField()
    book = SerializerMethodField()
    user = SerializerMethodField()
    class Meta:
        model = Record
        # fields = '__all__'
        fields = ['id', 'book', 'user', 'record_type', 'date_time_stamp']
    
    def get_date_time_stamp(self, obj):
        return str(obj.created)

    def get_book(self, obj):
        return {
            'id':obj.book.id,
            'name':obj.book.name
        }
    
    def get_user(self, obj):
        return {
            'id':obj.user.id,
            'name':f'{obj.user.first_name} {obj.user.last_name}' 
        }