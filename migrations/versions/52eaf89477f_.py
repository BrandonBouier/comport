"""empty message

Revision ID: 52eaf89477f
Revises: 51524883509
Create Date: 2016-01-25 12:43:06.464754

"""

# revision identifiers, used by Alembic.
revision = '52eaf89477f'
down_revision = '51524883509'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_department_relationship_table',
    sa.Column('department_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['department_id'], ['departments.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('department_id', 'user_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_department_relationship_table')
    ### end Alembic commands ###
