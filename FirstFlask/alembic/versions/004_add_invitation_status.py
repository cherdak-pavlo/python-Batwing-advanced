"""004_add_invitation_status

Revision ID: 004_add_invitation_status
Revises: 003_add_creator_id_field
Create Date: 2022-07-30 12:51:52.775386

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
from sqlalchemy.dialects import postgresql

revision = '004_add_invitation_status'
down_revision = '003_add_creator_id_field'
branch_labels = None
depends_on = None


def upgrade() -> None:
    postgresql.ENUM('accepted', 'declined', 'pending', name='invitation_status').create(op.get_bind())
    op.add_column('user_event',
                  sa.Column('invitation_status', sa.Enum('accepted', 'declined', 'pending', name='invitation_status'),
                            nullable=True))


def downgrade() -> None:
    op.drop_column('user_event', 'invitation_status')
