from django.db import models
from users.models import Profile

STATUS = [
    ('AVAILABLE', 'AVAILABLE'),
    ('BORROWED', 'BORROWED')
]

class Books(models.Model):
    
    book_name = models.CharField(max_length=200)
    authot_name = models.CharField(max_length=200)
    price = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS, default='AVAILABLE')
    issued_by = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
