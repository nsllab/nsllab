from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from members.models import Member

def get_default_user():
    return get_user_model().objects.get(username='admin').id

# Create your models here.

class Serendipity(models.Model):
    user = models.CharField(null=True, blank=True)
    subject = models.TextField("Serendipity", max_length=600)
    visit = models.IntegerField(null=True)
    write_date = models.DateTimeField(default=timezone.now, null=True)
    update_date = models.DateTimeField(default=timezone.now, null=True)
    ref = models.CharField(max_length=100, null=True, blank=True)
    tcp_ip = models.CharField(max_length=120, null=True)
    writer = models.ForeignKey(Member, on_delete=models.DO_NOTHING, related_name='serendipity', default=get_default_user)
    