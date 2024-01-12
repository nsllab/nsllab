from django.urls import path

from . import views

app_name = 'publications'

urlpatterns = [
    path('journals', views.journals, name='journals'),
    path('journals/create', views.JournalCreateView.as_view(), name='journal_create'),
    path('journals/update/<int:pk>', views.JournalUpdateView.as_view(), name='journal_update'),
    path('journals/<int:pk>', views.JournalDetailView.as_view(), name='journal_detail'),
    path('conferences', views.conferences, name='conferences'),
    path('conferences/create', views.ConferenceCreateView.as_view(), name='conference_create'),
    path('conferences/update/<int:pk>', views.ConferenceUpdateView.as_view(), name='conference_update'),
    path('conferences/<int:pk>', views.ConferenceDetailView.as_view(), name='conference_detail'),
]