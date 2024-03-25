/* StudentFactory.ts */

// Import the StudentModel class
import { StudentModel } from '../models/StudentModel';

// Define the StudentFactory class
export class StudentFactory {
  // Method to create a new student
  create(name: string, email: string) {
    // Create and return a new StudentModel instance
    return new StudentModel(name, email);
  }
}
