from sqlalchemy import *
from sqlalchemy.orm import *

from Model.Project import Project
from Model.LengthUnit import LengthUnit
from Model.SVGItem import SVGItem
from Model.Lithology import Lithology
from Model.Color import Color
from Model.BeddingType import BeddingType
from Model.SedimentStructure import SedimentStructure
from Model.Fossil import Fossil
from Model.CustomSymbol import CustomSymbol
from Model.BoundaryType import BoundaryType
from Model.PointOfInterest import PointOfInterest
from Model.Profile import Profile
from Model.GrainSizeType import GrainSizeType
from Model.GrainSize import GrainSize
from Model.LithologicalUnit import LithologicalUnit
from Model.Bed import Bed
from Model.LithologyInBed import LithologyInBed
from Model.ColorInBed import ColorInBed
from Model.BeddingTypeInBed import BeddingTypeInBed
from Model.CustomSymbolInBed import CustomSymbolInBed
from Model.SedimentStructureInBed import SedimentStructureInBed
from Model.FossilInBed import FossilInBed
from Model.GrainSizeInBed import GrainSizeInBed
from Model.BoundaryTypeInBed import BoundaryTypeInBed
from Model.LithologicalUnitType import LithologicalUnitType

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
                                            Column('micrometres', Integer, nullable=False),
                                            Column('name', String, nullable=False, server_default='New Length Unit'),
                                            Column('description', String, nullable=True),
                                            CheckConstraint('micrometres > 0', name='chk_length_units_micrometres_sensible'),
                                            CheckConstraint("name <> ''", name='chk_length_units_name_not_empty'),
                                            UniqueConstraint('micrometres', name='u_length_units_micrometres'),
                                            UniqueConstraint('name', name='u_length_units_name'),
                                            schema=self.schema)

        self.tables['svg_items'] = Table('svg_items', self.metadata,
                                         Column('id', Integer, Sequence('seq_svg_items', schema=self.schema), primary_key=True, nullable=False),
                                         Column('name', String, nullable=False, server_default='New SVG Item'),
                                         Column('description', String, nullable=True),
                                         Column('svg_data', String, nullable=False),
                                         Column('original_path', String, nullable=False),
                                         CheckConstraint("name <> ''", name="chk_svg_items_name_not_empty"),
                                         CheckConstraint("svg_data <> ''", name="chk_svg_items_svg_data_not_empty"),
                                         UniqueConstraint('name', name='u_svg_items_name'),
                                         schema=self.schema)

        self.tables['grain_size_types'] = Table('grain_size_types', self.metadata,
                                                Column('id', Integer, Sequence('seq_grain_size_types', schema=self.schema), primary_key=True, nullable=False),
                                                Column('name', String, nullable=False),
                                                Column('description', String, nullable=True),
                                                CheckConstraint("name <> ''", name='chk_grain_size_types_name_not_empty'),
                                                UniqueConstraint('name', name='u_grain_size_types_name'),
                                                schema=self.schema)

        self.tables['lithological_unit_types'] = Table('lithological_unit_types', self.metadata,
                                                       Column('id', Integer, Sequence('seq_lithological_unit_types', schema=self.schema), primary_key=True, nullable=False),
                                                       Column('name', String, nullable=False),
                                                       Column('description', String, nullable=True),
                                                       CheckConstraint("name <> ''", name='chk_lithological_unit_types_name_not_empty'),
                                                       UniqueConstraint('name', name='u_lithological_unit_types_name'),
                                                       schema=self.schema)

        self.tables['grain_sizes'] = Table('grain_sizes', self.metadata,
                                           Column('id', Integer, Sequence('seq_grain_sizes', schema=self.schema), primary_key=True, nullable=False),
                                           Column('grain_size_type_id', Integer, ForeignKey('%s.grain_size_types.id' % self.schema), nullable=False),
                                           Column('name', String, nullable=False, server_default='New Grain_Size'),
                                           Column('description', String, nullable=True),
                                           Column('min', Integer, nullable=True),
                                           Column('min_length_unit_id', Integer, ForeignKey('%s.length_units.id' % self.schema), nullable=True),
                                           Column('max', Integer, nullable=True),
                                           Column('max_length_unit_id', Integer, ForeignKey('%s.length_units.id' % self.schema), nullable=True),
                                           CheckConstraint("name <> ''", name='chk_grain_sizes_name_not_empty'),
                                           UniqueConstraint('name', name='u_grain_sizes_name'),
                                           schema=self.schema)

        self.tables['lithological_units'] = Table('lithological_units', self.metadata,
                                           Column('id', Integer, Sequence('seq_lithological_units', schema=self.schema), primary_key=True, nullable=False),
                                           Column('lithological_unit_type_id', Integer, ForeignKey('%s.lithological_unit_types.id' % self.schema), nullable=False),
                                           Column('name', String, nullable=False, server_default='New Lithological Unit'),
                                           Column('description', String, nullable=True),
                                           CheckConstraint("name <> ''", name='chk_lithological_units_name_not_empty'),
                                           UniqueConstraint('name', name='u_lithological_units_name'),
                                           schema=self.schema)

        self.tables['projects'] = Table('projects', self.metadata,
                                        Column('id', Integer, Sequence('seq_projects', schema=self.schema), primary_key=True, nullable=False),
                                        Column('name', String, nullable=False, server_default='New Project'),
                                        Column('description', String, nullable=True),
                                        CheckConstraint("name <> ''", name='chk_projects_name_not_empty'),
                                        UniqueConstraint('name', name='u_projects_name'),
                                        schema=self.schema)

        self.tables['lithologies'] = Table('lithologies', self.metadata,
                                           Column('id', Integer, Sequence('seq_lithologies', schema=self.schema), primary_key=True, nullable=False),
                                           Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                           Column('name', String, nullable=False, server_default='New Lithology'),
                                           Column('description', String, nullable=True),
                                           Column('svg_item_id', Integer, ForeignKey('%s.svg_items.id' % self.schema), nullable=True),
                                           Column('default_grain_size_id', Integer, ForeignKey('%s.grain_sizes.id' % self.schema), nullable=True),
                                           CheckConstraint("name <> ''", name='chk_lithologies_name_not_empty'),
                                           UniqueConstraint('name', 'project_id', name='u_lithologies_name_in_project'),
                                           schema=self.schema);

        self.tables['colors'] = Table('colors', self.metadata,
                                      Column('id', Integer, Sequence('seq_colors', schema=self.schema), primary_key=True, nullable=False),
                                      Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                      Column('name', String, nullable=False, server_default='New Color'),
                                      Column('description', String, nullable=True),
                                      Column('svg_item_id', Integer, ForeignKey('%s.svg_items.id' % self.schema), nullable=True),
                                      CheckConstraint("name <> ''", name='chk_colors_name_not_empty'),
                                      UniqueConstraint('name', 'project_id', name='u_colors_name_in_project'),
                                      schema=self.schema);

        self.tables['points_of_interest'] = Table('points_of_interest', self.metadata,
                                      Column('id', Integer, Sequence('seq_points_of_interest', schema=self.schema), primary_key=True, nullable=False),
                                      Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                      Column('name', String, nullable=False, server_default='New Color'),
                                      Column('description', String, nullable=True),
                                      Column('svg_item_id', Integer, ForeignKey('%s.svg_items.id' % self.schema), nullable=True),
                                      CheckConstraint("name <> ''", name='chk_points_of_interest_name_not_empty'),
                                      UniqueConstraint('name', 'project_id', name='u_points_of_interest_name_in_project'),
                                      schema=self.schema);

        self.tables['bedding_types'] = Table('bedding_types', self.metadata,
                                             Column('id', Integer, Sequence('seq_bedding_types', schema=self.schema), primary_key=True, nullable=False),
                                             Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                             Column('name', String, nullable=False, server_default='New Color'),
                                             Column('description', String, nullable=True),
                                             Column('svg_item_id', Integer, ForeignKey('%s.svg_items.id' % self.schema), nullable=True),
                                             CheckConstraint("name <> ''", name='chk_bedding_types_name_not_empty'),
                                             UniqueConstraint('name', 'project_id', name='u_bedding_types_name_in_project'),
                                             schema=self.schema);
        self.tables['sediment_structures'] = Table('sediment_structures', self.metadata,
                                                   Column('id', Integer, Sequence('seq_sediment_structures', schema=self.schema), primary_key=True, nullable=False),
                                                   Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                                   Column('name', String, nullable=False, server_default='New Color'),
                                                   Column('description', String, nullable=True),
                                                   Column('svg_item_id', Integer, ForeignKey('%s.svg_items.id' % self.schema), nullable=True),
                                                   CheckConstraint("name <> ''", name='chk_sediment_structures_name_not_empty'),
                                                   UniqueConstraint('name', 'project_id', name='u_sediment_structures_name_in_project'),
                                                   schema=self.schema);

        self.tables['fossils'] = Table('fossils', self.metadata,
                                       Column('id', Integer, Sequence('seq_fossils', schema=self.schema), primary_key=True, nullable=False),
                                       Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                       Column('name', String, nullable=False, server_default='New Fossil'),
                                       Column('description', String, nullable=True),
                                       Column('svg_item_id', Integer, ForeignKey('%s.svg_items.id' % self.schema), nullable=True),
                                       CheckConstraint("name <> ''", name='chk_fossils_name_not_empty'),
                                       UniqueConstraint('name', 'project_id', name='u_fossils_name_in_project'),
                                       schema=self.schema);

        self.tables['custom_symbols'] = Table('custom_symbols', self.metadata,
                                              Column('id', Integer, Sequence('seq_custom_symbols', schema=self.schema), primary_key=True, nullable=False),
                                              Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                              Column('name', String, nullable=False, server_default='New Fossil'),
                                              Column('description', String, nullable=True),
                                              Column('svg_item_id', Integer, ForeignKey('%s.svg_items.id' % self.schema), nullable=True),
                                              CheckConstraint("name <> ''", name='chk_custom_symbols_name_not_empty'),
                                              UniqueConstraint('name', 'project_id', name='u_custom_symbols_name_in_project'),
                                              schema=self.schema);

        self.tables['boundary_types'] = Table('boundary_types', self.metadata,
                                              Column('id', Integer, Sequence('seq_boundary_types', schema=self.schema), primary_key=True, nullable=False),
                                              Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                              Column('name', String, nullable=False, server_default='New Boundary_Type'),
                                              Column('description', String, nullable=True),
                                              Column('svg_item_id', Integer, ForeignKey('%s.svg_items.id' % self.schema), nullable=True),
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
        self.tables['beds'] = Table('beds', self.metadata,
                                    Column('id', Integer, Sequence('seq_beds', schema=self.schema), primary_key=True, nullable=False),
                                    Column('profile_id', Integer, ForeignKey('%s.profiles.id' % self.schema), nullable=False),
                                    Column('height', Integer, nullable=False),
                                    Column('length_unit_id', Integer, ForeignKey('%s.length_units.id' % self.schema), nullable=False),
                                    Column('bed_number', Integer, nullable=False),
                                    Column('name', String, nullable=False),
                                    CheckConstraint('height > 0', name='chk_beds_height_greater_zero'),
                                    UniqueConstraint('bed_number', 'profile_id', name='u_beds_bed_number_in_profile'),
                                    UniqueConstraint('name', name='u_beds_bed_name'),
                                    schema=self.schema)
        self.tables['lithologies_beds'] = Table('lithologies_beds', self.metadata,
                                                Column('id', Integer, Sequence('seq_lithologies_beds', schema=self.schema), primary_key=True, nullable=False),
                                                Column('begin_from_base', Integer, nullable=False, server_default=text('0')),
                                                Column('end_from_base', Integer, nullable=False, server_default=text('100')),
                                                Column('bed_id', Integer, ForeignKey('%s.beds.id' % self.schema), nullable=False),
                                                Column('lithology_id', Integer, ForeignKey('%s.lithologies.id' % self.schema), nullable=False),
                                                Column('description', String, nullable=True),
                                                Column('name', String, nullable=False),
                                                CheckConstraint('end_from_base > begin_from_base', name='chk_lithologies_beds_end_above_begin'),
                                                CheckConstraint('begin_from_base >= 0 and begin_from_base <= 100', name='chk_lithologies_beds_begin_in_range'),
                                                CheckConstraint('end_from_base >= 0 and end_from_base <= 100', name='chk_lithologies_beds_end_in_range'),
                                                CheckConstraint("name <> ''", name="chk_lithologies_beds_name_not_empty"),
                                                UniqueConstraint('begin_from_base', 'end_from_base', 'bed_id', 'lithology_id', name='u_lithologies_beds'),
                                                schema=self.schema)
        self.tables['colors_beds'] = Table('colors_beds', self.metadata,
                                           Column('id', Integer, Sequence('seq_colors_beds', schema=self.schema), primary_key=True, nullable=False),
                                           Column('begin_from_base', Integer, nullable=False, server_default=text('0')),
                                           Column('end_from_base', Integer, nullable=False, server_default=text('100')),
                                           Column('bed_id', Integer, ForeignKey('%s.beds.id' % self.schema), nullable=False),
                                           Column('color_id', Integer, ForeignKey('%s.colors.id' % self.schema), nullable=False),
                                           Column('description', String, nullable=True),
                                           Column('name', String, nullable=False),
                                           CheckConstraint('end_from_base > begin_from_base', name='chk_colors_beds_end_above_begin'),
                                           CheckConstraint('begin_from_base >= 0 and begin_from_base <= 100', name='chk_colors_beds_begin_in_range'),
                                           CheckConstraint('end_from_base >= 0 and end_from_base <= 100', name='chk_colors_beds_end_in_range'),
                                           CheckConstraint("name <> ''", name="chk_colors_beds_name_not_empty"),
                                           UniqueConstraint('begin_from_base', 'end_from_base', 'bed_id', 'color_id', name='u_colors_beds'),
                                           schema=self.schema)
        self.tables['boundary_types_beds'] = Table('boundary_types_beds', self.metadata,
                                           Column('id', Integer, Sequence('seq_boundary_types_beds', schema=self.schema), primary_key=True, nullable=False),
                                           Column('begin_from_base', Integer, nullable=False, server_default=text('0')),
                                           Column('end_from_base', Integer, nullable=False, server_default=text('100')),
                                           Column('bed_id', Integer, ForeignKey('%s.beds.id' % self.schema), nullable=False),
                                           Column('boundary_type_id', Integer, ForeignKey('%s.boundary_types.id' % self.schema), nullable=False),
                                           Column('description', String, nullable=True),
                                           Column('name', String, nullable=False),
                                           CheckConstraint('end_from_base > begin_from_base', name='chk_boundary_types_beds_end_above_begin'),
                                           CheckConstraint('begin_from_base >= 0 and begin_from_base <= 100', name='chk_boundary_types_beds_begin_in_range'),
                                           CheckConstraint('end_from_base >= 0 and end_from_base <= 100', name='chk_boundary_types_beds_end_in_range'),
                                           CheckConstraint("name <> ''", name="chk_boundary_types_beds_name_not_empty"),
                                           UniqueConstraint('begin_from_base', 'end_from_base', 'bed_id', 'boundary_type_id', name='u_boundary_types_beds'),
                                           schema=self.schema)
        self.tables['bedding_types_beds'] = Table('bedding_types_beds', self.metadata,
                                                  Column('id', Integer, Sequence('seq_bedding_types_beds', schema=self.schema), primary_key=True, nullable=False),
                                                  Column('begin_from_base', Integer, nullable=False, server_default=text('0')),
                                                  Column('end_from_base', Integer, nullable=False, server_default=text('100')),
                                                  Column('bed_id', Integer, ForeignKey('%s.beds.id' % self.schema), nullable=False),
                                                  Column('bedding_type_id', Integer, ForeignKey('%s.bedding_types.id' % self.schema), nullable=False),
                                                  Column('description', String, nullable=True),
                                                  Column('name', String, nullable=False),
                                                  CheckConstraint('end_from_base > begin_from_base', name='chk_bedding_types_beds_end_above_begin'),
                                                  CheckConstraint('begin_from_base >= 0 and begin_from_base <= 100', name='chk_bedding_types_beds_begin_in_range'),
                                                  CheckConstraint('end_from_base >= 0 and end_from_base <= 100', name='chk_bedding_types_beds_end_in_range'),
                                                  CheckConstraint("name <> ''", name="chk_bedding_types_beds_name_not_empty"),
                                                  UniqueConstraint('begin_from_base', 'end_from_base', 'bed_id', 'bedding_type_id', name='u_bedding_types_beds'),
                                                  schema=self.schema)

        self.tables['custom_symbols_beds'] = Table('custom_symbols_beds', self.metadata,
                                                  Column('id', Integer, Sequence('seq_custom_symbols_beds', schema=self.schema), primary_key=True, nullable=False),
                                                  Column('begin_from_base', Integer, nullable=False, server_default=text('0')),
                                                  Column('end_from_base', Integer, nullable=False, server_default=text('100')),
                                                  Column('bed_id', Integer, ForeignKey('%s.beds.id' % self.schema), nullable=False),
                                                  Column('custom_symbol_id', Integer, ForeignKey('%s.custom_symbols.id' % self.schema), nullable=False),
                                                  Column('description', String, nullable=True),
                                                  Column('name', String, nullable=False),
                                                  CheckConstraint('end_from_base > begin_from_base', name='chk_custom_symbols_beds_end_above_begin'),
                                                  CheckConstraint('begin_from_base >= 0 and begin_from_base <= 100', name='chk_custom_symbols_beds_begin_in_range'),
                                                  CheckConstraint('end_from_base >= 0 and end_from_base <= 100', name='chk_custom_symbols_beds_end_in_range'),
                                                  CheckConstraint("name <> ''", name="chk_custom_symbols_beds_name_not_empty"),
                                                  UniqueConstraint('begin_from_base', 'end_from_base', 'bed_id', 'custom_symbol_id', name='u_custom_symbols_beds'),
                                                  schema=self.schema)
        self.tables['sediment_structures_beds'] = Table('sediment_structures_beds', self.metadata,
                                                        Column('id', Integer, Sequence('seq_sediment_structures_beds', schema=self.schema), primary_key=True, nullable=False),
                                                        Column('begin_from_base', Integer, nullable=False, server_default=text('0')),
                                                        Column('end_from_base', Integer, nullable=False, server_default=text('100')),
                                                        Column('bed_id', Integer, ForeignKey('%s.beds.id' % self.schema), nullable=False),
                                                        Column('sediment_structure_id', Integer, ForeignKey('%s.sediment_structures.id' % self.schema), nullable=False),
                                                        Column('description', String, nullable=True),
                                                        Column('name', String, nullable=False),
                                                        CheckConstraint('end_from_base > begin_from_base', name='chk_sediment_structures_beds_end_above_begin'),
                                                        CheckConstraint('begin_from_base >= 0 and begin_from_base <= 100', name='chk_sediment_structures_beds_begin_in_range'),
                                                        CheckConstraint('end_from_base >= 0 and end_from_base <= 100', name='chk_sediment_structures_beds_end_in_range'),
                                                        CheckConstraint("name <> ''", name="chk_sediment_structures_beds_name_not_empty"),
                                                        UniqueConstraint('begin_from_base', 'end_from_base', 'bed_id', 'sediment_structure_id', name='u_sediment_structures_beds'),
                                                        schema=self.schema)
        self.tables['fossils_beds'] = Table('fossils_beds', self.metadata,
                                            Column('id', Integer, Sequence('seq_fossils_beds', schema=self.schema), primary_key=True, nullable=False),
                                            Column('begin_from_base', Integer, nullable=False, server_default=text('0')),
                                            Column('end_from_base', Integer, nullable=False, server_default=text('100')),
                                            Column('bed_id', Integer, ForeignKey('%s.beds.id' % self.schema), nullable=False),
                                            Column('fossil_id', Integer, ForeignKey('%s.fossils.id' % self.schema), nullable=False),
                                            Column('description', String, nullable=True),
                                            Column('name', String, nullable=False),
                                            CheckConstraint('end_from_base > begin_from_base', name='chk_fossils_beds_end_above_begin'),
                                            CheckConstraint('begin_from_base >= 0 and begin_from_base <= 100', name='chk_fossils_beds_begin_in_range'),
                                            CheckConstraint('end_from_base >= 0 and end_from_base <= 100', name='chk_fossils_beds_end_in_range'),
                                            CheckConstraint("name <> ''", name="chk_fossils_beds_name_not_empty"),
                                            UniqueConstraint('begin_from_base', 'end_from_base', 'bed_id', 'fossil_id', name='u_fossils_beds'),
                                            schema=self.schema)
        self.tables['grain_sizes_beds'] = Table('grain_sizes_beds', self.metadata,
                                                Column('id', Integer, Sequence('seq_grain_sizes_beds', schema=self.schema), primary_key=True, nullable=False),
                                                Column('begin_from_base', Integer, nullable=False, server_default=text('0')),
                                                Column('end_from_base', Integer, nullable=False, server_default=text('100')),
                                                Column('bed_id', Integer, ForeignKey('%s.beds.id' % self.schema), nullable=False),
                                                Column('grain_size_id', Integer, ForeignKey('%s.grain_sizes.id' % self.schema), nullable=False),
                                                Column('description', String, nullable=True),
                                                Column('name', String, nullable=False),
                                                CheckConstraint('end_from_base > begin_from_base', name='chk_grain_sizes_beds_end_above_begin'),
                                                CheckConstraint('begin_from_base >= 0 and begin_from_base <= 100', name='chk_grain_sizes_beds_begin_in_range'),
                                                CheckConstraint('end_from_base >= 0 and end_from_base <= 100', name='chk_grain_sizes_beds_end_in_range'),
                                                CheckConstraint("name <> ''", name="chk_grain_sizes_beds_name_not_empty"),
                                                UniqueConstraint('begin_from_base', 'end_from_base', 'bed_id', 'grain_size_id', name='u_grain_sizes_beds'),
                                                schema=self.schema)

    def setupMapping(self):
        clear_mappers()
        mapper(LengthUnit, self.tables['length_units'], properties = {
                'id': self.tables['length_units'].c.id,
                'microMetre': self.tables['length_units'].c.micrometres,
                'name': self.tables['length_units'].c.name,
                'description': self.tables['length_units'].c.description})
        mapper(SVGItem, self.tables['svg_items'], properties = {
                'id': self.tables['svg_items'].c.id,
                'name': self.tables['svg_items'].c.name,
                'description': self.tables['svg_items'].c.description,
                'svgData': self.tables['svg_items'].c.svg_data,
                'originalPath': self.tables['svg_items'].c.original_path
                })
        mapper(GrainSize, self.tables['grain_sizes'], properties = {
                'id': self.tables['grain_sizes'].c.id,
                'name': self.tables['grain_sizes'].c.name,
                'description': self.tables['grain_sizes'].c.description,
                'grainSizeType': relation(GrainSizeType, backref='grainSizes'),
                'minSize': self.tables['grain_sizes'].c.min,
                'minSizeLengthUnit': relation(LengthUnit,
                                              primaryjoin=self.tables['grain_sizes'].c.min_length_unit_id==self.tables['length_units'].c.id),
                'maxSize': self.tables['grain_sizes'].c.max,
                'maxSizeLengthUnit': relation(LengthUnit,
                                              primaryjoin=self.tables['grain_sizes'].c.max_length_unit_id==self.tables['length_units'].c.id)})
        mapper(LithologicalUnit, self.tables['lithological_units'], properties = {
                'id': self.tables['lithological_units'].c.id,
                'name': self.tables['lithological_units'].c.name,
                'description': self.tables['lithological_units'].c.description,
                'lithologicalUnitType': relation(LithologicalUnitType, backref='lithologicalUnits')})
        mapper(GrainSizeType, self.tables['grain_size_types'], properties = {
                'id': self.tables['grain_size_types'].c.id,
                'name': self.tables['grain_size_types'].c.name,
                'description': self.tables['grain_size_types'].c.description})
        mapper(LithologicalUnitType, self.tables['lithological_unit_types'], properties = {
                'id': self.tables['lithological_unit_types'].c.id,
                'name': self.tables['lithological_unit_types'].c.name,
                'description': self.tables['lithological_unit_types'].c.description})
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
                'profiles': relation(Profile, backref='project'),
                'pointsOfInterest': relation(PointOfInterest, backref='project')})
        mapper(Lithology, self.tables['lithologies'], properties = {
                'id': self.tables['lithologies'].c.id,
                'name': self.tables['lithologies'].c.name,
                'description': self.tables['lithologies'].c.description,
                'svgItem': relation(SVGItem, backref='lithologies'),
                'defaultGrainSize': relation(GrainSize)
                })
        mapper(Color, self.tables['colors'], properties = {
                'id': self.tables['colors'].c.id,
                'name': self.tables['colors'].c.name,
                'description': self.tables['colors'].c.description,
                'svgItem': relation(SVGItem, backref='colors'),
                })
        mapper(PointOfInterest, self.tables['points_of_interest'], properties = {
                'id': self.tables['points_of_interest'].c.id,
                'name': self.tables['points_of_interest'].c.name,
                'description': self.tables['points_of_interest'].c.description,
                'svgItem': relation(SVGItem, backref='pointsOfInterest'),
                })
        mapper(BeddingType, self.tables['bedding_types'], properties = {
                'id': self.tables['bedding_types'].c.id,
                'name': self.tables['bedding_types'].c.name,
                'description': self.tables['bedding_types'].c.description,
                'svgItem': relation(SVGItem, backref='beddingTypes')
                })
        mapper(SedimentStructure, self.tables['sediment_structures'], properties = {
                'id': self.tables['sediment_structures'].c.id,
                'name': self.tables['sediment_structures'].c.name,
                'description': self.tables['sediment_structures'].c.description,
                'svgItem': relation(SVGItem, backref='sedimentStructures')
                })
        mapper(Fossil, self.tables['fossils'], properties = {
                'id': self.tables['fossils'].c.id,
                'name': self.tables['fossils'].c.name,
                'description': self.tables['fossils'].c.description,
                'svgItem': relation(SVGItem, backref='fossils')
                })
        mapper(CustomSymbol, self.tables['custom_symbols'], properties = {
                'id': self.tables['custom_symbols'].c.id,
                'name': self.tables['custom_symbols'].c.name,
                'description': self.tables['custom_symbols'].c.description,
                'svgItem': relation(SVGItem, backref='customSymbols')
                })
        
        mapper(BoundaryType, self.tables['boundary_types'], properties = {
                'id': self.tables['boundary_types'].c.id,
                'name': self.tables['boundary_types'].c.name,
                'description': self.tables['boundary_types'].c.description,
                'svgItem': relation(SVGItem, backref='boundaryTypes')
                })
        mapper(Bed, self.tables['beds'], properties = {
                'id': self.tables['beds'].c.id,
                'number': self.tables['beds'].c.bed_number,
                'name':  self.tables['beds'].c.name,
                'height': self.tables['beds'].c.height,
                'lengthUnit': relation(LengthUnit),
                'lithologies': relation(LithologyInBed, backref='bed'),
                'colors': relation(ColorInBed, backref='bed'),
                'beddingTypes': relation(BeddingTypeInBed, backref='bed'),
                'customSymbols': relation(CustomSymbolInBed, backref='bed'),
                'sedimentStructures': relation(SedimentStructureInBed, backref='bed'),
                'fossils': relation(FossilInBed, backref='bed'),
                'grainSizes': relation(GrainSizeInBed, backref='bed'),
                'boundaryTypes': relation(BoundaryTypeInBed, backref='bed')
                })
        mapper(Profile, self.tables['profiles'], properties = {
                'id': self.tables['profiles'].c.id,
                'name': self.tables['profiles'].c.name,
                'description': self.tables['profiles'].c.description,
                'beds': relation(Bed, backref='profile')
                })
        mapper(LithologyInBed, self.tables['lithologies_beds'], properties = {
                'id': self.tables['lithologies_beds'].c.id,
                'begin': self.tables['lithologies_beds'].c.begin_from_base,
                'end': self.tables['lithologies_beds'].c.end_from_base,
                'description':  self.tables['lithologies_beds'].c.description,
                'lithology': relation(Lithology, backref='lithologiesInBed'),
                'name': self.tables['lithologies_beds'].c.name
                })
        mapper(ColorInBed, self.tables['colors_beds'], properties = {
                'id': self.tables['colors_beds'].c.id,
                'begin': self.tables['colors_beds'].c.begin_from_base,
                'end': self.tables['colors_beds'].c.end_from_base,
                'description': self.tables['colors_beds'].c.description,
                'color': relation(Color, backref='colorsInBed'),
                'name': self.tables['colors_beds'].c.name
                })
        mapper(BoundaryTypeInBed, self.tables['boundary_types_beds'], properties = {
                'id': self.tables['boundary_types_beds'].c.id,
                'begin': self.tables['boundary_types_beds'].c.begin_from_base,
                'end': self.tables['boundary_types_beds'].c.end_from_base,
                'description': self.tables['boundary_types_beds'].c.description,
                'boundaryType': relation(BoundaryType, backref='boundaryTypesInBed'),
                'name': self.tables['boundary_types_beds'].c.name
                })
        mapper(BeddingTypeInBed, self.tables['bedding_types_beds'], properties = {
                'id': self.tables['bedding_types_beds'].c.id,
                'begin': self.tables['bedding_types_beds'].c.begin_from_base,
                'end': self.tables['bedding_types_beds'].c.end_from_base,
                'description': self.tables['bedding_types_beds'].c.description,
                'beddingType': relation(BeddingType, backref='beddingTypesInBed'),
                'name': self.tables['bedding_types_beds'].c.name
                })
        mapper(CustomSymbolInBed, self.tables['custom_symbols_beds'], properties = {
                'id': self.tables['custom_symbols_beds'].c.id,
                'begin': self.tables['custom_symbols_beds'].c.begin_from_base,
                'end': self.tables['custom_symbols_beds'].c.end_from_base,
                'description': self.tables['custom_symbols_beds'].c.description,
                'customSymbol': relation(CustomSymbol, backref='customSymbolsInBed'),
                'name': self.tables['custom_symbols_beds'].c.name
                })
        mapper(SedimentStructureInBed, self.tables['sediment_structures_beds'], properties = {
                'id': self.tables['sediment_structures_beds'].c.id,
                'begin': self.tables['sediment_structures_beds'].c.begin_from_base,
                'end': self.tables['sediment_structures_beds'].c.end_from_base,
                'description': self.tables['sediment_structures_beds'].c.description,
                'sedimentStructure': relation(SedimentStructure, backref='sedimentStructuresInBed'),
                'name': self.tables['sediment_structures_beds'].c.name
                })
        mapper(FossilInBed, self.tables['fossils_beds'], properties = {
                'id': self.tables['fossils_beds'].c.id,
                'begin': self.tables['fossils_beds'].c.begin_from_base,
                'end': self.tables['fossils_beds'].c.end_from_base,
                'description': self.tables['fossils_beds'].c.description,
                'fossil': relation(Fossil, backref='fossilsInBed'),
                'name': self.tables['fossils_beds'].c.name
                })
        mapper(GrainSizeInBed, self.tables['grain_sizes_beds'], properties = {
                'id': self.tables['grain_sizes_beds'].c.id,
                'begin': self.tables['grain_sizes_beds'].c.begin_from_base,
                'end': self.tables['grain_sizes_beds'].c.end_from_base,
                'description': self.tables['grain_sizes_beds'].c.description,
                'grainSize': relation(GrainSize, backref='grainSizesInBed'),
                'name': self.tables['grain_sizes_beds'].c.name
                })

    def open(self, connectionData):
        self.schema = unicode(connectionData.schema)
        self.setupTables()
        self.setupMapping()
        self.engine = create_engine(connectionData.makeConnectionString(), echo=True)
        self.engine.connect()
        self.session = create_session(bind=self.engine, autocommit=False, autoflush=False)
        self.metadata.bind = self.engine
        if connectionData.dropSchema:
            self.metadata.drop_all()
        if connectionData.createSchema:
            self.metadata.create_all()

    def begin(self):
        return self.session.begin()
    def commit(self):
        self.session.commit()
    def rollback(self):
        self.session.rollback()
