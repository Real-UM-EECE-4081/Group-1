from django.db import models

class Notification(models.Model):
    message = models.TextField()
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message
