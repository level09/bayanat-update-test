"""test: add auto_update_test column to bulletin (additive, should succeed)

Revision ID: test40100001
Revises: cdaa80fb493a
Create Date: 2026-04-18 00:00:00.000000

"""

from alembic import op
import sqlalchemy as sa

revision = "test40100001"
down_revision = "cdaa80fb493a"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("bulletin", sa.Column("auto_update_test", sa.String(), nullable=True))


def downgrade():
    op.drop_column("bulletin", "auto_update_test")
