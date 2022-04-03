from django.db import models
from django.contrib.auth.models import User

class Profile(User):

    is_librarian = models.BooleanField(verbose_name='Is Librarian', default=False, blank=True, null=True)