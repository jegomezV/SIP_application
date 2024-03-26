#attendance renderer
from gluon.html import TABLE, TR, TH, TD, SELECT, OPTION, INPUT

class Renderer:
    """Class for rendering attendance data."""
    def __init__(self):
        pass

    def render_attendance(self, data):
        """
        Render attendance data into a HTML table.

        Args:
            data (list): A list of dictionaries containing student, subject, and classroom data.

        Returns:
            gluon.html.TABLE: A TABLE object containing the rendered attendance data.
        """
        rows = []
        for row in data:
            student_id = row["student"].get("id")
            if student_id is None:
                raise KeyError("No 'id' in 'student'")

            subject_id = row["subject"].get("id")
            if subject_id is None:
                raise KeyError("No 'id' in 'subject'")

            classroom_id = row["classroom"].get("id")
            if classroom_id is None:
                raise KeyError("No 'id' in 'classroom'")

            select = SELECT(OPTION('Select', _value="", _selected="selected"),
                            OPTION('Attended', _value="attended"),
                            OPTION('Absent', _value="absent"),
                            _name=f'attendance-{student_id}',
                            _class="attendance-select",
                            _data_student_id=student_id,
                            _data_subject_id=subject_id,
                            _data_classroom_id=classroom_id)

            date_input = INPUT(_type='date', _name=f'date-{student_id}', _class="attendance-date")
            rows.append(TR(TD(row["student"]["name"]),
                        TD(row["subject"]["name"]),
                        TD(row["classroom"]["name"]),
                        TD(date_input),
                        TD(select)))

        table = TABLE(
            *rows,
            _style=(
                "width: 100%; "
                "table-layout: auto; "
                "border-collapse: separate; "
                "border-spacing: 2em;"
            ),
            _class="attendance-table"
        )

        return table
