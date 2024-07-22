from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('logout/', views.custom_logout, name='logout'),
    path('delete_member/<int:member_id>/', views.delete_member, name='delete_member'),
    path('custom_admin/login/', views.custom_admin_login, name='custom_admin_login'),
    path('custom_admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('custom_admin/create_admin/', views.create_admin, name='create_admin'),
    path('member_details/<int:member_id>/', views.member_details, name='member_details'),
]
