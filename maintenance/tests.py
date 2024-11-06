from django.core import mail
from django.test import TestCase
from django.contrib.auth.models import User
from maintenance.models import MaintenanceNotification

class MaintenanceNotificationTestCase(TestCase):

    def setUp(self):
        # Create a superuser
        self.superuser = User.objects.create_superuser('admin', 'admin@example.com', 'password')

        # Create a regular user
        self.user = User.objects.create_user('testuser', 'testuser@example.com', 'password')

    def test_send_maintenance_notification_email(self):
        # Create a maintenance notification (this would trigger the email sending)
        maintenance = MaintenanceNotification.objects.create(
            title='Scheduled Maintenance',
            description='System update and bug fixes.',
            start_time='2024-11-01 10:00:00',
            end_time='2024-11-01 12:00:00'
        )

        # Now we want to check if emails were sent to all users
        # Send email notifications (make sure this function is being called in the view)
        maintenance.send_maintenance_notification(maintenance)

        # Check if an email was sent
        self.assertEqual(len(mail.outbox), 1)

        # Check if the email is being sent to the correct recipient
        self.assertEqual(mail.outbox[0].to, ['testuser@example.com'])

        # Optionally, you can also check the subject and content of the email
        self.assertIn('Scheduled Maintenance', mail.outbox[0].subject)
        self.assertIn('System update and bug fixes.', mail.outbox[0].body)
