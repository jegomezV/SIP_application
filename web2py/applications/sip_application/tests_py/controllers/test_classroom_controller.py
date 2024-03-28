import unittest
from gluon.globals import Request
from applications.sip_application.controllers.classrooms import classrooms_view

# Renombrar la base de datos de prueba para que las funciones la usen en lugar de la base de datos real
db = test_db

class TestClassroomController(unittest.TestCase):
    def setUp(self):
        # Define your table
        if 'classrooms' not in db.tables:
            db.define_table('classrooms', Field('name'))
        db.classrooms.insert(name='Classroom 1')
        db.classrooms.insert(name='Classroom 2')
        db.classrooms.insert(name='Classroom 3')
        db.commit()

    def test_classrooms_view(self):
        # Act
        result = classrooms_view()

        # Assert
        self.assertIsInstance(result, dict)
        self.assertIn('grid', result)
        self.assertIsNotNone(result['grid'])
        self.assertIsInstance(result['grid'], DIV)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestClassroomController)
    unittest.TextTestRunner(verbosity=2).run(suite)