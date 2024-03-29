"""
This module contains the controller for attendance operations. 
It includes functions for showing, creating and updating attendance records.
"""

from gluon import HTTP
from gluon import current
from http import HTTPStatus
from applications.sip_application.modules.repository.student_repo import StudentRepository
from applications.sip_application.modules.renderer.attendance_renderer import Renderer
from applications.sip_application.modules.repository.attendance_repo import AttendanceRepository

# Decoments to test
# db = current.globalenv['db']


def show_attendance():
    """
    This function retrieves all students, subjects, and classrooms from the database.
    It then prepares the data for the Renderer and returns the rendered attendance table.
    """
    # Create an instance of StudentRepository
    student_repository = StudentRepository(db)

    # Get the data of the students, subjects, and classrooms from the database.
    students = student_repository.get_all_students()

    # Get all the subjects directly from the database
    subjects = db(db.subjects).select()

    # Get all the classrooms directly from the database
    classrooms = db(db.classrooms).select()

    # Prepare the data for the Renderer.
    data = [
        {
            "student": {"id": student.id, "name": student.name},
            "subject": {"id": subject.id, "name": subject.name},
            "classroom": {"id": room.id, "name": room.name},
        }
        for student in students
        for subject in subjects
        for room in classrooms
    ]

    renderer = Renderer()
    attendance_table = renderer.render_attendance(data)

    return dict(attendance_table=attendance_table)

# Add request, response how parameters to test


def create_attendance():
    """
    This function creates an attendance record. It gets the attendance status, student id, 
    subject id, classroom id, and attendance date from the POST data. It checks if all required 
    data is present, converts the attendance date to a datetime object, and then stores the 
    attendance data in the database.
    """
    # Get the attendance status, student id, subject id, classroom id,
    # and attendance date from the POST data
    attendance_status = request.vars.attendance_status
    student_id = request.vars.student_id[0] if isinstance(
        request.vars.student_id, list) else request.vars.student_id
    subject_id = request.vars.subject_id[0] if isinstance(
        request.vars.subject_id, list) else request.vars.subject_id
    classroom_id = request.vars.classroom_id[0] if isinstance(
        request.vars.classroom_id, list) else request.vars.classroom_id

    # Convert IDs to integers
    student_id = int(student_id)
    subject_id = int(subject_id)
    classroom_id = int(classroom_id)

    # Check if all required data is present
    if not all([attendance_status, student_id, subject_id, classroom_id]):
        return response.json(dict(success=False, message="Missing required data"))

    # Instantiate AttendanceRepository
    attendance_repo = AttendanceRepository(db)

    # Call update_attendance_repo method
    attendance_repo.update_attendance_repo(
        student_id,
        classroom_id,
        subject_id,
        attendance_status
    )

    return response.json(dict(success=True, message="Attendance data successfully stored"))
