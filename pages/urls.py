from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('serendipity/', views.serendipity, name='serendipity'),
    path('serendipity/<int:pk>/update', views.serendipity_update, name='serendipity_update'),
    path('serendipity/create', views.serendipity_create, name='serendipity_create'),
]