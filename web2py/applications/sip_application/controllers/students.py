# Create an instance of StudentRepository
from unittest.mock import MagicMock
from applications.sip_application.modules.services.business_logic import student_service

def register_student():
    """Registers a new student."""
    if request.env.request_method != 'POST':
        raise HTTP(HTTPStatus.METHOD_NOT_ALLOWED)

    try:
        # Print request details for debugging
        print('request.env:', request.env)

        # Extract student data from the request vars
        student_data = request.vars

        # Check if student_data is None
        if student_data is None:
            raise HTTP(HTTPStatus.BAD_REQUEST, 'Student data not provided')

        # Validate student data
        if 'name' not in student_data or not student_data['name']:
            raise HTTP(HTTPStatus.BAD_REQUEST, 'Name is required')
        if 'email' not in student_data or not student_data['email']:
            raise HTTP(HTTPStatus.BAD_REQUEST, 'Email is required')

        # Create student and save in the database
        student_service.create_student(student_data, db)

        return dict(success=True)
    except Exception as e:
        raise HTTP(400, "controller error " + str(e)) from e


def student_view():
    """
    This function retrieves all students, subjects, and classrooms from the database.
    It then prepares the data for the Renderer and returns the rendered attendance table.
    """

    return dict()
