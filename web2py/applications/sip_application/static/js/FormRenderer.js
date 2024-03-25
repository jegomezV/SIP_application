(function webpackUniversalModuleDefinition(root, factory) {
	if(typeof exports === 'object' && typeof module === 'object')
		module.exports = factory();
	else if(typeof define === 'function' && define.amd)
		define([], factory);
	else if(typeof exports === 'object')
		exports["FormRenderer"] = factory();
	else
		root["FormRenderer"] = factory();
})(self, () => {
return /******/ (() => { // webpackBootstrap
/******/ 	"use strict";
var __webpack_exports__ = {};
// This entry need to be wrapped in an IIFE because it uses a non-standard name for the exports (exports).
(() => {
var exports = __webpack_exports__;
/*!**********************************!*\
  !*** ./renderer/FormRenderer.ts ***!
  \**********************************/

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
module.exports["default"] = FormRenderer;

})();

/******/ 	return __webpack_exports__;
/******/ })()
;
});
//# sourceMappingURL=FormRenderer.js.map