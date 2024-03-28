/* StudentRepository.test.ts */

import { StudentModel } from '../../models/StudentModel';
import StudentRepository from '../../repository/StudentRepository';

// Import fetch mock
import fetchMock from 'jest-fetch-mock';

// Enable fetch mocks
fetchMock.enableMocks();

describe('StudentRepository', () => {
  let repository: StudentRepository;
  let student: StudentModel;

  beforeEach(() => {
    // Initialize StudentRepository
    repository = new StudentRepository();

    // Initialize a StudentModel instance
    student = new StudentModel(/* pass the necessary arguments here */);

    // Reset all fetch mocks before each test
    fetchMock.resetMocks();
  });

  it('should register a student', async () => {
    // Mock a successful fetch response
    fetchMock.mockResponseOnce(JSON.stringify({ status: 200 }));

    const response = await repository.registerStudentRepo(student);

    // Check that fetch was called with the right arguments
    expect(fetchMock).toHaveBeenCalledWith(
      'http://127.0.0.1:8000/sip_application/students/register_student',
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(student),
      },
    );

    // Check that the response is as expected
    expect(response).toEqual(200); // Changed this line
  });

  it('should throw an error if the fetch operation fails', async () => {
    // Mock a failed fetch response
    fetchMock.mockReject(new Error('fetch error'));

    await expect(repository.registerStudentRepo(student)).rejects.toThrow('fetch error');
  });
});