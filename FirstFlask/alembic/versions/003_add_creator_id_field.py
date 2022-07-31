"""003_add_creator_id_field

Revision ID: 1b9fc9557a6c
Revises: 002_add_event_relation
Create Date: 2022-07-26 19:35:20.560319

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '003_add_creator_id_field'
down_revision = '002_add_event_relation'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('event', sa.Column('creator_id', sa.Integer()))


def downgrade() -> None:
    op.drop_column('event', 'creator_id')
