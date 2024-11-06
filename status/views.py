from django.shortcuts import render
from django.http import JsonResponse
from .models import Server

def dashboard(request):
    # Fetch all server data
    servers = Server.objects.all()
    # Pass the servers data to the template
    return render(request, 'status/dashboard.html', {'servers': servers})

def server_status_view(request):
    servers = Server.objects.all()
    data = [{"name": server.name, "status": server.status, "severity": server.severity} for server in servers]
    return JsonResponse(data, safe=False)

