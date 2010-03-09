from sqlalchemy import *
from sqlalchemy.orm import *

from Model.Project import Project
from Model.LengthUnit import LengthUnit
from Model.Lithology import Lithology
from Model.Color import Color
from Model.BeddingType import BeddingType
from Model.SedimentStructure import SedimentStructure
from Model.Fossil import Fossil
from Model.CustomSymbol import CustomSymbol
from Model.BoundaryType import BoundaryType
from Model.Profile import Profile

class Database:
    def __init__(self):
        self.engine = None
        self.metadata = None
        self.session = None
        self.schema = None

    def setupTables(self):
        self.metadata = MetaData()
        self.tables = dict()

        self.tables['length_units'] = Table('length_units', self.metadata,
                                            Column('id', Integer, Sequence('seq_length_units', schema=self.schema), primary_key=True, nullable=False),
                                            Column('millimetres', Integer, nullable=False),
                                            Column('name', String, nullable=False),
                                            CheckConstraint('millimetres > 0', name='chk_length_units_millimetres_sensible'),
                                            CheckConstraint('name is not null', name='chk_length_units_name_not_null'),
                                            CheckConstraint("name <> ''", name='chk_length_units_name_not_empty'),
                                            UniqueConstraint('millimetres', name='u_length_units_millimetres'),
                                            UniqueConstraint('name', name='u_length_units_name'),
                                            schema=self.schema)

        self.tables['projects'] = Table('projects', self.metadata,
                                        Column('id', Integer, Sequence('seq_projects', schema=self.schema), primary_key=True, nullable=False),
                                        Column('name', String, nullable=False, server_default='New Project'),
                                        Column('description', String, nullable=True),
                                        CheckConstraint('name is not null', name='chk_projects_name_not_null'),
                                        CheckConstraint("name <> ''", name='chk_projects_name_not_empty'),
                                        UniqueConstraint('name', name='u_projects_name'),
                                        schema=self.schema)

        self.tables['lithologies'] = Table('lithologies', self.metadata,
                                           Column('id', Integer, Sequence('seq_lithologies', schema=self.schema), primary_key=True, nullable=False),
                                           Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                           Column('name', String, nullable=False, server_default='New Lithology'),
                                           Column('description', String, nullable=True),
                                           CheckConstraint("name <> ''", name='chk_lithologies_name_not_empty'),
                                           UniqueConstraint('name', 'project_id', name='u_lithologies_name_in_project'),
                                           schema=self.schema);

        self.tables['colors'] = Table('colors', self.metadata,
                                      Column('id', Integer, Sequence('seq_colors', schema=self.schema), primary_key=True, nullable=False),
                                      Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                      Column('name', String, nullable=False, server_default='New Color'),
                                      Column('description', String, nullable=True),
                                      CheckConstraint("name <> ''", name='chk_colors_name_not_empty'),
                                      UniqueConstraint('name', 'project_id', name='u_colors_name_in_project'),
                                      schema=self.schema);

        self.tables['bedding_types'] = Table('bedding_types', self.metadata,
                                             Column('id', Integer, Sequence('seq_bedding_types', schema=self.schema), primary_key=True, nullable=False),
                                             Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                             Column('name', String, nullable=False, server_default='New Color'),
                                             Column('description', String, nullable=True),
                                             CheckConstraint("name <> ''", name='chk_bedding_types_name_not_empty'),
                                             UniqueConstraint('name', 'project_id', name='u_bedding_types_name_in_project'),
                                             schema=self.schema);
        self.tables['sediment_structures'] = Table('sediment_structures', self.metadata,
                                                   Column('id', Integer, Sequence('seq_sediment_structures', schema=self.schema), primary_key=True, nullable=False),
                                                   Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                                   Column('name', String, nullable=False, server_default='New Color'),
                                                   Column('description', String, nullable=True),
                                                   CheckConstraint("name <> ''", name='chk_sediment_structures_name_not_empty'),
                                                   UniqueConstraint('name', 'project_id', name='u_sediment_structures_name_in_project'),
                                                   schema=self.schema);

        self.tables['fossils'] = Table('fossils', self.metadata,
                                       Column('id', Integer, Sequence('seq_fossils', schema=self.schema), primary_key=True, nullable=False),
                                       Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                       Column('name', String, nullable=False, server_default='New Fossil'),
                                       Column('description', String, nullable=True),
                                       CheckConstraint("name <> ''", name='chk_fossils_name_not_empty'),
                                       UniqueConstraint('name', 'project_id', name='u_fossils_name_in_project'),
                                       schema=self.schema);

        self.tables['custom_symbols'] = Table('custom_symbols', self.metadata,
                                              Column('id', Integer, Sequence('seq_custom_symbols', schema=self.schema), primary_key=True, nullable=False),
                                              Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                              Column('name', String, nullable=False, server_default='New Fossil'),
                                              Column('description', String, nullable=True),
                                              CheckConstraint("name <> ''", name='chk_custom_symbols_name_not_empty'),
                                              UniqueConstraint('name', 'project_id', name='u_custom_symbols_name_in_project'),
                                              schema=self.schema);

        self.tables['boundary_types'] = Table('boundary_types', self.metadata,
                                              Column('id', Integer, Sequence('seq_boundary_types', schema=self.schema), primary_key=True, nullable=False),
                                              Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                              Column('name', String, nullable=False, server_default='New Boundary_Type'),
                                              Column('description', String, nullable=True),
                                              CheckConstraint("name <> ''", name='chk_boundary_types_name_not_empty'),
                                              UniqueConstraint('name', 'project_id', name='u_boundary_types_name_in_project'),
                                              schema=self.schema);

        self.tables['profiles'] = Table('profiles', self.metadata,
                                       Column('id', Integer, Sequence('seq_profiles', schema=self.schema), primary_key=True, nullable=False),
                                       Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                       Column('name', String, nullable=False, server_default='New Profile'),
                                       Column('description', String, nullable=True),
                                       CheckConstraint("name <> ''", name='chk_profiles_name_not_empty'),
                                       UniqueConstraint('name', 'project_id', name='u_profiles_name_in_project'),
                                       schema=self.schema);

    def setupMapping(self):
        mapper(Project, self.tables['projects'], properties = {
                'id': self.tables['projects'].c.id,
                'name': self.tables['projects'].c.name,
                'description': self.tables['projects'].c.description,
                'lithologies': relation(Lithology, backref='project'),
                'colors': relation(Color, backref='project'),
                'beddingTypes': relation(BeddingType, backref='project'),
                'sedimentStructures': relation(SedimentStructure, backref='project'),
                'colors': relation(Color, backref='project'),
                'fossils': relation(Fossil, backref='project'),
                'customSymbols': relation(CustomSymbol, backref='project'),
                'boundaryTypes': relation(BoundaryType, backref='project'),
                'profiles': relation(Profile, backref='project')})
        mapper(LengthUnit, self.tables['length_units'], properties = {
                'id': self.tables['length_units'].c.id,
                'milliMetre': self.tables['length_units'].c.millimetres,
                'name': self.tables['length_units'].c.name})
        mapper(Lithology, self.tables['lithologies'], properties = {
                'id': self.tables['lithologies'].c.id,
                'name': self.tables['lithologies'].c.name,
                'description': self.tables['lithologies'].c.description
                })
        mapper(Color, self.tables['colors'], properties = {
                'id': self.tables['colors'].c.id,
                'name': self.tables['colors'].c.name,
                'description': self.tables['colors'].c.description
                })
        mapper(BeddingType, self.tables['bedding_types'], properties = {
                'id': self.tables['bedding_types'].c.id,
                'name': self.tables['bedding_types'].c.name,
                'description': self.tables['bedding_types'].c.description
                })
        mapper(SedimentStructure, self.tables['sediment_structures'], properties = {
                'id': self.tables['sediment_structures'].c.id,
                'name': self.tables['sediment_structures'].c.name,
                'description': self.tables['sediment_structures'].c.description
                })
        mapper(Fossil, self.tables['fossils'], properties = {
                'id': self.tables['fossils'].c.id,
                'name': self.tables['fossils'].c.name,
                'description': self.tables['fossils'].c.description
                })
        mapper(CustomSymbol, self.tables['custom_symbols'], properties = {
                'id': self.tables['custom_symbols'].c.id,
                'name': self.tables['custom_symbols'].c.name,
                'description': self.tables['custom_symbols'].c.description
                })
        mapper(BoundaryType, self.tables['boundary_types'], properties = {
                'id': self.tables['boundary_types'].c.id,
                'name': self.tables['boundary_types'].c.name,
                'description': self.tables['boundary_types'].c.description
                })
        mapper(Profile, self.tables['profiles'], properties = {
                'id': self.tables['profiles'].c.id,
                'name': self.tables['profiles'].c.name,
                'description': self.tables['profiles'].c.description
                })
        
    def open(self, connectionData):
        self.schema = connectionData.schema
        self.setupTables()
        self.setupMapping()
        print "opening... %s" % connectionData.makeConnectionString()
        self.engine = create_engine(connectionData.makeConnectionString(), echo=True)
        self.engine.connect()
        self.session = create_session(bind=self.engine, autocommit=False, autoflush=False)
        self.metadata.bind = self.engine
        if connectionData.dropSchema:
            self.metadata.drop_all()
        if connectionData.createSchema:
            self.metadata.create_all()

    def begin(self):
        return self.session
    def commit(self):
        self.session.commit()
    def rollback(self):
        self.session.rollback()
