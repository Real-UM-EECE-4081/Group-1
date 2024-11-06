from django.urls import path
from . import views

urlpatterns = [
    path('status/', views.dashboard, name='status'),        # URL for dashboard view
    path('', views.server_status_view, name='server_status')  # URL for server status JSON data
]
