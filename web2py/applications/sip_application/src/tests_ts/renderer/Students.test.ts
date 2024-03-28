/* Students.test.ts */

import { JSDOM } from 'jsdom';
import StudentRepository from '../../repository/StudentRepository';
import { StudentFactory } from '../../factory/StudentFactory';
import FormRenderer from '../../renderer/FormRenderer';
import { StudentController } from '../../controllers/StudentControllers';

describe('Students', () => {
  let repository: StudentRepository;
  let factory: StudentFactory;
  let renderer: FormRenderer;
  let controller: StudentController;
  let dom: JSDOM;
  let window: Window;
  let document: Document;

  beforeEach(() => {
    // Create a new JSDOM instance
    dom = new JSDOM(`<!DOCTYPE html><div id="form-container"></div>`);
    window = dom.window;
    document = window.document;

    // Create new instances of the classes
    repository = new StudentRepository();
    factory = new StudentFactory();
    renderer = new FormRenderer();
    controller = new StudentController(repository, factory, renderer);
  });

  it('should render form', () => {
    // Render the form
    const formHtml = controller.renderForm();

    // Add the form to the DOM
    const formContainer = document.querySelector("#form-container");
    if (formContainer) {
      formContainer.innerHTML = formHtml;
    }

    // Check that the form was added to the DOM
    const form = document.querySelector("#student-registration-form");
    expect(form).not.toBeNull();
  });

  // Add more tests as needed...
});