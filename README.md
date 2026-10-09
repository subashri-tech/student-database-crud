# Student Database CRUD API

## Project Overview
This project is a Student Database Management API developed using Python, FastAPI, and SQLite.

It helps manage student records through Create, Read, Update, and Delete (CRUD) operations. The SQLite database stores student information persistently.

## Technologies Used
- Python
- FastAPI
- SQLite
- Uvicorn

## Features
- Add new student records
- View all students
- Retrieve a student by ID
- Update student details
- Delete student records
- Validate email addresses
- Handle requests for students who do not exist

## Student Information
Each student record contains:
- ID
- Name
- Date of Birth
- Email
- Phone Number
- Course

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check whether the API is running |
| POST | `/students` | Create a student |
| GET | `/students` | Retrieve all students |
| GET | `/students/{student_id}` | Retrieve a student by ID |
| PUT | `/students/{student_id}` | Update student details |
| DELETE | `/students/{student_id}` | Delete a student |

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/subashri-tech/student-database-crud.git
```

### 2. Open the Project Folder

```bash
cd student-database-crud
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
uvicorn main:app --reload
```

## API Documentation

After starting the application, open the following URL in your browser:

http://127.0.0.1:8000/docs

The interactive Swagger documentation allows you to test the API endpoints.

## Database

SQLite is used to store student records. The database table is created automatically when the application initializes, if it does not already exist.

## Project Purpose

This project was developed to practice building REST APIs, implementing CRUD operations, validating input, and storing data using Python and SQLite.
