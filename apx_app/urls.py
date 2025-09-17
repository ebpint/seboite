# apx_app/urls.py

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'apx_app'

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('server/', views.ServerView.as_view(), name='server'),
    path('server/listas-negras/', views.ListasNegrasView.as_view(), name='listas_negras'),
    path('server/operaciones/', views.OperacionesView.as_view(), name='operaciones'),
    path('kyc/', views.KYCView.as_view(), name='kyc'),
    path('cliente/', views.ClienteView.as_view(), name='cliente'),
]