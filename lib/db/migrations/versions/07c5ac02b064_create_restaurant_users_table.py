"""Create restaurant_users table

Revision ID: 07c5ac02b064
Revises: cdc8a03fb018
Create Date: 2024-05-27 17:10:45.254282

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "07c5ac02b064"
down_revision: Union[str, None] = "cdc8a03fb018"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "restaurant_users",
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("restaurant_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["restaurant_id"],
            ["restaurants.id"],
            name=op.f("fk_restaurant_users_restaurant_id_restaurants"),
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_restaurant_users_user_id_users")
        ),
        sa.PrimaryKeyConstraint("user_id", "restaurant_id"),
    )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        op.f("fk_bookings_user_id_users"), "bookings", type_="foreignkey"
    )
    op.drop_constraint(
        op.f("fk_bookings_restaurant_id_restaurants"), "bookings", type_="foreignkey"
    )
    op.drop_column("bookings", "restaurant_id")
    op.drop_column("bookings", "user_id")
    op.drop_table("restaurant_users")
    # ### end Alembic commands ###