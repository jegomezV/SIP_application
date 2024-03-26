from typing import Dict, Any
from ...models.classroom_model import Classrooms

class Singleton(type):
    """
    Singleton class to ensure that a class has only one instance.
    """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class ClassroomFactory(metaclass=Singleton):
    """
    A factory class for creating classrooms.

    Attributes:
        db: A database connection object.
    """
    _cache = {}

    def create_classroom(self, classroom_data: Dict[str, Any]) -> Classrooms:
        """
        The function to create a classroom.

        Parameters:
            classroom_data (Dict[str, Any]): The data of the classroom.

        Returns:
            Classrooms: An instance of the Classrooms model.
        """
        name = classroom_data['name']
        if name not in self._cache:
            self._cache[name] = Classrooms(name)
        return self._cache[name]
