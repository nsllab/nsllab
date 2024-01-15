from django.db import models
from django.utils import timezone
from datetime import timedelta

from django.contrib.auth import get_user_model

from members.models import Member

def get_default_user():
    return get_user_model().objects.get(username='admin').id

def default_from_date():
    return timezone.now() + timedelta(days=(0 - timezone.now().weekday()) % 7)

def default_till_date():
    return timezone.now() + timedelta(days=(4 - timezone.now().weekday()) % 7 + 1)


class WeeklyReport(models.Model):
    fr_dt = models.DateTimeField("From Date", default=timezone.now)
    to_dt = models.DateTimeField("Till", default=default_from_date)
    paper_progress = models.TextField("Paper Progress")
    paper_prog_percent = models.IntegerField("Paper Progress Percent")
    paper_last_wk = models.TextField("Last Week Paper")
    paper_this_wk = models.TextField("This Week Paper")
    project_progress = models.TextField("Project Progress")
    project_prog_percent = models.IntegerField("Paper Progress Percent")
    project_last_wk = models.TextField("Last Week Project")
    project_this_wk = models.TextField("Last Week Project")
    mnth_gls = models.TextField("Monthly Goals")
    annl_gls = models.TextField("Annual Goals")
    user = models.CharField(null=True, blank=True)
    writer = models.ForeignKey(Member, on_delete=models.DO_NOTHING, related_name='reports', default=get_default_user)
    is_post_doc = models.BooleanField("Post Doc?",default=False)
    # pass