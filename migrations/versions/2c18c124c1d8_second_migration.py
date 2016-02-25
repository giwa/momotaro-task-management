"""second migration

Revision ID: 2c18c124c1d8
Revises: None
Create Date: 2016-02-25 16:15:18.995630

"""

# revision identifiers, used by Alembic.
revision = '2c18c124c1d8'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    ### end Alembic commands ###
