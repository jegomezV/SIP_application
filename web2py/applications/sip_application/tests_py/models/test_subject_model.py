import unittest
from applications.sip_application.models.subjects_model import Subjects

class TestSubjects(unittest.TestCase):
    def test_init(self):
        # Arrange
        name = "Test Subject"

        # Act
        subject = Subjects(name)

        # Assert
        self.assertEqual(subject.name, name)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSubjects)
    unittest.TextTestRunner().run(suite)