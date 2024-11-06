from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),        # URL for dashboard view
    path('', views.server_status_view, name='server_status')  # URL for server status JSON data
]
