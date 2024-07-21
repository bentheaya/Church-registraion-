from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('custom_admin/login/', views.custom_admin_login, name='custom_admin_login'),
    path('custom_admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('custom_admin/create_admin/', views.create_admin, name='create_admin'),
]
