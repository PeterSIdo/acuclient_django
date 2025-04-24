from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name="clients/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('client/add/', views.add_client, name='add_client'),
    path('client/<str:client_id>/edit/', views.edit_client, name='edit_client'),
    path('client/<str:client_id>/delete/', views.delete_client, name='delete_client'),
    path('client/<str:client_id>/view/', views.view_client, name='view_client'),
]