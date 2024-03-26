import  StudentRepository  from "../repository/StudentRepository";
import { StudentFactory } from "../factory/StudentFactory";
import  FormRenderer  from "./FormRenderer";
import { StudentController } from "../controllers/StudentControllers";

document.addEventListener("DOMContentLoaded", () => {
  const repository = new StudentRepository();
  const factory = new StudentFactory();
  const renderer = new FormRenderer();
  const controller = new StudentController(repository, factory, renderer);

  // Render the form
  const formHtml = controller.renderForm();

  // Add the form to the DOM
  const formContainer = document.querySelector("#form-container");
  if (formContainer) {
    formContainer.innerHTML = formHtml;
  }

  const form = document.querySelector("#student-registration-form");
  if (form) {
    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      const form = event.target as HTMLFormElement;
      const name = (form.elements.namedItem("name") as HTMLInputElement).value;
      const email = (form.elements.namedItem("email") as HTMLInputElement)
        .value;

      try {
        const student = await controller.registerStudent(name, email);
        console.log("Student registered:", student);
      } catch (error) {
        console.error("Error registering student:", error);
      }
    });
  }
});