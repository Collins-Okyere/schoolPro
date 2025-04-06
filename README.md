# SchoolPro - School Management System

## Overview
SchoolPro is designed to streamline school management processes.
Built with Django and MySQL, it provides essential functionalities for managing students, courses and manual fee payments.

## Features
- Dashboard
- Student Management: CRUD operations for student records.
- Course Management: Add, update, and remove courses.
- Manual Fee Payments: Track and process student fee payments manually.

## Technologies Used
- Django (Python) + Tailwindcss
- Database: MySQL
- API Framework: Django REST Framework (DRF)

## Installation
### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- MySQL
- pip & virtualenv
- Tailwindcss:
   guide (https://django-tailwind.readthedocs.io/en/latest/installation.html)

### Setup Instructions
1. Clone the repository:
   git clone https://github.com/Collins-Okyere/schoolPro.git
   cd schoolPro

2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install dependencies:
   pip install -r requirements.txt

4. Configure the database in 'settings.py':python
   DATABASES = {
      'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': BASE_DIR / 'db.sqlite3',
      }
   }

5. Apply database migrations:
   python manage.py migrate

6. Create a superuser (optional for admin access):
   python manage.py createsuperuser

7. Run the development server:
   python manage.py runserver

## API Endpoints
- Dashboard: 'dashboard'
- Students: 'students/'
- Courses: 'courses/'
- Fees: 'fees/'


## Contact
For inquiries, reach out at: [cagyeiokyere@gmail.com]

