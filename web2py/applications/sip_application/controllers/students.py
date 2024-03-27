# Create an instance of StudentRepository
from gluon.http import HTTP
from http import HTTPStatus
from gluon import current
from applications.sip_application.modules.services.business_logic.student_service import create_student

def register_student(request):
    """Registers a new student."""
    db = current.globalenv['db']
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
            raise HTTP(HTTPStatus.BAD_REQUEST.value, 'Name is required')
        if 'email' not in student_data or not student_data['email']:
            raise HTTP(HTTPStatus.BAD_REQUEST.value, 'Email is required')

        # Create student and save in the database
        create_student(student_data, db)

        return dict(success=True)
    except Exception as e:
        print("Original error: ", e)
        raise HTTP(400, "controller error " + str(e)) from e


def student_view():
    """
    This function retrieves all students, subjects, and classrooms from the database.
    It then prepares the data for the Renderer and returns the rendered attendance table.
    """

    return dict()