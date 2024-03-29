/* attendance.js */

// Get all the attendance selects
const attendanceSelects = document.querySelectorAll(".attendance-select");

// Add a change event listener to each select control
attendanceSelects.forEach((select, index) => {
  select.addEventListener("change", function (event) {
    // Get the selected attendance status
    const attendanceStatus = event.target.value;

    // Get the student id from the data-student-id attribute
    const studentId = event.target.getAttribute("data_student_id");

    // Get the subject id from the data-subject-id attribute
    const subjectId = event.target.getAttribute("data_subject_id");

    // Get the classroom id from the data-classroom-id attribute
    const classroomId = event.target.getAttribute("data_classroom_id");

    // Create a new FormData object
    let formData = new FormData();

    // Append the attendance status, student id, subject id, classroom id, and attendance date to the FormData object
    formData.append("attendance_status", attendanceStatus);
    formData.append("student_id", studentId);
    formData.append("subject_id", subjectId);
    formData.append("classroom_id", classroomId);

    for (let pair of formData.entries()) {
      console.log(pair[0] + ", " + pair[1]);
    }

    console.log("attendanceStatus:", attendanceStatus);
    console.log("studentId:", studentId);
    console.log("subjectId:", subjectId);
    console.log("classroomId:", classroomId);

    // Make an API call to update the attendance status
    fetch(
      `http://127.0.0.1:8000/sip_application/attendance/create_attendance`,
      {
        method: "POST",
        body: formData,
      }
    )
      .then((response) => {
        console.log("Response status:", response.status);
        console.log("Response headers:", [...response.headers]);
        return response.text();
      })
      .then((text) => {
        console.log("Response text:", text);
        return JSON.parse(text);
      })
      .then((data) => {
        console.log("Respuesta del servidor:", data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
});
