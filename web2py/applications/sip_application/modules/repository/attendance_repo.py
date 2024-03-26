#attendance repository
from typing import Optional, Dict
from gluon import HTTP
from datetime import datetime

class AttendanceRepository:
    """
    AttendanceRepository is a class that provides methods
    to interact with the 'attendance' collection in the database.
    """

    def __init__(self, db):
        """
        Initializes a new instance of the AttendanceRepository class.
        """
        self.db = db


    def get_all_attendance_repo(self):
        """
        Retrieves all attendance records from the 'attendance' collection.

        :return: A list of dictionaries representing the attendance records.
        """
        return self.db(self.db.attendance).select()


    def get_attendance_by_id_repo(self, attendance_id: int) -> Optional[dict]:
        """
        Retrieves an attendance record by its ID from the 'attendance' collection.

        :param attendance_id: An integer representing the attendance record's ID.
        :return: A dictionary representing the attendance record if found, None otherwise.
        :raises ValueError: If no attendance record is found with the provided ID.
        """
        attendance = self.db.attendance(attendance_id)
        if not attendance:
            raise ValueError(f"No attendance record found with id {attendance_id}")
        return attendance


    def update_attendance_repo(
    self,
    student_id,
    classroom_id,
    subject_id,
    attendance_date,
    attendance_status
    ):
        """
        Updates an attendance record in the 'attendance' collection.

        :param student_id: An integer representing the student's ID.
        :param classroom_id: An integer representing the classroom's ID.
        :param subject_id: An integer representing the subject's ID.
        :param attendance_date: A date object representing the attendance date.
        :param attendance_status: A string representing the attendance status.
        :return: None
        """
        try:
            # Get the names from the database
            student_query = self.db(self.db.students.id == student_id)
            student = student_query.select(self.db.students.name).first()
            if student is None:
                print(f"No student found with ID {student_id}")
                return
            student_name = student.name

            classroom_query = self.db(self.db.classrooms.id == classroom_id)
            classroom = classroom_query.select(self.db.classrooms.name).first()
            if classroom is None:
                print(f"No classroom found with ID {classroom_id}")
                return
            classroom_name = classroom.name

            subject_query = self.db(self.db.subjects.id == subject_id)
            subject = subject_query.select(self.db.subjects.name).first()
            if subject is None:
                print(f"No subject found with ID {subject_id}")
                return
            subject_name = subject.name

            # Insert the attendance data into the attendance table
            self.db.attendance.insert(
                student_name=student_name,
                classroom_name=classroom_name,
                subject_name=subject_name,
                attendance_date=attendance_date,
                status=attendance_status
            )
            self.db.commit()
        except (TypeError, ValueError) as e:
            print(f"Error updating attendance: {e}")
