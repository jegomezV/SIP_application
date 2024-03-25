from ...models.student_model import Student

class StudentFactory:
    """
    A factory class for creating students.

    Attributes:
        db: A database connection object.
    """
    def create_student(self, name: str, email: str) -> dict:
        """
        The function to create a student.

        Parameters:
            name (str): The name of the student.
            email (str): The email of the student.

        Returns:
            dict: A dictionary containing the name and email of the student.
        """

        print("FACTORYYYYYYY")
        # Here you can add any additional logic you need for creating a student
        student = Student(name, email)
        print(student.name)
        print(student.email)
        return {"name": student.name, "email": student.email}
