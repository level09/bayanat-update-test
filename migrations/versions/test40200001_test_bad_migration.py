"""test: intentionally failing migration (should roll back cleanly)

Revision ID: test40200001
Revises: test40100001
Create Date: 2026-04-18 00:00:01.000000
"""

from alembic import op

revision = "test40200001"
down_revision = "test40100001"
branch_labels = None
depends_on = None


def upgrade():
    op.execute("SELECT bayanat_intentionally_missing_fn_for_test()")


def downgrade():
    pass
