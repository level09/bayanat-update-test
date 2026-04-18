"""test: recovery additive migration after failed releases

Revision ID: test40400001
Revises: test40100001
Create Date: 2026-04-18 00:00:03.000000
"""

from alembic import op
import sqlalchemy as sa

revision = "test40400001"
down_revision = "test40100001"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "bulletin",
        sa.Column("auto_update_recovery_test", sa.String(), nullable=True),
    )


def downgrade():
    op.drop_column("bulletin", "auto_update_recovery_test")
