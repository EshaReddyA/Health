created a new GitHub repository and named it Health
Created a virtual environment
python -m venv .env 
Activated the virtual environment 
.env\Scripts\activate
installed Django and checked the version
pip install Django
django-admin --version
create a new Django project and named it Health.
django-admin startproject Health 
created an app called Patients
python manage.py startapp Patients
view functions in the file views.py inside the Patients app
urls.py file inside the Patients app and added URLs
linked the Patients app URLs to the main project’s urls.py
Used the command python manage.py migrate to apply database migrations
   
# Health