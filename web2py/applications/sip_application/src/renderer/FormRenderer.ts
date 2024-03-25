import { StudentModel } from '../models/StudentModel';

export class FormRenderer {

    render(students: StudentModel[] = []): string {

        return `
            <!-- Student registration form -->
            <form id="student-registration-form">
                <label for="name">Name:</label><br>
                <input type="text" id="name" name="name"><br>
                <label for="email">Email:</label><br>
                <input type="text" id="email" name="email"><br>
                <input type="submit" value="Register">
            </form>
        `;
    }
}
