"""002_create_books_table

Revision ID: 002_create_books_table
Revises: 001_create_authors_table
Create Date: 2022-07-10 15:48:32.100301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002_create_books_table'
down_revision = '001_create_authors_table'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "books",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("book_name", sa.String(300), nullable=False),
        sa.Column("year", sa.Integer, nullable=False)
    )


def downgrade() -> None:
    op.drop_table("books")
