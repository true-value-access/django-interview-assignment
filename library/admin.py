from django.contrib import admin

from library.models import MyUser,Book

# Register your models here.
admin.site.register(MyUser)

admin.site.register(Book)