/* FormRenderer.test.ts */

// Import the necessary modules and classes
import FormRenderer from '../../renderer/FormRenderer';
import { StudentModel } from '../../models/StudentModel';

describe('FormRenderer', () => {
  let renderer: FormRenderer;

  beforeEach(() => {
    // Create a new instance of FormRenderer before each test
    renderer = new FormRenderer();
  });

  it('should render form', () => {
    // Define a mock student
    const studentMock = new StudentModel();
    studentMock.name = 'John Doe';
    studentMock.email = 'john.doe@example.com';

    // Call the render method on the renderer
    const formHtml = renderer.render([studentMock]);

    // Define the expected HTML
    const expectedHtml = `
            <!-- Student registration form -->
            <form id="student-registration-form">
                <label for="name">Name:</label><br>
                <input type="text" id="name" name="name" value="${studentMock.name}"><br>
                <label for="email">Email:</label><br>
                <input type="text" id="email" name="email" value="${studentMock.email}"><br>
                <input type="submit" value="Register">
            </form>
        `;

    // Check that the returned HTML is correct
    expect(formHtml).toBe(expectedHtml);
  });
});