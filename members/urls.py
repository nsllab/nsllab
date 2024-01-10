from django.urls import path
from . import views

app_name = 'members'

urlpatterns = [
    # other paths...
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('professors/', views.professors_list, name="professors_list"),

    path('post_docs/', views.PostDocsListView.as_view(), name="post_docs_list"),
    path('post_docs/<int:pk>', views.PostDoctDetailView.as_view(), name="post_docs_detail"),

    path('full_time/', views.FullTimeListView.as_view(), name="full_time_list"),
    path('full_time/<int:pk>', views.FullTimeDetailView.as_view(), name="full_time_detail"),

    path('profile/update/', views.MemberUpdateView.as_view(), name='update_profile'),
    path('<int:pk>/password/',views. MemberChangePasswordView.as_view(), name='change_password'),
]
