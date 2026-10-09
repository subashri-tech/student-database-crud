from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
import database

app = FastAPI(title="Student Database CRUD API")


class Student(BaseModel):
    name: str
    dob: str
    email: EmailStr
    phone: str
    course: str


@app.get("/")
def home():
    return {"message": "Student CRUD API is running"}


# CREATE - Add a new student
@app.post("/students")
def create_student(student: Student):
    cursor = database.connection.cursor()

    cursor.execute("""
        INSERT INTO students (name, dob, email, phone, course)
        VALUES (?, ?, ?, ?, ?)
    """, (
        student.name,
        student.dob,
        student.email,
        student.phone,
        student.course
    ))

    database.connection.commit()

    student_id = cursor.lastrowid

    return {
        "message": "Student created successfully",
        "id": student_id
    }


# READ - Get all students
@app.get("/students")
def get_students():
    cursor = database.connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    return [
        {
            "id": row[0],
            "name": row[1],
            "dob": row[2],
            "email": row[3],
            "phone": row[4],
            "course": row[5]
        }
        for row in students
    ]


# READ - Get one student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    cursor = database.connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "id": student[0],
        "name": student[1],
        "dob": student[2],
        "email": student[3],
        "phone": student[4],
        "course": student[5]
    }


# UPDATE - Update student details
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    cursor = database.connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    existing_student = cursor.fetchone()

    if existing_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    cursor.execute("""
        UPDATE students
        SET name = ?, dob = ?, email = ?, phone = ?, course = ?
        WHERE id = ?
    """, (
        student.name,
        student.dob,
        student.email,
        student.phone,
        student.course,
        student_id
    ))

    database.connection.commit()

    return {"message": "Student updated successfully"}


# DELETE - Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    cursor = database.connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    database.connection.commit()

    return {"message": "Student deleted successfully"}
