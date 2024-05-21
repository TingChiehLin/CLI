"""Add Booking Table

Revision ID: c37f7225b1d6
Revises: 5d229568a10d
Create Date: 2024-05-21 17:26:09.225159

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c37f7225b1d6'
down_revision: Union[str, None] = '5d229568a10d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
