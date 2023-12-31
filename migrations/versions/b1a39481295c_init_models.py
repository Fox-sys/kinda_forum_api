"""init models

Revision ID: b1a39481295c
Revises: 0259c9532df5
Create Date: 2023-10-25 00:58:41.308909

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'b1a39481295c'
down_revision: Union[str, None] = '0259c9532df5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('custom_role_color_scheme', sa.String(), nullable=True),
                    sa.Column('create_thread', sa.Boolean(), nullable=False),
                    sa.Column('create_comment', sa.Boolean(), nullable=False),
                    sa.Column('delete_comment', sa.Boolean(), nullable=False),
                    sa.Column('delete_thread', sa.Boolean(), nullable=False),
                    sa.Column('change_role', sa.Boolean(), nullable=False),
                    sa.Column('change_role_superuser', sa.Boolean(), nullable=False),
                    sa.Column('use_color_scheme', sa.Boolean(), nullable=False),
                    sa.Column('ban_user', sa.Boolean(), nullable=False),
                    sa.Column('change_own_prefix', sa.Boolean(), nullable=False),
                    sa.Column('change_other_prefix', sa.Boolean(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('first_name', sa.String(), nullable=False),
                    sa.Column('last_name', sa.String(), nullable=True),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('is_active', sa.Boolean(), nullable=True),
                    sa.Column('is_superuser', sa.Boolean(), nullable=True),
                    sa.Column('register_date', sa.TIMESTAMP(), nullable=True),
                    sa.Column('custom_role_prefix', sa.String(), nullable=True),
                    sa.Column('custom_role_color_scheme', sa.String(), nullable=True),
                    sa.Column('role', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['role'], ['roles.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('id'),
                    sa.UniqueConstraint('username')
                    )
    op.create_table('threads',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('short_description', sa.Text(), nullable=False),
                    sa.Column('long_description', sa.Text(), nullable=False),
                    sa.Column('auther', sa.Integer(), nullable=False),
                    sa.Column('rating', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['auther'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('comments',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('text', sa.Text(), nullable=False),
                    sa.Column('auther', sa.Integer(), nullable=False),
                    sa.Column('thread', sa.Integer(), nullable=False),
                    sa.Column('upper_comment', sa.Integer(), nullable=True),
                    sa.Column('rating', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['auther'], ['users.id'], ),
                    sa.ForeignKeyConstraint(['thread'], ['threads.id'], ),
                    sa.ForeignKeyConstraint(['upper_comment'], ['comments.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    op.drop_table('threads')
    op.drop_table('users')
    op.drop_table('roles')
    # ### end Alembic commands ###
