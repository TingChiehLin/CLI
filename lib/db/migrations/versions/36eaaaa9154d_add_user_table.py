"""Add User  Table

Revision ID: 36eaaaa9154d
Revises: 5a98cf2bfb93
Create Date: 2024-05-21 17:12:22.062449

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '36eaaaa9154d'
down_revision: Union[str, None] = '5a98cf2bfb93'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
