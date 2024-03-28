import unittest
from applications.sip_application.controllers.students import register_student
from gluon.storage import Storage

class TestStudentsController(unittest.TestCase):
    def setUp(self):
        # Create a new request object
        self.request = Storage()
        self.request.env = Storage()
        self.request.env.request_method = 'POST'

    def test_register_student(self):
        # Arrange
        self.request.vars = Storage()
        self.request.vars.name = 'Test Student'
        self.request.vars.email = 'test2@student.com'

        # Act
        result = register_student(self.request)

        # Assert
        self.assertTrue(result['success'])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStudentsController)
    unittest.TextTestRunner().run(suite)