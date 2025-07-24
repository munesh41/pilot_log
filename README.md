# Pilotlog Assignment

This Django application demonstrates a clean, modular solution to importing JSON data from file provided and exporting to csv the pilot logbook data provided .

Implemented  Features Include

- **A Reusable JSON Importer** for thelogbook data
- **A Reusable CSV Exporter** that matches provided template
- **Normalized, DRY Django ORM Models**
- **Management Commands** for CLI integration
- **Clean, Extensible Architecture** ready for production or extension

##  Setup Project

```bash
git clone https://github.com/munesh41/pilot_log.git to local folder
create a virtual environment: python -m venv venv
Activate the virtual environment: source venv/bin/activate
Navigate to right directory: cd pilotlog
Install required libraries: pip install -r requirements.txt
Do migrations: python manage.py migrate

```
To import JSON data run this command: python manage.py import_json_data

To export the imported and saved data to a csv file  run this command: python manage.py export_data_csv

