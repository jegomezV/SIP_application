import unittest
from gluon.globals import Request
from applications.sip_application.controllers.subjects import subjects_view
from gluon.html import DIV

# Renombrar la base de datos de prueba para que las funciones la usen en lugar de la base de datos real
db = test_db

class TestSubjectController(unittest.TestCase):
    def setUp(self):
        # Define your table
        if 'subjects' not in db.tables:
            db.define_table('subjects', Field('name'))
        db.subjects.insert(name='Subject 1')
        db.subjects.insert(name='Subject 2')
        db.subjects.insert(name='Subject 3')
        db.commit()

    def test_subjects_view(self):
        # Act
        result = subjects_view()

        # Assert
        self.assertIsInstance(result, dict)
        self.assertIn('grid', result)
        self.assertIsNotNone(result['grid'])
        self.assertIsInstance(result['grid'], DIV)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSubjectController)
    unittest.TextTestRunner(verbosity=2).run(suite)
