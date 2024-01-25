# Gyan Machine Test

## Api App
This Django project consists of two distinct apps: API and Authentication.

- GET `/api/Students`: Retrieves a comprehensive list of students.
- POST `/api/Students`: Adds a new student. Parameters: 'name', 'address', 'phone', 'school'.
- PUT `/api/Students`: Modifies existing student details. Include relevant parameters.
- DELETE `/api/Students`: Deletes a specific student.

### Schools

- Additional information about the School model and related functionalities.

### Gallery

- Allows image uploads in JPG and PNG formats.
- Images are automatically converted to WebP format for display within the Django admin.

## Authentication App

### Endpoints

#### Registration

- POST `/Registration`: User registration.

#### Login

- POST `/Login`: User login.

## Setup

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies: `pip install -r requirements.txt`.
4. Apply migrations: `python manage.py migrate`.
5. Run the development server: `python manage.py runserver`.

