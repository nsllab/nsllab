from django.urls import path

from . import views

app_name = 'publications'

urlpatterns = [
    path('journals', views.journals, name='journals'),
    path('journals/create', views.JournalCreateView.as_view(), name='journal_create'),
]