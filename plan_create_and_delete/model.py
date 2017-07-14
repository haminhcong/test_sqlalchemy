# from sqlalchemy import Table, Collumn, Integer, ForeignKey, String, Unicode, UniqueConstraint
import sqlalchemy as sqla
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Farmer(Base):
    __tablename__ = 'farmer'
    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    farmer_id = sqla.Column(sqla.String(50))
    farmer_name = sqla.Column(sqla.Unicode(100))
    address = sqla.Column(sqla.Unicode(100))
    group_id = sqla.Column(sqla.String(50), sqla.ForeignKey('group.id'))
    group = relationship('Group', back_populates='farmers')
    deleted_at = sqla.Column(sqla.DateTime())


class Group(Base):
    __tablename__ = 'group'
    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    group_id = sqla.Column(sqla.String(50))
    group_name = sqla.Column(sqla.Unicode(100))
    farmers = relationship(Farmer, back_populates='group')
    a_group_id = sqla.Column(sqla.String(50),
                             sqla.ForeignKey('associate_group.id'), nullable=True)
    associate_group = relationship('AssociateGroup', back_populates='groups')
    deleted_at = sqla.Column(sqla.DateTime())


class AssociateGroup(Base):
    __tablename__ = 'associate_group'
    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    a_group_id = sqla.Column(sqla.String(50))
    a_group_name = sqla.Column(sqla.Unicode(100))
    groups = relationship('Group', back_populates='associate_group')
    deleted_at = sqla.Column(sqla.DateTime())
