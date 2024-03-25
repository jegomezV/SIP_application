from typing import Optional, List, Dict
from gluon import HTTP

class StudentRepository:
    """
    StudentRepository is a class that provides methods
    to interact with the 'students' collection in the database.
    """

    def __init__(self, db):
        """
        Initializes a new instance of the StudentRepository class.

        """
        self.db = db

    def get_all_students(self):
        """
        Retrieves all students from the 'students' collection.

        :return: A list of dictionaries representing the students.
        """
        return self.db(self.db.students).select()

    def get_student_by_id(self, student_id: int) -> Optional[dict]:
        """
        Retrieves a student by its ID from the 'students' collection.

        :param student_id: An integer representing the student's ID.
        :return: A dictionary representing the student if found, None otherwise.
        :raises ValueError: If no student is found with the provided ID.
        """
        student = self.db.students(student_id)
        if not student:
            raise ValueError(f"No student found with id {student_id}")
        return student

    def create_student_repo(self, student: Dict[str, str]):
        """
        Creates a new student in the 'students' collection.

        :param student: A dictionary representing the student.
        :return: A dictionary representing the created student.
        :raises ValueError: If either 'name' or 'email'
        is empty or if the email already exists in the database.
        """
        
        print("JOIN REPOOOOOO")
        print(student)
        if not student['name'] or not student['email']:
            print("Name or email is empty")
            raise ValueError("Both name and email are required")

        # Check if a student with this email already exists in the database
        if self.student_exists(student['email']):
            print("YA EXISTE")
            raise HTTP(400, "A student with this email already exists")

        print("sale del repo")
        return self.db.students.insert(name=student['name'], email=student['email'])

    def update_student(self, student_id: int, name: str, email: str) -> Optional[dict]:
        """
        Updates a student in the 'students' collection.

        :param student_id: An integer representing the student's ID.
        :param name: A string representing the student's name.
        :param email: A string representing the student's email.
        :return: A dictionary representing the updated student if successful, None otherwise.
        :raises ValueError: If either 'name' or 'email' is empty.
        """
        if not name or not email:
            raise ValueError("Both name and email are required")
        return self.db.students(student_id).update_record(name=name, email=email)

    def delete_student(self, student_id: int) -> bool:
        """
        Deletes a student from the 'students' collection.

        :param student_id: An integer representing the student's ID.
        :return: True if the deletion was successful, False otherwise.
        """
        return self.db.students(student_id).delete_record()

    def student_exists(self, email: str) -> bool:
        """
        Checks if a student with the given email exists in the 'students' collection.

        :param email: A string representing the student's email.
        :return: True if a student with the given email exists, False otherwise.
        """
        query = self.db.students.email == email
        results = self.db(query).select()
        return len(results) > 0
