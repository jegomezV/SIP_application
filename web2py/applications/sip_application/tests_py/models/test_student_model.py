import unittest
from applications.sip_application.models.student_model import Student

class TestStudent(unittest.TestCase):
    def test_student_creation(self):
        name = "John Doe"
        email = "john.doe@example.com"
        student = Student(name, email)
        self.assertEqual(student.name, name)
        self.assertEqual(student.email, email)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStudent)
    unittest.TextTestRunner().run(suite)
