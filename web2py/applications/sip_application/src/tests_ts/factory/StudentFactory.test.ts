/* StudentFactory.test.ts */

// Import the necessary modules and classes
import { StudentFactory } from '../../factory/StudentFactory';
import { StudentModel } from '../../models/StudentModel';

describe('StudentFactory', () => {
  let factory: StudentFactory;

  beforeEach(() => {
    // Create a new instance of StudentFactory before each test
    factory = new StudentFactory();
  });

  it('should create a new student', () => {
    // Define the name and email for the new student
    const name = 'John Doe';
    const email = 'john.doe@example.com';

    // Call the create method on the factory
    const student = factory.create(name, email);

    // Check that the returned student is an instance of StudentModel
    expect(student).toBeInstanceOf(StudentModel);

    // Check that the student's name and email are correct
    expect(student.name).toBe(name);
    expect(student.email).toBe(email);
  });
});
