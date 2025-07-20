from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('farmer/register/', views.farmer_register, name='farmer_register'),
    path('register/', views.farmer_register, name='farmer_register'),
    path('register/self/', views.farmer_register,
         {'self_registration': True}, name='farmer_register_self'),
    path('officer/create/', views.create_officer, name='create_officer'),
    path('farmer/approve/<int:user_id>/',
         views.approve_farmer, name='approve_farmer'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # or if using your custom view:
    path('accounts/login/', views.login_view, name='login'),






]
