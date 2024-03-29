from typing import Dict, Any
from applications.sip_application.modules.factory.student_fact import StudentFactory
from applications.sip_application.modules.repository.student_repo import StudentRepository


def create_student(student_data: Dict[str, str], db: Any):
    """
    Create a student object using the factory and insert the student data into the database.

    Args:
        student_data (Dict[str, str]):
        A dictionary containing student data.
        It should have 'name' and 'email' keys.
        db (Any): Database connection object.

    Returns:
        Student: An instance of the Student class.
    """

    try:
        print("SERVICEEEEE")
        student_repository = StudentRepository(db)
        student_factory = StudentFactory()
        student = student_factory.create_student(
            student_data['name'], student_data['email'])
        print("go repo")
        student_repository.create_student_repo(student)
        return student

    except Exception as e:
        raise Exception("Error service " + str(e)) from e


def get_all_students(db: Any):
    """
    Get all students from the database.

    Args:
        db (Any): Database connection object.

    Returns:
        List[Student]: A list of Student instances.
    """

    try:
        student_repository = StudentRepository(db)
        students = student_repository.get_all_students()
        return students

    except Exception as e:
        raise Exception("Error service " + str(e)) from e
