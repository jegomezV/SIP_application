(function webpackUniversalModuleDefinition(root, factory) {
	if(typeof exports === 'object' && typeof module === 'object')
		module.exports = factory();
	else if(typeof define === 'function' && define.amd)
		define([], factory);
	else if(typeof exports === 'object')
		exports["main"] = factory();
	else
		root["main"] = factory();
})(self, () => {
return /******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "./controllers/StudentControllers.ts":
/*!*******************************************!*\
  !*** ./controllers/StudentControllers.ts ***!
  \*******************************************/
/***/ (function(__unused_webpack_module, exports) {


/* StudentController.ts */
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.StudentController = void 0;
// Define the StudentController class
class StudentController {
    // Constructor for the StudentController class
    constructor(repository, factory, renderer) {
        this.repository = repository;
        this.factory = factory;
        this.renderer = renderer;
    }
    // Method to render the form
    renderForm() {
        const formHtml = this.renderer.render();
        const formContainer = document.getElementById('form-container');
        if (formContainer) {
            formContainer.innerHTML = formHtml;
        }
        return formHtml;
    }
    // Method to register a student
    registerStudent(name, email) {
        return __awaiter(this, void 0, void 0, function* () {
            // Create a new student using the factory
            const student = this.factory.create(name, email);
            // Register the student using the repository
            try {
                yield this.repository.registerStudent(student);
                return student;
            }
            catch (error) {
                // If the registration was not successful, throw an error
                throw new Error('The user has already been created'); // Assume the error details include a "message" property
            }
        });
    }
}
exports.StudentController = StudentController;


/***/ }),

/***/ "./factory/StudentFactory.ts":
/*!***********************************!*\
  !*** ./factory/StudentFactory.ts ***!
  \***********************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


/* StudentFactory.ts */
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.StudentFactory = void 0;
// Import the StudentModel class
const StudentModel_1 = __webpack_require__(/*! ../models/StudentModel */ "./models/StudentModel.ts");
// Define the StudentFactory class
class StudentFactory {
    // Method to create a new student
    create(name, email) {
        // Create and return a new StudentModel instance
        return new StudentModel_1.StudentModel(name, email);
    }
}
exports.StudentFactory = StudentFactory;


/***/ }),

/***/ "./models/StudentModel.ts":
/*!********************************!*\
  !*** ./models/StudentModel.ts ***!
  \********************************/
/***/ ((__unused_webpack_module, exports) => {


/* StudentModel.ts */
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.StudentModel = void 0;
// Define the StudentModel class
class StudentModel {
    // Constructor for the StudentModel class
    constructor(name, email) {
        // Initialize the name and email properties
        this.name = name;
        this.email = email;
    }
}
exports.StudentModel = StudentModel;


/***/ }),

/***/ "./renderer/FormRenderer.ts":
/*!**********************************!*\
  !*** ./renderer/FormRenderer.ts ***!
  \**********************************/
/***/ ((__unused_webpack_module, exports) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
class FormRenderer {
    render(students = []) {
        return `
            <!-- Student registration form -->
            <form id="student-registration-form">
                <label for="name">Name:</label><br>
                <input type="text" id="name" name="name"><br>
                <label for="email">Email:</label><br>
                <input type="text" id="email" name="email"><br>
                <input type="submit" value="Register">
            </form>
        `;
    }
}
exports["default"] = FormRenderer;


/***/ }),

/***/ "./renderer/Students.ts":
/*!******************************!*\
  !*** ./renderer/Students.ts ***!
  \******************************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
const StudentRepository_1 = __importDefault(__webpack_require__(/*! ../repository/StudentRepository */ "./repository/StudentRepository.ts"));
const StudentFactory_1 = __webpack_require__(/*! ../factory/StudentFactory */ "./factory/StudentFactory.ts");
const FormRenderer_1 = __importDefault(__webpack_require__(/*! ./FormRenderer */ "./renderer/FormRenderer.ts"));
const StudentControllers_1 = __webpack_require__(/*! ../controllers/StudentControllers */ "./controllers/StudentControllers.ts");
document.addEventListener("DOMContentLoaded", () => {
    const repository = new StudentRepository_1.default();
    const factory = new StudentFactory_1.StudentFactory();
    const renderer = new FormRenderer_1.default();
    const controller = new StudentControllers_1.StudentController(repository, factory, renderer);
    // Render the form
    const formHtml = controller.renderForm();
    // Add the form to the DOM
    const formContainer = document.querySelector("#form-container");
    if (formContainer) {
        formContainer.innerHTML = formHtml;
    }
    const form = document.querySelector("#student-registration-form");
    if (form) {
        form.addEventListener("submit", (event) => __awaiter(void 0, void 0, void 0, function* () {
            event.preventDefault();
            const form = event.target;
            const name = form.elements.namedItem("name").value;
            const email = form.elements.namedItem("email")
                .value;
            try {
                const student = yield controller.registerStudent(name, email);
                console.log("Student registered:", student);
            }
            catch (error) {
                console.error("Error registering student:", error);
            }
        }));
    }
});


/***/ }),

/***/ "./repository/StudentRepository.ts":
/*!*****************************************!*\
  !*** ./repository/StudentRepository.ts ***!
  \*****************************************/
/***/ (function(__unused_webpack_module, exports) {


/* StudentRepository.ts */
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
// Define the StudentRepository class
class StudentRepository {
    // Method to register a student
    registerStudent(student) {
        return __awaiter(this, void 0, void 0, function* () {
            try {
                console.log("ENTROO");
                console.log(student);
                console.log('student');
                const response = yield fetch('http://127.0.0.1:8000/sip_application/students/register_student', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(student),
                    credentials: 'include',
                });
                // Check if the request was successful
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response;
            }
            catch (error) {
                console.error('There was an error with the fetch operation: ', error);
                throw error; // Re-throwing the error so it can be caught and handled by the caller
            }
        });
    }
}
exports["default"] = StudentRepository;


/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module is referenced by other modules so it can't be inlined
/******/ 	var __webpack_exports__ = __webpack_require__("./renderer/Students.ts");
/******/ 	
/******/ 	return __webpack_exports__;
/******/ })()
;
});
//# sourceMappingURL=main.js.map
