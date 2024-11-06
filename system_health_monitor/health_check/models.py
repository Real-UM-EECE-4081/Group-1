from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    auth_token = models.CharField(max_length=255,blank=True,null=True)
    status = models.CharField(max_length=10)
    last_checked = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return f"{self.name} - {self.status}"
    