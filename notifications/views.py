from django.shortcuts import render, redirect
from .models import Notification
from django.http import Http404

def home(request):
    # Fetch the unread notifications
    unread_notifications = Notification.objects.filter(is_read=False)
    return render(request, 'notifications/home.html', {'unread_notifications': unread_notifications})

def mark_as_read(request, notification_id):
    try:
        notification = Notification.objects.get(id=notification_id)
        notification.is_read = True
        notification.save()
        return redirect('home')
    except Notification.DoesNotExist:
        raise Http404("Notification not found")
