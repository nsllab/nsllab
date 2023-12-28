# import necessary modules
import json
 # replace with your actual model
from django.utils import timezone
import os

from django.core.wsgi import get_wsgi_application

# set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")  # replace with your actual project settings module

# initialize the Django application
app = get_wsgi_application()

from django.conf import settings
from publications.models import Journal 

# specify the path to your JSON file
json_file_path = './data_.json'  # replace with the actual path

def load_data_from_json():
    with open(json_file_path, 'r') as file:
        data = json.load(file)

        for entry in data:
            # Modify the entry if needed, e.g., setting timestamps
            

            # Create a model instance and save it to the database
            Journal.objects.create(**entry['fields'])

if __name__ == '__main__':
    load_data_from_json()
