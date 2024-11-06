from django.db import models

class Server(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20)  # e.g., 'up', 'down'
    last_checked = models.DateTimeField(auto_now=True)
    severity = models.CharField(max_length=20)  # e.g., 'low', 'medium', 'high'

    def __str__(self):
        return self.name
