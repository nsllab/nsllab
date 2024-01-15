from django.urls import path
from . import views

app_name = "works"

urlpatterns = [
    path('', views.weekly_reports, name='weekly_reports'),
    path('create', views.WeeklyReportCreateView.as_view(), name='create_report'),
    path('<int:pk>/details', views.WeeklyReportDetailView.as_view(), name='details'),
    path('<int:pk>/update', views.WeeklyReportUpdateView.as_view(), name='update'),
]