"""create scores table

Revision ID: 87cc16b4dfc4
Revises: 
Create Date: 2024-07-11 16:03:19.460551

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine.reflection import Inspector


# revision identifiers, used by Alembic.
revision = '87cc16b4dfc4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    inspector = Inspector.from_engine(conn)
    tables = inspector.get_table_names()
    table_name = 'scores'
    if table_name not in tables:
        op.create_table(
            'scores',
            sa.Column('initials', sa.String(3), nullable=False),
            sa.Column('score', sa.Integer, nullable=False)
        )

def downgrade():
    pass
