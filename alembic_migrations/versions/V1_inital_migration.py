"""inital migration

Revision ID: 462fea73a25f
Revises:
Create Date: 2024-06-25 00:51:28.538024

"""

from typing import Sequence
from typing import Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "462fea73a25f"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "events",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("start_date_time", sa.DateTime(), nullable=False),
        sa.Column("end_date_time", sa.DateTime(), nullable=False),
        sa.Column("min_price", sa.Float(), nullable=False),
        sa.Column("max_price", sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.add_column("events", sa.Column("event_id", sa.Integer(), nullable=False))
    op.add_column("events", sa.Column("base_event_id", sa.Integer(), nullable=False))
    op.create_index(op.f("ix_events_base_event_id"), "events", ["base_event_id"], unique=False)
    op.create_index(op.f("ix_events_end_date_time"), "events", ["end_date_time"], unique=False)
    op.create_index(op.f("ix_events_event_id"), "events", ["event_id"], unique=False)
    op.create_index(
        op.f("ix_events_start_date_time"), "events", ["start_date_time"], unique=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_events_start_date_time"), table_name="events")
    op.drop_index(op.f("ix_events_event_id"), table_name="events")
    op.drop_index(op.f("ix_events_end_date_time"), table_name="events")
    op.drop_index(op.f("ix_events_base_event_id"), table_name="events")
    op.drop_column("events", "base_event_id")
    op.drop_column("events", "event_id")
    op.drop_table("events")
    # ### end Alembic commands ###