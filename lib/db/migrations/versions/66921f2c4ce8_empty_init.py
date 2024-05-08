"""Empty Init

Revision ID: 66921f2c4ce8
Revises: f4c119ad864c
Create Date: 2024-05-08 21:26:48.426204

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '66921f2c4ce8'
down_revision: Union[str, None] = 'f4c119ad864c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
