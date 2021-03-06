"""added username

Revision ID: 63340ed63b10
Revises: f9160d34d296
Create Date: 2021-12-20 09:57:51.062765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63340ed63b10'
down_revision = 'f9160d34d296'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.String(length=255), nullable=False))
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'username')
    # ### end Alembic commands ###
