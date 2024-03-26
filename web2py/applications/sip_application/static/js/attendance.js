/* attendance.js */

// Get all the attendance selects
const attendanceSelects = document.querySelectorAll('.attendance-select');

// Get all the attendance dates
const attendanceDates = document.querySelectorAll('.attendance-date');

// Add a change event listener to each select control
attendanceSelects.forEach((select, index) => {
  select.addEventListener('change', function (event) {
    // Get the selected attendance status
    const attendanceStatus = event.target.value;

    console.log(`El estado de asistencia seleccionado es ${attendanceStatus}.`);

    // Get the student id from the data-student-id attribute
    const studentId = event.target.getAttribute('data_student_id');

    console.log(`El ID del estudiante es ${studentId}.`);

    // Get the subject id from the data-subject-id attribute
    const subjectId = event.target.getAttribute('data_subject_id');

    console.log(`El ID del sujeto es ${subjectId}.`);

    // Get the classroom id from the data-classroom-id attribute
    const classroomId = event.target.getAttribute('data_classroom_id');

    console.log(`El ID del aula es ${classroomId}.`);

    // Get the attendance date from the corresponding date input
    const attendanceDate = attendanceDates[index].value;

    console.log(`La fecha de asistencia es ${attendanceDate}.`);

    // Create a new FormData object
    let formData = new FormData();

    // Append the attendance status, student id, subject id, classroom id, and attendance date to the FormData object
    formData.append('attendance_status', attendanceStatus);
    formData.append('student_id', studentId);
    formData.append('subject_id', subjectId);
    formData.append('classroom_id', classroomId);
    formData.append('attendance_date', attendanceDate);

    // Make an API call to update the attendance status
    fetch(
      `http://127.0.0.1:8000/SIP_application/attendance/create_attendance`,
      {
        method: 'POST',
        body: formData,
      },
    )
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log('Respuesta del servidor:', data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  });
});
