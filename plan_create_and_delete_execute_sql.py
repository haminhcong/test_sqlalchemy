import os
from datetime import datetime
from plan_create_and_delete.model import Base, Farmer, Group, AssociateGroup
from sqlalchemy.orm import sessionmaker

basedir = os.path.abspath(os.path.dirname(__file__))
import sqlalchemy

# from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                          'sqlite:///' + os.path.join(basedir, 'plan_create_and_delete.sqlite')

test_engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Base.metadata.create_all(test_engine)  # create database
Session = sessionmaker(bind=test_engine)
session = Session()  # create session

associate_groups = [
    AssociateGroup(a_group_id='AG000', a_group_name='Liên nhóm 0'),
    AssociateGroup(a_group_id='AG001', a_group_name='Liên nhóm 1'),
    AssociateGroup(a_group_id='AG002', a_group_name='Liên nhóm 2')
]

groups = [
    Group(group_id='G000', group_name='Nhóm 0', associate_group=associate_groups[0]),
    Group(group_id='G001', group_name='Nhóm 1', associate_group=associate_groups[0]),
    Group(group_id='G002', group_name='Nhóm 2', associate_group=associate_groups[1]),
    Group(group_id='G003', group_name='Nhóm 3', associate_group=associate_groups[1]),
]

farmers = [
    Farmer(farmer_id='F000', farmer_name='Nông dân 0', address='Tỉnh 0', group=groups[0]),
    Farmer(farmer_id='F001', farmer_name='Nông dân 1', address='Tỉnh 1', group=groups[0]),
    Farmer(farmer_id='F002', farmer_name='Nông dân 2', address='Tỉnh 2', group=groups[1]),
    Farmer(farmer_id='F003', farmer_name='Nông dân 3', address='Tỉnh 3', group=groups[1]),
    Farmer(farmer_id='F004', farmer_name='Nông dân 4', address='Tỉnh 4', group=groups[2]),
    Farmer(farmer_id='F005', farmer_name='Nông dân 5', address='Tỉnh 5', group=groups[2]),
    Farmer(farmer_id='F006', farmer_name='Nông dân 6', address='Tỉnh 6', group=groups[3]),
    Farmer(farmer_id='F007', farmer_name='Nông dân 7', address='Tỉnh 7', group=groups[3]),

]

[session.add(associate_group) for associate_group in associate_groups]
[session.add(group) for group in groups]

session.commit()

# to change associate of group groups[1] ( group_id = 'G001', id=2)
# from associate_groups[0] (a_group_id= 'AG000',id=1)
# to associate_groups[2] (a_group_id= 'AG002',id=3)

# soft delete old record
groups[1].deleted_at = datetime.now()
# create new record with new value in attribute associate_group is associate_groups[2]
edited_group = Group(group_id=groups[1].group_id, group_name=groups[1].group_name,
                     associate_group=associate_groups[2])
# edited_group will have id = 5

# but farmers[2]( 'F002') and farmers[3] ('F003') is still linking with soft deleted group record (id =2)
# therefore, we need to update related farmer to them can link with updated record(id=5)

# in plan replace field we don't need make this step.

farmers[2].group = edited_group
farmers[3].group = edited_group

session.add(edited_group)
session.commit()
