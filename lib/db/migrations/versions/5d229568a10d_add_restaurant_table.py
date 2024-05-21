"""Add Restaurant Table

Revision ID: 5d229568a10d
Revises: 36eaaaa9154d
Create Date: 2024-05-21 17:19:23.158004

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5d229568a10d'
down_revision: Union[str, None] = '36eaaaa9154d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
