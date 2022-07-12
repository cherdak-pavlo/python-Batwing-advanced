"""003_create_relation

Revision ID: 003_create_relation
Revises: 002_create_books_table
Create Date: 2022-07-10 22:17:44.591561

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '003_create_relation'
down_revision = '002_create_books_table'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "books_authors",
        sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
        sa.Column("book_id", sa.Integer, sa.ForeignKey("books.id")),
        sa.Column("author_id", sa.Integer, sa.ForeignKey("authors.id"))
    )


def downgrade() -> None:
    op.drop_table("books_authors")

