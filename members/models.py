from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Member(AbstractUser):
    address = models.CharField(max_length=150, null=True, blank=True)
    login_cnt = models.IntegerField(default=0) # increments
    restriction_date = models.DateTimeField(null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)