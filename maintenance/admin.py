from django.contrib import admin
from .models import MaintenanceNotification

# Register the model so it appears in the admin interface
@admin.register(MaintenanceNotification)
class MaintenanceNotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('start_time', 'end_time')
