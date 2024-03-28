import unittest
from unittest.mock import MagicMock
from applications.sip_application.modules.repository.student_repo import StudentRepository

class TestStudentRepository(unittest.TestCase):
    def setUp(self):
        self.db_mock = MagicMock()
        self.student_repo = StudentRepository(self.db_mock)

    def test_get_all_students(self):
        self.student_repo.get_all_students()
        self.db_mock.assert_called_once()

    def test_get_student_by_id(self):
        self.student_repo.get_student_by_id(1)
        self.db_mock.students.assert_called_once_with(1)

    def test_create_student_repo(self):
        student = {'name': 'John Doe', 'email': 'john.doe@example.com'}
        self.student_repo.create_student_repo(student)
        self.db_mock.students.insert.assert_called_once_with(name=student['name'], email=student['email'])

    def test_update_student(self):
        self.student_repo.update_student(1, 'John Doe', 'john.doe@example.com')
        self.db_mock.students.assert_called_once_with(1)
        self.db_mock.students().update_record.assert_called_once_with(name='John Doe', email='john.doe@example.com')

    def test_delete_student(self):
        self.student_repo.delete_student(1)
        self.db_mock.students.assert_called_once_with(1)
        self.db_mock.students().delete_record.assert_called_once()

    def test_student_exists(self):
        self.student_repo.student_exists('john.doe@example.com')
        self.db_mock.assert_called_once_with(self.db_mock.students.email == 'john.doe@example.com')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStudentRepository)
    unittest.TextTestRunner().run(suite)
