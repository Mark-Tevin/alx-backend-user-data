#!/usr/bin/env python3
"""
This module defines a SQLAlchemy model for the 'users' database table.

The `User` model maps attributes of a user to a database table
using SQLAlchemy's ORM capabilities. With attributes such as `id`, `email`,
`hashed_password`, `session_id`, and `reset_token`.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):
    """
    User model for the 'users' table in the database.

    This class maps the `users` table and provides the structure for storing
    and retrieving user data.

    Attributes:
        __tablename__ (str): Table name in the db.
        id (Column): Primary key.
        email (Column): Non-nullable string storing user's email address.
        hashed_password : Non-nullable string storing hashed password.
        session_id (Column): Nullable string for session management.
        reset_token (Column): Nullable string for the password reset token.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
