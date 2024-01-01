# Interview Management Application

Hello there! 👋 Welcome to the Interview Management Application, a project I've developed as part of the Two-a-Day Coding Challenge for the Junior Python Developer position. Below, you'll find everything you need to know to understand, set up, and showcase this project.

## Project Overview

The Interview Management Application is a Django-based web application designed to streamline the process of managing candidates during the interview cycle. With a focus on simplicity and functionality, this application allows users to create, view, edit, and delete candidate information, along with adding and managing notes related to each candidate.

## Features

- **User Authentication:**
  - Sign up: Create an account with a unique username and password.
  - Login: Log in securely to access the application.

- **Candidate Management:**
  - Create Candidates: Add new candidates with details such as name, contact information, and resume.
  - View Candidates: See a list of all candidates with basic information.
  - Edit Candidate Details: Modify candidate information as needed.

- **Notes Management:**
  - Add Notes to Candidates: Include notes related to interviews, assessments, or other relevant information.
  - View Notes: See all notes associated with a specific candidate.
  - Edit and Delete Notes: Modify existing notes or remove them as needed.

## Technical Details

- **Backend:**
  - Built with Django, a Python web framework.

- **Frontend:**
  - Simple HTML/CSS for a clean and straightforward user interface.

- **Database:**
  - SQLite for a lightweight and easy-to-use database solution.

- **User Authentication:**
  - Utilizes Django's built-in authentication system for user sign-up and login.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python (3.10 or higher)
- pip to install django
- Django (5.0 was used)

### Setting Up Locally

1. Clone the repository:

    ```bash
    git clone [https://WynandVStaden@bitbucket.org/interview-management-system/interview-management-system.git]
    cd interview_management
    ```

2. Run the development server:

    ```bash
    python manage.py runserver
    ```

3. Access the application in your browser at `http://127.0.0.1:8000/`.

### Database Setup (Optional)

#### 1. Delete the Database
rm db.sqlite3

#### 2. Rebuild the Database
python makemigrations
python migrate

#### 3. Create a Superuser
python manage.py createsuperuser

####s 4. Add Sample Data (Optional)
python manage.py add_sample_data


