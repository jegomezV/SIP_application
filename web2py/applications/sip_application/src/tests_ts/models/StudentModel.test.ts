/* StudentModel.test.ts */

// Import the necessary modules and classes
import { StudentModel } from '../../models/StudentModel';

describe('StudentModel', () => {
  it('should create a new student model', () => {
    // Define the name and email for the new student model
    const name = 'John Doe';
    const email = 'john.doe@example.com';

    // Create a new instance of StudentModel
    const student = new StudentModel(name, email);

    // Check that the student's name and email are correct
    expect(student.name).toBe(name);
    expect(student.email).toBe(email);
  });
});
