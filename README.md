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

TEMPLATE CREATION
Created a folder inside the app named templates
Created an HTML file: home.html
Created a view function in views.py
Added a URL path in urls.py

FIELDS CREATION in models.py
Opened Patients/models.py and created modelS
ran this python manage.py makemigrations analyzes the changes made to the models.py file and generates migration files
ran this python manage.py migrate  creates database tables based on the models in models.py


