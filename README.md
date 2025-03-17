# schoolPro - School Management System

## Overview
schoolPro is a backend system designed to streamline school management processes.
Built with Django and MySQL, it provides essential functionalities for managing students, courses, enrollments, and manual fee payments.

## Features
- **Student Management**: CRUD operations for student records.
- **Course Management**: Add, update, and remove courses.
- **Student-Course Enrollment**: Manage student registrations for courses.
- **Manual Fee Payments**: Track and process student fee payments manually.

## Technologies Used
- **Backend**: Django (Python)
- **Database**: MySQL
- **API Framework**: Django REST Framework (DRF)

## Installation
### Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- MySQL
- pip & virtualenv

### Setup Instructions
1. Clone the repository:
   git clone https://github.com/Collins-Okyere/schoolPro.git
   cd schoolPro
2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. Install dependencies:
   pip install
<!-- 4. Configure the database in `settings.py`:python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': '',
           'USER': '',
           'PASSWORD': '',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   } -->
5. Apply database migrations:
   python manage.py migrate
6. Create a superuser (optional for admin access):
   python manage.py createsuperuser
7. Run the development server:
   python manage.py runserver

## API Endpoints
- **Students**: `/api/students/`
- **Courses**: `/api/courses/`
- **Enrollments**: `/api/enrollments/`
- **Payments**: `/api/payments/`

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License.

## Contact
For inquiries or support, reach out at: [cagyeiofficail@gmail.com]

