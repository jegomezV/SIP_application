"""tables_create

Revision ID: 611c77106a95
Revises: 
Create Date: 2024-03-28 16:29:15.351142

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '611c77106a95'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Crear la tabla 'students'
    op.create_table(
        'students',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(50), nullable=False, unique=True)
    )

    # Crear la tabla 'classrooms'
    op.create_table(
        'classrooms',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False)
    )

    # Crear la tabla 'subjects'
    op.create_table(
        'subjects',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False)
    )

    # Crear la tabla 'attendance'
    op.create_table(
        'attendance',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('student_id', sa.Integer, sa.ForeignKey('students.id'), nullable=False),
        sa.Column('classroom_id', sa.Integer, sa.ForeignKey('classrooms.id'), nullable=False),
        sa.Column('subject_id', sa.Integer, sa.ForeignKey('subjects.id'), nullable=False),
        sa.Column('attendance_date', sa.DateTime, nullable=True),
        sa.Column('status', sa.String(50), nullable=False)
    )


def downgrade() -> None:
    # Eliminar las tablas en orden inverso a su creación
    op.drop_table('attendance')
    op.drop_table('subjects')
    op.drop_table('classrooms')
    op.drop_table('students')
