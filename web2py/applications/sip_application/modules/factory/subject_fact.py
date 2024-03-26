from typing import Dict
from ...models.subjects_model import Subjects

class Singleton(type):
    """
    Singleton class to ensure that a class has only one instance.
    """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class SubjectFactory(metaclass=Singleton):
    """
    A factory class for creating materias.

    Attributes:
        db: A database connection object.
    """
    _cache = {}

    def create_subject(self, subject_data: Dict[str, Any]) -> Subjects:
        """
        The function to create a materia.

        Parameters:
            subject_data (Dict[str, Any]): The data of the materia.

        Returns:
            Subjects: An instance of the Subjects model.
        """
        name = subject_data['name']
        if name not in self._cache:
            self._cache[name] = Subjects(name)
        return self._cache[name]
