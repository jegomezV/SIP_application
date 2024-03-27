"""
This module contains the controller for attendance operations. 
It includes functions for showing, creating and updating attendance records.
"""

from http import HTTPStatus
from gluon import HTTP
from applications.sip_application.modules.repository.student_repo import StudentRepository
from applications.sip_application.modules.renderer.attendance_renderer import Renderer
from applications.sip_application.modules.repository.attendance_repo import AttendanceRepository

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
    data = []
    for student in students:
        for subject in subjects:
            for room in classrooms:
                data.append({
                    "student": {"id": student.id, "name": student.name},
                    "subject": {"id": subject.id, "name": subject.name},
                    "classroom": {"id": room.id, "name": room.name},
                })

    renderer = Renderer()
    attendance_table = renderer.render_attendance(data)

    return dict(attendance_table=attendance_table)

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
    student_id = request.vars.student_id[0] if isinstance(request.vars.student_id, list) else request.vars.student_id
    subject_id = request.vars.subject_id[0] if isinstance(request.vars.subject_id, list) else request.vars.subject_id
    classroom_id = request.vars.classroom_id[0] if isinstance(request.vars.classroom_id, list) else request.vars.classroom_id

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

def update_attendance():
    """
    This function updates an attendance record. It checks if the request method is POST, 
    extracts the attendance data from the request vars, validates the attendance data, 
    and then updates the attendance data in the database.
    """
    try:
        if request.env.request_method != 'POST':
            raise HTTP(HTTPStatus.METHOD_NOT_ALLOWED.value)

        # Extract attendance data from the request vars
        attendance_data = request.vars

        # Check if attendance_data is None or empty
        if not attendance_data:
            raise HTTP(HTTPStatus.BAD_REQUEST.value, 'Attendance data not provided or empty')

        # Validate attendance data
        if 'student_id' not in attendance_data or not attendance_data['student_id']:
            raise HTTP(HTTPStatus.BAD_REQUEST.value, 'Student ID is required')
        if 'subject_id' not in attendance_data or not attendance_data['subject_id']:
            raise HTTP(HTTPStatus.BAD_REQUEST.value, 'Subject ID is required')
        if 'classroom_id' not in attendance_data or not attendance_data['classroom_id']:
            raise HTTP(HTTPStatus.BAD_REQUEST.value, 'Classroom ID is required')
        if 'attendance' not in attendance_data or not attendance_data['attendance']:
            raise HTTP(HTTPStatus.BAD_REQUEST.value, 'Attendance status is required')

        # Create an instance of AttendanceRepository
        attendance_repository = AttendanceRepository(db)

        # Update the attendance record in the database
        success = attendance_repository.update_attendance_repo(
            db, 
            attendance_data['student_id'], 
            attendance_data['subject_id'], 
            attendance_data['classroom_id'], 
            attendance_data['attendance']
        )

        # Return success status as JSON
        response.json = dict(success=success)
    except Exception as e:
        raise HTTP(HTTPStatus.BAD_REQUEST.value, str(e)) from e