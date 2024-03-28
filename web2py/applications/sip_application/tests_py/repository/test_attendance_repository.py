import unittest
from unittest.mock import MagicMock
from applications.sip_application.modules.repository.attendance_repo import AttendanceRepository

class TestAttendanceRepository(unittest.TestCase):
    def setUp(self):
        self.db_mock = MagicMock()
        self.attendance_repo = AttendanceRepository(self.db_mock)

    def test_get_all_attendance_repo(self):
        self.attendance_repo.get_all_attendance_repo()
        self.db_mock.assert_called_once()

    def test_get_attendance_by_id_repo(self):
        self.attendance_repo.get_attendance_by_id_repo(1)
        self.db_mock.attendance.assert_called_once_with(1)

    def test_update_attendance_repo(self):
        student_id = 1
        classroom_id = 1
        subject_id = 1
        attendance_status = "Present"
        self.attendance_repo.update_attendance_repo(student_id, classroom_id, subject_id, attendance_status)
        self.db_mock.attendance.insert.assert_called_once_with(student_id=student_id, classroom_id=classroom_id, subject_id=subject_id, status=attendance_status)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAttendanceRepository)
    unittest.TextTestRunner().run(suite)
