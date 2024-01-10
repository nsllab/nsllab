from django.db import models
from django.contrib.auth.models import AbstractUser
from publications.choices import POSITION
# from cloudinary_storage.storage import MediaCloudinaryStorage
# import

# Create your models here.

class Member(AbstractUser):
    address = models.CharField(max_length=150, null=True, blank=True)
    login_cnt = models.IntegerField(default=0) # increments
    restriction_date = models.DateTimeField(null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)

# Create your models here.

class Bio(models.Model):
    bio = models.TextField(blank=True, null=True)
    career = models.TextField()
    name = models.CharField(max_length=255)
    
    position = models.IntegerField(choices=POSITION, default=1, null=False, blank=False)
    link = models.URLField(blank=True, null=True)
    email_list = models.TextField()
    image = models.ImageField(upload_to='bio_images/', null=True, blank=True)
    user = models.OneToOneField(Member, on_delete=models.DO_NOTHING, related_name='bio', null=True, blank=True)

    def __str__(self):
        return self.name