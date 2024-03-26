import { StudentModel } from '../models/StudentModel';

export default class FormRenderer {

    render(students: StudentModel[] = []): string {
        let studentForms = students.map(student => `
            <!-- Student registration form -->
            <form id="student-registration-form">
                <label for="name">Name:</label><br>
                <input type="text" id="name" name="name" value="${student.name}"><br>
                <label for="email">Email:</label><br>
                <input type="text" id="email" name="email" value="${student.email}"><br>
                <input type="submit" value="Register">
            </form>
        `).join('');

        return studentForms;
    }
}
