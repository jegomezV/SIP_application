def classrooms_view():
    """
    This function uses SQLFORM.grid
    to create a CRUD view for the 'classrooms' table in the database.
    It orders the classrooms by their names.
    It returns a dictionary that contains the grid.

    :return: A dictionary that contains the grid.
    """
    grid_classroom = SQLFORM.grid(db.classrooms, orderby=db.classrooms.name)
    return {"grid": grid_classroom}
