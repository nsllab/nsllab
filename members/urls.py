from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    # other paths...
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('professors/', views.professors_list, name="professors_list"),
    path('post_docs/', views.post_docs_list, name="post_docs_list"),
    path('post_docs/<int:pk>', views.PostDoctDetailView.as_view(), name="post_docs_detail"),
]
