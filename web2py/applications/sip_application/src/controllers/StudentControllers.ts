/* StudentController.ts */

// Import necessary classes
import { StudentModel } from '../models/StudentModel';
import { StudentRepository } from '../repository/StudentRepository';
import { StudentFactory } from '../factory/StudentFactory';
import { FormRenderer } from '../renderer/FormRenderer'

// Define the StudentController class
export class StudentController {
  // Declare private variables for the repository, factory, and renderer
  private repository: StudentRepository;
  private factory: StudentFactory;
  private renderer: FormRenderer;

  // Constructor for the StudentController class
  constructor(repository: StudentRepository, factory: StudentFactory, renderer: FormRenderer) {
    this.repository = repository;
    this.factory = factory;
    this.renderer = renderer;
  }

  // Method to render the form
  renderForm(): string {
    const formHtml = this.renderer.render();
    const formContainer = document.getElementById('form-container');
    if (formContainer) {
      formContainer.innerHTML = formHtml;
    }
    return formHtml;
  }

  // Method to register a student
  async registerStudent(name: string, email: string): Promise<StudentModel> {
    // Create a new student using the factory
    const student = this.factory.create(name, email);

    // Register the student using the repository
    try {
      await this.repository.registerStudent(student);
      return student;
    } catch (error) {
      // If the registration was not successful, throw an error
      throw new Error('The user has already been created'); // Assume the error details include a "message" property
    }
  }
}