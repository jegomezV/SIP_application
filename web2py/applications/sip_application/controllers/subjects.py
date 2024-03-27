from gluon.sqlhtml import SQLFORM
from gluon import current

db = current.globalenv['db']

def subjects_view():
    """
    This function uses SQLFORM.grid to create a CRUD view for the 'subjects' table in the database.
    It returns a dictionary that contains the grid.

    :return: A dictionary that contains the grid.
    """
    grid = SQLFORM.grid(db.subjects)
    return {"grid": grid}
