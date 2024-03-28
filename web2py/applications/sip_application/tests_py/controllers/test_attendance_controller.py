import json
import unittest
from gluon.html import TABLE
from gluon.globals import Request, current, Response
from applications.sip_application.controllers.attendance import show_attendance, create_attendance

# Renombrar la base de datos de prueba para que las funciones la usen en lugar de la base de datos real
db = test_db

class TestAttendanceController(unittest.TestCase):
    def setUp(self):
        # Define your tables
        if 'students' not in db.tables:
            db.define_table('students', Field('name'))
        if 'subjects' not in db.tables:
            db.define_table('subjects', Field('name'))
        if 'classrooms' not in db.tables:
            db.define_table('classrooms', Field('name'))
        if 'attendance' not in db.tables:
            db.define_table('attendance', Field('student_id'), Field('subject_id'), Field('classroom_id'), Field('status'))
            
        self.request = Request(globals())
        self.response = Response()
        current.request = self.request
        current.response = self.response

        db.students.insert(name='Student 1')
        db.subjects.insert(name='Subject 1')
        db.classrooms.insert(name='Classroom 1')
        db.commit()

    def test_show_attendance(self):
        # Act
        result = show_attendance()

        # Assert
        self.assertIsInstance(result, dict)
        self.assertIn('attendance_table', result)
        self.assertIsNotNone(result['attendance_table'])
        self.assertIsInstance(result['attendance_table'], TABLE)

    def test_create_attendance(self):
        # Arrange
        self.request.vars.attendance_status = 'present'
        self.request.vars.student_id = '1'
        self.request.vars.subject_id = '1'
        self.request.vars.classroom_id = '1'

        # Act
        result = create_attendance(self.request, self.response)
        
        # Convert the result to a Python dictionary
        result_dict = json.loads(result)

        # Assert
        self.assertIsInstance(result_dict, dict)
        self.assertIn('success', result_dict)
        self.assertTrue(result_dict['success'])
        self.assertEqual(result_dict['message'], "Attendance data successfully stored")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAttendanceController)
    unittest.TextTestRunner(verbosity=2).run(suite)
