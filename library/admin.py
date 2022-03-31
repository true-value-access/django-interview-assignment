from django.contrib import admin

from library.models import MyUser,Book, Record

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Book)
admin.site.register(Record)