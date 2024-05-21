"""Add restaurent_user Table

Revision ID: aeba6afdd3fd
Revises: c37f7225b1d6
Create Date: 2024-05-21 17:27:41.668729

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aeba6afdd3fd'
down_revision: Union[str, None] = 'c37f7225b1d6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
