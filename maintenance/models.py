from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import User

class MaintenanceNotification(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.start_time} - {self.end_time})"
    
    def save(self, *args, **kwargs):
        super(MaintenanceNotification, self).save(*args, **kwargs)  # Save the object first
        
        # Send email notifications to all users after saving the maintenance notification
        self.send_maintenance_notification()

    def send_maintenance_notification(self):
        users = User.objects.all()
        for user in users:
            send_mail(
                f"Maintenance Notification: {self.title}",
                f"Hello {user.username},\n\nWe wanted to let you know that {self.description}\n\nMaintenance will start at {self.start_time} and end at {self.end_time}.\n\nThank you for your understanding.",
                'admin@yourwebsite.com',  # Use your actual admin email
                [user.email],
                fail_silently=False,
            )
