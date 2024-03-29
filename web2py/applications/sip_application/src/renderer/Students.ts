import  StudentRepository  from "../repository/StudentRepository";
import { StudentFactory } from "../factory/StudentFactory";
import  FormRenderer  from "./FormRenderer";
import { StudentController } from "../controllers/StudentControllers";
import Swal from 'sweetalert2';

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
      const email = (form.elements.namedItem("email") as HTMLInputElement).value;
  
      // Validaciones
      if (!name) {
        Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: 'Name is required',
        });
        return;
      }
  
      if (!email) {
        Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: 'Email is required',
        });
        return;
      }
  
      // Comprobación del formato del email
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
        Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: 'Invalid email format',
        });
        return;
      }
  
      try {
        const student = await controller.registerStudentController(name, email);
        Swal.fire({
          icon: 'success',
          title: 'Success',
          text: 'Student registered successfully.',
        });
      } catch (error) {
        console.error("Error registering student:", error);
        if ((error as Error).message === 'The user has already been created') {
          Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'This user has already been registered.',
          });
        } else {
          Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'An unknown error occurred while registering the student.',
          });
        }
      }
    });
  }
});
