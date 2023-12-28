import json

def convert_to_django_compatible(json_data, app_name, model_name):
    django_data = []
    for entry in json_data['rows']:
        model_entry = {
            "model": f"{app_name}.{model_name}",
            "pk": entry['id'],
            "fields": {
                "title": entry['title'],
                "journal_name": entry['journal_name'],
                "status": entry['status'],
                "journal_type": entry['journal_type'],
                "write_date": entry['write_date'],
                "update_date": entry['update_date'],
                "visit": entry['visit'],
                "ack": entry['ack'],
                "pub_year": entry['pub_year'],
                "extras": entry['extras'],
                "all_authors": entry['all_authors'],
            }
        }
        django_data.append(model_entry)

    return django_data

# Load the original JSON data
with open('./data.json', 'r') as file:
    original_json_data = json.load(file)

# Specify your Django app and model names
app_name = 'publications'
model_name = 'journal'

# Convert to Django-compatible format
django_compatible_data = convert_to_django_compatible(original_json_data, app_name, model_name)

# Save the converted data to a new file
with open('./data_.json', 'w') as file:
    json.dump(django_compatible_data, file, indent=2)
