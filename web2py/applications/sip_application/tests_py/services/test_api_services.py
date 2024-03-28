import unittest
from unittest.mock import MagicMock, patch
from applications.sip_application.modules.services.business_logic.student_service import create_student, get_all_students

class TestStudentService(unittest.TestCase):
    def setUp(self):
        self.db_mock = MagicMock()

    def test_create_student(self):
        student_data = {'name': 'John Doe', 'email': 'john.doe@example.com'}
        student = create_student(student_data, self.db_mock)
        self.assertEqual(student['name'], student_data['name'])
        self.assertEqual(student['email'], student_data['email'])
        self.db_mock.assert_called_once()

    @patch('applications.sip_application.modules.services.business_logic.student_service.get_all_students')
    def test_get_all_students(self, get_all_students_mock):
        get_all_students_mock.return_value = [{'name': 'John Doe', 'email': 'john.doe@example.com'}]
        students = get_all_students_mock(self.db_mock)
        get_all_students_mock.assert_called_once()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStudentService)
    unittest.TextTestRunner().run(suite)
