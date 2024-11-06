from django.shortcuts import render
from .models import Service
from faker import Faker
import random
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone

# Initialize Faker to create fake data for services (Testing Purpose)
fake = Faker()
#print(fake.url())

# Create your views here.

# Creating the fake data for Testing purpose 
def create_fake_services():
    # It going to create 10 fake services 
    for _ in range(10):
        # Generating a fake name for the services
        service_name = fake.company()
        # Generates a fake url for the service
        service_url = fake.url()
        print(f"Generated URL: {service_url}")  # Debug line
        # Generates a random token for the auth.
        auth_token = fake.sha1()
        # It choose randolmy if the service is OK or DOWN
        status = random.choice(['OK', 'DOWN'])
        # This creates a new service entry in the data base
        Service.objects.create(name=service_name,
                                url=service_url,
                                auth_token=auth_token,
                                status=status,
                                last_checked=timezone.now(),
        )



# This will check the status of each service and it will update the status of the service either 'OK' or "DOWN" in the database
def update_service_status():
    services = Service.objects.all() # Getting all of the services in the database
    

    for service in services:
        #print(f"Checking status for service: {service.name} - URL: {service.url}")

        headers = {} #Initialize headers for the request
        if service.auth_token:
            headers['Authorization'] = f'Bearer {service.auth_token}'
            #print(f"Authorization token used: {service.auth_token}")

        try:
            #print(f"Making request to: {service.url}")
            # Request to get the service url 
            response = requests.get(service.url,headers=headers,timeout=10)

            # If the reponse status = 200 then the service is ok 
            if response.status_code == 200:
                service.status = 'OK'
                #print(f"Service {service.name} is OK (Status Code: 200)")

            # Otherwise, it is down 
            else:
                service.status = 'DOWN'
                #print(f"Service {service.name} is DOWN (Status Code: {response.status_code})")

        except requests.RequestException as e:
            #print(f"Error checking {service.url}: {e}")
            service.status = 'DOWN'

        # Changing the time check and saving it to the database
        service.last_checked = timezone.now()
        service.save()
        #print(f"Updated service {service.name} - Status: {service.status} - Last Checked: {service.last_checked}")



# This will check the health of the service every x minutes
def start_health_check_scheduler():
    schedular = BackgroundScheduler()
    # For testing purpose, the interval is set to every 10 seconds
    schedular.add_job(update_service_status,'interval',seconds=10) # Every 10 seconds
    schedular.start()


# This will fetch all of the services from teh Service Model and pass them to the status.html
def health_check_view(request):
    services = Service.objects.all()
    return render(request,'health_check/status.html',{'services':services})
