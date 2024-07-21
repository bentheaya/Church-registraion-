from django.contrib import admin
from django.urls import include, path
from registration import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/login/', views.custom_admin_login, name='custom_admin_login'),
    path('', include('registration.urls')),
]
