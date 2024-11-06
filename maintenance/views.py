from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import MaintenanceNotification

# Admin check
def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def create_maintenance(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']

        maintenance = MaintenanceNotification(
            title=title,
            description=description,
            start_time=start_time,
            end_time=end_time
        )
        maintenance.save()

        # Send email notification
        send_maintenance_notification(maintenance)

        return redirect('maintenance:list')

    return render(request, 'maintenance/create.html')

@user_passes_test(is_admin)
def maintenance_list(request):
    notifications = MaintenanceNotification.objects.all()
    return render(request, 'maintenance/list.html', {'notifications': notifications})

def send_maintenance_notification(maintenance):
    # Get the user emails (you can adjust this query as needed)
    users = User.objects.all()

    for user in users:
        send_mail(
            f"Maintenance Notification: {maintenance.title}",
            f"Hello {user.username},\n\nWe wanted to let you know that {maintenance.description}\n\nMaintenance will start at {maintenance.start_time} and end at {maintenance.end_time}.\n\nThank you for your understanding.",
            'admin@yourwebsite.com',  # Replace with a valid email address
            [user.email],
            fail_silently=False,
        )
