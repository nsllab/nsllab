from django.db import models


# from accounts.models import CustomUser
from django.utils import timezone
from django.contrib.auth import get_user_model
from .choices import PAPER_STATUS, PAPER_TYPE
from members.models import Member

def get_default_user():
    return get_user_model().objects.get(username='admin').id

# Create your models here.
class Journal(models.Model):
    title = models.CharField(max_length=500, null=True, blank=False)
    journal_name = models.CharField(max_length=100, null=True)
    abstract = models.TextField(null=True)
    status = models.IntegerField(choices=PAPER_STATUS, default=1, null=True)
    journal_type = models.IntegerField(choices=PAPER_TYPE, default=1, null=True)
    # writer = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, related_name='journals', default=get_default_user)
    writer = models.ForeignKey(Member, on_delete=models.DO_NOTHING, related_name='journals', default=get_default_user)
    write_date = models.DateTimeField(default=timezone.now, null=True)
    update_date = models.DateTimeField(default=timezone.now, null=True)
    visit = models.IntegerField(default=1)
    ack = models.CharField(max_length=100, null=True, blank=True)
    pub_year = models.CharField(max_length=10, blank=True, null=True)
    extras = models.CharField(max_length=50, null=True, blank=True)
    all_authors = models.CharField(max_length=200, null=True, blank=True)
    file = models.FileField(upload_to='journals/', null=True, blank=True)


class Conference(models.Model):
    title = models.CharField(max_length=500, null=True, blank=False)
    conference_name = models.CharField(max_length=100, null=True)
    abstract = models.TextField(null=True)
    status = models.IntegerField(choices=PAPER_STATUS, default=1, null=True)
    conference_type = models.IntegerField(choices=PAPER_TYPE, default=1, null=True)
    # # writer = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING, related_name='journals', default=get_default_user)
    writer = models.ForeignKey(Member, on_delete=models.DO_NOTHING, related_name='conferences', default=get_default_user)
    write_date = models.DateTimeField(default=timezone.now, null=True)
    update_date = models.DateTimeField(default=timezone.now, null=True)
    visit = models.IntegerField(default=1)
    ack = models.CharField(max_length=100, null=True, blank=True)
    pub_year = models.CharField(max_length=10, blank=True, null=True)
    extras = models.CharField(max_length=50, null=True, blank=True)
    all_authors = models.CharField(max_length=200, null=True, blank=True)
    file = models.FileField(upload_to='conference/', null=True, blank=True)