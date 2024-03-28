import { JSDOM } from 'jsdom';
import { StudentController } from '../../controllers/StudentControllers';
import StudentRepository from '../../repository/StudentRepository';
import { StudentFactory } from '../../factory/StudentFactory';
import FormRenderer from '../../renderer/FormRenderer'

describe('StudentController', () => {
  let repositoryMock: jest.Mocked<StudentRepository>;
  let factoryMock: jest.Mocked<StudentFactory>;
  let rendererMock: jest.Mocked<FormRenderer>;

  beforeEach(() => {
    repositoryMock = {
      registerStudentRepo: jest.fn(),
    } as any;

    factoryMock = {
      create: jest.fn(),
    } as any;

    rendererMock = {
      render: jest.fn().mockReturnValue('<form></form>'),
    } as any;
  });

  it('should render form', () => {
    const dom = new JSDOM(`<!DOCTYPE html><div id="form-container"></div></html>`);
    global.document = dom.window.document;

    const controller = new StudentController(repositoryMock, factoryMock, rendererMock);
    const formHtml = controller.renderForm();

    expect(formHtml).toBe('<form></form>');
    expect(rendererMock.render).toHaveBeenCalled();
  });

  it('should register a student', async () => {
    const controller = new StudentController(repositoryMock, factoryMock, rendererMock);
    const name = 'John Doe';
    const email = 'john.doe@example.com';
    const studentMock = { id: 1, name, email };

    factoryMock.create.mockReturnValue(studentMock);
    repositoryMock.registerStudentRepo.mockResolvedValue();

    const registeredStudent = await controller.registerStudentController(name, email);

    expect(factoryMock.create).toHaveBeenCalledWith(name, email);
    expect(repositoryMock.registerStudentRepo).toHaveBeenCalledWith(studentMock);
    expect(registeredStudent).toBe(studentMock);
  });

  it('should throw an error when registration fails', async () => {
    const controller = new StudentController(repositoryMock, factoryMock, rendererMock);
    const name = 'John Doe';
    const email = 'john.doe@example.com';
    const errorMock = new Error('The user has already been created');

    factoryMock.create.mockReturnValue({ id: 1, name, email });
    repositoryMock.registerStudentRepo.mockRejectedValue(errorMock);

    await expect(controller.registerStudentController(name, email)).rejects.toThrowError(errorMock);
  });
});