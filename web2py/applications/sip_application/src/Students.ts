/* formEvents.ts */

import { StudentModel } from "./models/StudentModel";
import { StudentRepository } from "./repository/StudentRepository";
import { StudentFactory } from "./factory/StudentFactory";
import { FormRenderer } from "./renderer/FormRenderer";
import { StudentController } from "../controllers/StudentControllers";

const repository = new StudentRepository();
const factory = new StudentFactory();
const renderer = new FormRenderer();
const controller = new StudentController(repository, factory, renderer);

document.addEventListener("DOMContentLoaded", () => {
  // Render the form
  controller.renderForm();

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
