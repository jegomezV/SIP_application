import unittest
from applications.sip_application.models.classroom_model import Classrooms

class TestClassrooms(unittest.TestCase):
    def test_init(self):
        # Arrange
        name = "Test Classroom"

        # Act
        classroom = Classrooms(name)

        # Assert
        self.assertEqual(classroom.name, name)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestClassrooms)
    unittest.TextTestRunner().run(suite)
