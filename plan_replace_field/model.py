# from sqlalchemy import Table, Collumn, Integer, ForeignKey, String, Unicode, UniqueConstraint
import sqlalchemy as sqla
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Farmer(Base):
    __tablename__ = 'farmer'
    farmer_id = sqla.Column(sqla.String(50), primary_key=True)
    farmer_name = sqla.Column(sqla.Unicode(100), unique=True)
    address = sqla.Column(sqla.Unicode(100))
    group_id = sqla.Column(sqla.String(50), sqla.ForeignKey('group.group_id'))
    group = relationship('Group', back_populates='farmers')
    deleted_at = sqla.Column(sqla.DateTime())


class Group(Base):
    __tablename__ = 'group'
    group_id = sqla.Column(sqla.String(50), primary_key=True)
    group_name = sqla.Column(sqla.Unicode(100), unique=True)
    farmers = relationship(Farmer, back_populates='group')
    # associate_group_id = sqla.Column(sqla.String(50), sqla.ForeignKey('associate_group_id'))
    a_group_id = sqla.Column(sqla.String(50),
                             sqla.ForeignKey('associate_group.a_group_id'), nullable=True)
    associate_group = relationship('AssociateGroup', back_populates='groups')
    deleted_at = sqla.Column(sqla.DateTime())


class AssociateGroup(Base):
    __tablename__ = 'associate_group'
    a_group_id = sqla.Column(sqla.String(50), primary_key=True)
    a_group_name = sqla.Column(sqla.Unicode(100), unique=True)
    groups = relationship('Group', back_populates='associate_group')
    deleted_at = sqla.Column(sqla.DateTime())
