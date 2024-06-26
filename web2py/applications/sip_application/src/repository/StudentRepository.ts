/* StudentRepository.ts */

// Import the StudentModel class
import { StudentModel } from '../models/StudentModel';

// Define the StudentRepository class
export default class StudentRepository {
  // Method to register a student
  async registerStudentRepo(student: StudentModel): Promise<number> {
    try {
      const response = await fetch(
        'https://127.0.0.1:8000/sip_application/students/register_student',
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(student),
        },
      );
  
      // Check if the request was successful
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
  
      return response.status;
    } catch (error) {
      console.error('There was an error with the fetch operation: ', error);
      throw error;  // Re-throwing the error so it can be caught and handled by the caller
    }
  }
}
