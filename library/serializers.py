from rest_framework import serializers

from . models import Books

class BooksSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Books
        fields = ('book_name', 'authot_name', 'price', 'status','issued_by', 'id')