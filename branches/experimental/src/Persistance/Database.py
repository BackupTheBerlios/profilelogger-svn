from sqlalchemy import *
from sqlalchemy.orm import *

from Model.ColumnInProfile import ColumnInProfile
from Model.ProfileColumn import ProfileColumn
from Model.ProfileAssembly import ProfileAssembly
from Model.Project import Project
from Model.LengthUnit import LengthUnit
from Model.SVGItem import SVGItem
from Model.Lithology import Lithology
from Model.Color import Color
from Model.Facies import Facies
from Model.BeddingType import BeddingType
from Model.SedimentStructure import SedimentStructure
from Model.Fossil import Fossil
from Model.CustomSymbol import CustomSymbol
from Model.BoundaryType import BoundaryType
from Model.PointOfInterest import PointOfInterest
from Model.Profile import Profile
from Model.GrainSizeType import GrainSizeType
from Model.GrainSize import GrainSize
from Model.Bed import Bed
from Model.ProfileInProfileAssembly import ProfileInProfileAssembly
from Model.LithologyInBed import LithologyInBed
from Model.ColorInBed import ColorInBed
from Model.BeddingTypeInBed import BeddingTypeInBed
from Model.CustomSymbolInBed import CustomSymbolInBed
from Model.SedimentStructureInBed import SedimentStructureInBed
from Model.FossilInBed import FossilInBed
from Model.GrainSizeInBed import GrainSizeInBed
from Model.BoundaryTypeInBed import BoundaryTypeInBed
from Model.LithologicalUnitType import LithologicalUnitType
from Model.LithologicalUnit import LithologicalUnit
from Model.StratigraphicUnitType import StratigraphicUnitType
from Model.StratigraphicUnit import StratigraphicUnit
from Model.TectonicUnitType import TectonicUnitType
from Model.TectonicUnit import TectonicUnit
from Model.OutcropType import OutcropType
from Model.OutcropTypeInBed import OutcropTypeInBed
from Model.FaciesInBed import FaciesInBed
from Model.LithologicalUnitInBed import LithologicalUnitInBed
from Model.StratigraphicUnitInBed import StratigraphicUnitInBed
from Model.TectonicUnitInBed import TectonicUnitInBed
from Model.GeologicalMeasurementType import GeologicalMeasurementType
from Model.GeologicalMeasurementInBed import GeologicalMeasurementInBed
from Model.GrainSizeTypeInProfile import *

class Database:
    def __init__(self):
        self.engine = None
        self.metadata = None
        self.session = None
        self.schema = None

    def setupTables(self):
        self.metadata = MetaData()
        self.tables = dict()
        self.tables['profiles_profile_columns'] = Table('profiles_profile_columns', self.metadata,
                                                        Column('id', Integer, Sequence('seq_profiles_profile_columns', schema=self.schema), nullable=False, primary_key=True),
                                                        Column('profile_id', ForeignKey('%s.profiles.id' % self.schema), nullable=False),
                                                        Column('profile_column_id', ForeignKey('%s.profile_columns.id' % self.schema), nullable=False),
                                                        Column('position', Integer, nullable=False),
                                                        Column('width', Integer, nullable=False, server_default='50'),
                                                        schema=self.schema)
        self.tables['profile_columns'] = Table('profile_columns', self.metadata,
                                               Column('id', Integer, Sequence('seq_profile_columns', schema=self.schema), nullable=False, primary_key=True),
                                               Column('name', String, nullable=False),
                                               Column('description', String, nullable=True),
                                               Column('header_class_name', String, nullable=False),
                                               Column('bed_part_class_name', String, nullable=False),
                                               UniqueConstraint('name', name='u_profile_columns'),
                                               schema=self.schema)
        self.tables['grain_size_types_profiles'] = Table('grain_size_types_profiles', self.metadata,
                                                         Column('id', Integer, Sequence('seq_grain_size_types_profiles', schema=self.schema), primary_key=True, nullable=False),
                                                         Column('grain_size_type_id', Integer, ForeignKey('%s.grain_size_types.id' % self.schema), nullable=False),
                                                         Column('profile_id', Integer, ForeignKey('%s.profiles.id' % self.schema), nullable=False),
                                                         UniqueConstraint('grain_size_type_id', 'profile_id', name='u_grain_size_types_profiles'),
                                                         schema=self.schema)
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
        self.tables['profiles_profile_assemblies'] = Table('profiles_profile_assemblies', self.metadata,
                                                           Column('id', Integer, Sequence('seq_profiles_profile_assemblies', schema=self.schema), primary_key=True, nullable=False),
                                                           Column('name', String, nullable=False, server_default='New Profile in Profile Assembly'),
                                                           Column('show_big_height_marks', Boolean, nullable=False),
                                                           Column('show_small_height_marks', Boolean, nullable=False),
                                                           Column('show_big_height_marks_labels', Boolean, nullable=False),
                                                           Column('show_small_height_marks_labels', Boolean, nullable=False),
                                                           Column('show_lithology', Boolean, nullable=False),
                                                           Column('show_lithology_number_in_lithology', Boolean, nullable=False),
                                                           Column('show_grain_size', Boolean, nullable=False),
                                                           Column('show_bedding_type_in_grain_size_column', Boolean, nullable=False),
                                                           Column('show_bedding_type_in_column', Boolean, nullable=False),
                                                           Column('show_bedding_type_number', Boolean, nullable=False),
                                                           Column('show_bed_number_in_lithology', Boolean, nullable=False),
                                                           Column('show_bed_number_in_column', Boolean, nullable=False),
                                                           Column('show_bed_height_in_lithology', Boolean, nullable=False),
                                                           Column('show_bed_height_in_column', Boolean, nullable=False),
                                                           Column('show_fossils_in_column', Boolean, nullable=False),
                                                           Column('show_fossils_in_bedding_type', Boolean, nullable=False),
                                                           Column('show_fossils_in_lithology', Boolean, nullable=False),
                                                           Column('show_sediment_structures_in_column', Boolean, nullable=False),
                                                           Column('show_sediment_structures_in_bedding_type', Boolean, nullable=False),
                                                           Column('show_sediment_structures_in_lithology', Boolean, nullable=False),
                                                           Column('show_custom_symbols_in_column', Boolean, nullable=False),
                                                           Column('show_custom_symbols_in_bedding_type', Boolean, nullable=False),
                                                           Column('show_custom_symbols_in_lithology', Boolean, nullable=False),
                                                           Column('show_facies_in_column', Boolean, nullable=False),
                                                           Column('show_lithological_unit_in_column', Boolean, nullable=False),
                                                           Column('show_tectonic_unit_in_column', Boolean, nullable=False),
                                                           Column('show_stratigraphic_unit_in_column', Boolean, nullable=False),
                                                           Column('bed_numbers_column_width', Integer, nullable=False),
                                                           Column('bed_heights_column_width', Integer, nullable=False),
                                                           Column('bedding_types_column_width', Integer, nullable=False),
                                                           Column('lithologies_column_width', Integer, nullable=False),
                                                           Column('grain_sizes_column_width', Integer, nullable=False),
                                                           Column('custom_symbols_column_width', Integer, nullable=False),
                                                           Column('fossils_column_width', Integer, nullable=False),
                                                           Column('sediment_structures_column_width', Integer, nullable=False),
                                                           Column('custom_symbols_column_width', Integer, nullable=False),
                                                           Column('facies_column_width', Integer, nullable=False),
                                                           Column('lithological_units_column_width', Integer, nullable=False),
                                                           Column('tectonic_units_column_width', Integer, nullable=False),
                                                           Column('stratigraphic_units_column_width', Integer, nullable=False),
                                                           Column('scale', Integer, nullable=False),
                                                           Column('big_marks_distance_value', Integer, nullable=False),
                                                           Column('small_marks_distance_value', Integer, nullable=False),
                                                           Column('big_marks_distance_length_unit_id', Integer, ForeignKey('%s.length_units.id' % self.schema), nullable=True),
                                                           Column('small_marks_distance_length_unit_id', Integer, ForeignKey('%s.length_units.id' % self.schema), nullable=True),
                                                           Column('first_bed_id', Integer, ForeignKey('%s.beds.id' % self.schema), nullable=True),
                                                           Column('last_bed_id', Integer, ForeignKey('%s.beds.id' % self.schema), nullable=True),
                                                           Column('description', String, nullable=True),
                                                           Column('profile_assembly_id', Integer, ForeignKey('%s.profile_assemblies.id' % self.schema), nullable=False),
                                                           Column('profile_id', Integer, ForeignKey('%s.profiles.id' % self.schema), nullable=False), 
                                                           CheckConstraint("name <> ''", name='chk_profiles_profile_assemblies_name_not_empty'),
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
        self.tables['geological_measurement_types'] = Table('geological_measurement_types', self.metadata,
                                                            Column('id', Integer, Sequence('seq_geological_measurement_types', schema=self.schema), primary_key=True, nullable=False),
                                                            Column('name', String, nullable=False),
                                                            Column('description', String, nullable=True),
                                                            Column('is_plane', Boolean, nullable=False),
                                                            CheckConstraint("name <> ''", name='chk_geological_measurement_types_name_not_empty'),
                                                            UniqueConstraint('name', name='u_geological_measurement_types_name'),
                                                            schema=self.schema)
        self.tables['geological_measurements_beds'] = Table('geological_measurements_beds', self.metadata,
                                                            Column('id', Integer, Sequence('seq_geological_measurements_beds', schema=self.schema), primary_key=True, nullable=False),
                                                            Column('name', String, nullable=False),
                                                            Column('begin_from_base', Integer, nullable=False),
                                                            Column('end_from_base', Integer, nullable=False),
                                                            Column('strike', Integer, nullable=False),
                                                            Column('dip', Integer, nullable=False),
                                                            Column('description', String, nullable=True),
                                                            Column('bed_id', ForeignKey('%s.beds.id' % self.schema), nullable=False),
                                                            Column('geological_measurement_type_id', ForeignKey('%s.geological_measurement_types.id' % self.schema), nullable=False),
                                                            CheckConstraint("name <> ''", name='chk_geological_measurements_in_beds_name'),
                                                            CheckConstraint('strike >= 0 and strike <= 360', name='chk_geological_measurements_in_beds_strike_valid'),
                                                            CheckConstraint('dip >= 0 and dip <= 90', name='chk_geological_measurements_in_beds_dip_valid'),
                                                            schema=self.schema)
        self.tables['grain_size_types'] = Table('grain_size_types', self.metadata,
                                                Column('id', Integer, Sequence('seq_grain_size_types', schema=self.schema), primary_key=True, nullable=False),
                                                Column('name', String, nullable=False),
                                                Column('description', String, nullable=True),
                                                CheckConstraint("name <> ''", name='chk_grain_size_types_name_not_empty'),
                                                UniqueConstraint('name', name='u_grain_size_types_name'),
                                                schema=self.schema)
        self.tables['grain_sizes'] = Table('grain_sizes', self.metadata,
                                           Column('id', Integer, Sequence('seq_grain_sizes', schema=self.schema), primary_key=True, nullable=False),
                                           Column('grain_size_type_id', Integer, ForeignKey('%s.grain_size_types.id' % self.schema), nullable=False),
                                           Column('name', String, nullable=False, server_default='New Grain_Size'),
                                           Column('short_name', String, nullable=False, server_default=''),
                                           Column('description', String, nullable=True),
                                           Column('min', Integer, nullable=True),
                                           Column('min_length_unit_id', Integer, ForeignKey('%s.length_units.id' % self.schema), nullable=True),
                                           Column('max', Integer, nullable=True),
                                           Column('max_length_unit_id', Integer, ForeignKey('%s.length_units.id' % self.schema), nullable=True),
                                           Column('percent_from_minimum', Integer, nullable=False, server_default='0'),
                                           CheckConstraint("name <> ''", name='chk_grain_sizes_name_not_empty'),
                                           CheckConstraint('percent_from_minimum between 0 and 100', name='chk_grain_size_percent_from_minimum_in_range'),
                                           UniqueConstraint('name', name='u_grain_sizes_name'),
                                           UniqueConstraint('short_name', name='u_grain_sizes_short_name'),
                                           schema=self.schema)
        self.tables['outcrop_types'] = Table('outcrop_types', self.metadata,
                                             Column('id', Integer, Sequence('seq_outcrop_types', schema=self.schema), primary_key=True, nullable=False),
                                             Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                             Column('name', String, nullable=False, server_default='New Color'),
                                             Column('description', String, nullable=True),
                                             Column('svg_item_id', Integer, ForeignKey('%s.svg_items.id' % self.schema), nullable=True),
                                             CheckConstraint("name <> ''", name='chk_outcrop_types_name_not_empty'),
                                             UniqueConstraint('name', 'project_id', name='u_outcrop_types_name_in_project'),
                                             schema=self.schema);
        self.tables['lithological_unit_types'] = Table('lithological_unit_types', self.metadata,
                                                       Column('id', Integer, Sequence('seq_lithological_unit_types', schema=self.schema), primary_key=True, nullable=False),
                                                       Column('name', String, nullable=False),
                                                       Column('description', String, nullable=True),
                                                       CheckConstraint("name <> ''", name='chk_lithological_unit_types_name_not_empty'),
                                                       UniqueConstraint('name', name='u_lithological_unit_types_name'),
                                                       schema=self.schema)
        self.tables['stratigraphic_unit_types'] = Table('stratigraphic_unit_types', self.metadata,
                                                       Column('id', Integer, Sequence('seq_stratigraphic_unit_types', schema=self.schema), primary_key=True, nullable=False),
                                                       Column('name', String, nullable=False),
                                                       Column('description', String, nullable=True),
                                                       CheckConstraint("name <> ''", name='chk_stratigraphic_unit_types_name_not_empty'),
                                                       UniqueConstraint('name', name='u_stratigraphic_unit_types_name'),
                                                       schema=self.schema)
        self.tables['stratigraphic_units'] = Table('stratigraphic_units', self.metadata,
                                                   Column('id', Integer, Sequence('seq_stratigraphic_units', schema=self.schema), primary_key=True, nullable=False),
                                                   Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                                   Column('name', String, nullable=False, server_default='New Stratigraphic Unit'),                                                 
                                                   Column('description', String, nullable=True),
                                                   Column('svg_item_id', Integer, ForeignKey('%s.svg_items.id' % self.schema), nullable=True),
                                                   Column('stratigraphic_unit_type_id', Integer, ForeignKey('%s.stratigraphic_unit_types.id' % self.schema), nullable=False),
                                                   CheckConstraint("name <> ''", name='chk_stratigraphic_units_name_not_empty'),
                                                   UniqueConstraint('name', name='u_stratigraphic_units_name'),
                                                   schema=self.schema)
        self.tables['tectonic_unit_types'] = Table('tectonic_unit_types', self.metadata,
                                                       Column('id', Integer, Sequence('seq_tectonic_unit_types', schema=self.schema), primary_key=True, nullable=False),
                                                       Column('name', String, nullable=False),
                                                       Column('description', String, nullable=True),
                                                       CheckConstraint("name <> ''", name='chk_tectonic_unit_types_name_not_empty'),
                                                       UniqueConstraint('name', name='u_tectonic_unit_types_name'),
                                                       schema=self.schema)
        self.tables['tectonic_units'] = Table('tectonic_units', self.metadata,
                                              Column('id', Integer, Sequence('seq_tectonic_units', schema=self.schema), primary_key=True, nullable=False),
                                              Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                              Column('name', String, nullable=False, server_default='New Tectonic Unit'),                                                 
                                              Column('description', String, nullable=True),
                                              Column('svg_item_id', Integer, ForeignKey('%s.svg_items.id' % self.schema), nullable=True),
                                              Column('tectonic_unit_type_id', Integer, ForeignKey('%s.tectonic_unit_types.id' % self.schema), nullable=False),
                                              CheckConstraint("name <> ''", name='chk_tectonic_units_name_not_empty'),
                                              UniqueConstraint('name', name='u_tectonic_units_name'),
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
                                           schema=self.schema)
        self.tables['colors'] = Table('colors', self.metadata,
                                      Column('id', Integer, Sequence('seq_colors', schema=self.schema), primary_key=True, nullable=False),
                                      Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                      Column('name', String, nullable=False, server_default='New Color'),
                                      Column('description', String, nullable=True),
                                      Column('svg_item_id', Integer, ForeignKey('%s.svg_items.id' % self.schema), nullable=True),
                                      CheckConstraint("name <> ''", name='chk_colors_name_not_empty'),
                                      UniqueConstraint('name', 'project_id', name='u_colors_name_in_project'),
                                      schema=self.schema)
        self.tables['lithological_units'] = Table('lithological_units', self.metadata,
                                                  Column('id', Integer, Sequence('seq_lithological_units', schema=self.schema), primary_key=True, nullable=False),
                                                  Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                                  Column('name', String, nullable=False, server_default='New Lithological Unit'),                                                 
                                                  Column('description', String, nullable=True),
                                                  Column('svg_item_id', Integer, ForeignKey('%s.svg_items.id' % self.schema), nullable=True),
                                                  Column('lithological_unit_type_id', Integer, ForeignKey('%s.lithological_unit_types.id' % self.schema), nullable=False),
                                                  CheckConstraint("name <> ''", name='chk_lithological_units_name_not_empty'),
                                                  UniqueConstraint('name', name='u_lithological_units_name'),
                                                  schema=self.schema)
        self.tables['facies'] = Table('facies', self.metadata,
                                      Column('id', Integer, Sequence('seq_facies', schema=self.schema), primary_key=True, nullable=False),
                                      Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                      Column('name', String, nullable=False, server_default='New Facie'),
                                      Column('description', String, nullable=True),
                                      Column('svg_item_id', Integer, ForeignKey('%s.svg_items.id' % self.schema), nullable=True),
                                      CheckConstraint("name <> ''", name='chk_facies_name_not_empty'),
                                      UniqueConstraint('name', 'project_id', name='u_facies_name_in_project'),
                                      schema=self.schema)
        self.tables['points_of_interest'] = Table('points_of_interest', self.metadata,
                                                  Column('id', Integer, Sequence('seq_points_of_interest', schema=self.schema), primary_key=True, nullable=False),
                                                  Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                                  Column('name', String, nullable=False, server_default='New Color'),
                                                  Column('description', String, nullable=True),
                                                  Column('svg_item_id', Integer, ForeignKey('%s.svg_items.id' % self.schema), nullable=True),
                                                  CheckConstraint("name <> ''", name='chk_points_of_interest_name_not_empty'),
                                                  UniqueConstraint('name', 'project_id', name='u_points_of_interest_name_in_project'),
                                                  schema=self.schema)
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
                                        Column('start_height_value', Integer, nullable=False, server_default='0'),
                                        Column('start_height_length_unit_id', Integer, ForeignKey('%s.length_units.id' % self.schema), nullable=False),
                                        Column('description', String, nullable=True),
                                        Column('scale', Integer, nullable=False, server_default='1'),
                                        Column('big_marks_distance_value', Integer, nullable=False, server_default='0'),
                                        Column('big_marks_distance_length_unit_id', Integer, ForeignKey('%s.length_units.id' % self.schema), nullable=False),
                                        Column('small_marks_distance_value', Integer, nullable=False, server_default='0'),
                                        Column('small_marks_distance_length_unit_id', Integer, ForeignKey('%s.length_units.id' % self.schema), nullable=False),
                                        Column('cols_in_legend', Integer, nullable=False, server_default='10'),
                                        CheckConstraint("name <> ''", name='chk_profiles_name_not_empty'),
                                        CheckConstraint('cols_in_legend between 1 and 50', name='chk_profiles_cols_in_legend_sensible'),
                                        UniqueConstraint('name', 'project_id', name='u_profiles_name_in_project'),
                                        schema=self.schema);
        self.tables['profile_assemblies'] = Table('profile_assemblies', self.metadata,
                                                  Column('id', Integer, Sequence('seq_profile_assemblies', schema=self.schema), primary_key=True, nullable=False),
                                                  Column('project_id', Integer, ForeignKey('%s.projects.id' % self.schema), nullable=False),
                                                  Column('name', String, nullable=False, server_default='New Profile'),
                                                  Column('description', String, nullable=True),
                                                  CheckConstraint("name <> ''", name='chk_profile_assemblies_name_not_empty'),
                                                  UniqueConstraint('name', 'project_id', name='u_profile_assemblies_name_in_project'),
                                                  schema=self.schema);
        self.tables['beds'] = Table('beds', self.metadata,
                                    Column('id', Integer, Sequence('seq_beds', schema=self.schema), primary_key=True, nullable=False),
                                    Column('profile_id', Integer, ForeignKey('%s.profiles.id' % self.schema), nullable=False),
                                    Column('height', Integer, nullable=False),
                                    Column('length_unit_id', Integer, ForeignKey('%s.length_units.id' % self.schema), nullable=False),
                                    Column('bed_number', Integer, nullable=False),
                                    Column('name', String, nullable=False),
                                    CheckConstraint('height > 0', name='chk_beds_height_greater_zero'),
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
        self.tables['lithological_units_beds'] = Table('lithological_units_beds', self.metadata,
                                                       Column('id', Integer, Sequence('seq_lithological_units_beds', schema=self.schema), primary_key=True, nullable=False),
                                                       Column('begin_from_base', Integer, nullable=False, server_default=text('0')),
                                                       Column('end_from_base', Integer, nullable=False, server_default=text('100')),
                                                       Column('bed_id', Integer, ForeignKey('%s.beds.id' % self.schema), nullable=False),
                                                       Column('lithological_unit_id', Integer, ForeignKey('%s.lithological_units.id' % self.schema), nullable=False),
                                                       Column('description', String, nullable=True),
                                                       Column('name', String, nullable=False),
                                                       CheckConstraint('end_from_base > begin_from_base', name='chk_lithological_units_beds_end_above_begin'),
                                                       CheckConstraint('begin_from_base >= 0 and begin_from_base <= 100', name='chk_lithological_units_beds_begin_in_range'),
                                                       CheckConstraint('end_from_base >= 0 and end_from_base <= 100', name='chk_lithological_units_beds_end_in_range'),
                                                       CheckConstraint("name <> ''", name="chk_lithological_units_beds_name_not_empty"),
                                                       UniqueConstraint('begin_from_base', 'end_from_base', 'bed_id', 'lithological_unit_id', name='u_lithologicalUnits_beds'),
                                                       schema=self.schema)
        self.tables['tectonic_units_beds'] = Table('tectonic_units_beds', self.metadata,
                                                   Column('id', Integer, Sequence('seq_tectonic_units_beds', schema=self.schema), primary_key=True, nullable=False),
                                                   Column('begin_from_base', Integer, nullable=False, server_default=text('0')),
                                                   Column('end_from_base', Integer, nullable=False, server_default=text('100')),
                                                   Column('bed_id', Integer, ForeignKey('%s.beds.id' % self.schema), nullable=False),
                                                   Column('tectonic_unit_id', Integer, ForeignKey('%s.tectonic_units.id' % self.schema), nullable=False),
                                                   Column('description', String, nullable=True),
                                                   Column('name', String, nullable=False),
                                                   CheckConstraint('end_from_base > begin_from_base', name='chk_tectonic_units_beds_end_above_begin'),
                                                   CheckConstraint('begin_from_base >= 0 and begin_from_base <= 100', name='chk_tectonic_units_beds_begin_in_range'),
                                                   CheckConstraint('end_from_base >= 0 and end_from_base <= 100', name='chk_tectonic_units_beds_end_in_range'),
                                                   CheckConstraint("name <> ''", name="chk_tectonic_units_beds_name_not_empty"),
                                                   UniqueConstraint('begin_from_base', 'end_from_base', 'bed_id', 'tectonic_unit_id', name='u_tectonicUnits_beds'),
                                                   schema=self.schema)
        self.tables['stratigraphic_units_beds'] = Table('stratigraphic_units_beds', self.metadata,
                                                        Column('id', Integer, Sequence('seq_stratigraphic_units_beds', schema=self.schema), primary_key=True, nullable=False),
                                                        Column('begin_from_base', Integer, nullable=False, server_default=text('0')),
                                                        Column('end_from_base', Integer, nullable=False, server_default=text('100')),
                                                        Column('bed_id', Integer, ForeignKey('%s.beds.id' % self.schema), nullable=False),
                                                        Column('stratigraphic_unit_id', Integer, ForeignKey('%s.stratigraphic_units.id' % self.schema), nullable=False),
                                                        Column('description', String, nullable=True),
                                                        Column('name', String, nullable=False),
                                                        CheckConstraint('end_from_base > begin_from_base', name='chk_stratigraphic_units_beds_end_above_begin'),
                                                        CheckConstraint('begin_from_base >= 0 and begin_from_base <= 100', name='chk_stratigraphic_units_beds_begin_in_range'),
                                                        CheckConstraint('end_from_base >= 0 and end_from_base <= 100', name='chk_stratigraphic_units_beds_end_in_range'),
                                                        CheckConstraint("name <> ''", name="chk_stratigraphic_units_beds_name_not_empty"),
                                                        UniqueConstraint('begin_from_base', 'end_from_base', 'bed_id', 'stratigraphic_unit_id', name='u_stratigraphicUnits_beds'),
                                                        schema=self.schema)
        self.tables['outcrop_types_beds'] = Table('outcrop_types_beds', self.metadata,
                                           Column('id', Integer, Sequence('seq_outcrop_types_beds', schema=self.schema), primary_key=True, nullable=False),
                                           Column('begin_from_base', Integer, nullable=False, server_default=text('0')),
                                           Column('end_from_base', Integer, nullable=False, server_default=text('100')),
                                           Column('bed_id', Integer, ForeignKey('%s.beds.id' % self.schema), nullable=False),
                                           Column('outcrop_type_id', Integer, ForeignKey('%s.outcrop_types.id' % self.schema), nullable=False),
                                           Column('description', String, nullable=True),
                                           Column('name', String, nullable=False),
                                           CheckConstraint('end_from_base > begin_from_base', name='chk_outcrop_types_beds_end_above_begin'),
                                           CheckConstraint('begin_from_base >= 0 and begin_from_base <= 100', name='chk_outcrop_types_beds_begin_in_range'),
                                           CheckConstraint('end_from_base >= 0 and end_from_base <= 100', name='chk_outcrop_types_beds_end_in_range'),
                                           CheckConstraint("name <> ''", name="chk_outcrop_types_beds_name_not_empty"),
                                           UniqueConstraint('begin_from_base', 'end_from_base', 'bed_id', 'outcrop_type_id', name='u_outcrop_types_beds'),
                                           schema=self.schema)
        self.tables['facies_beds'] = Table('facies_beds', self.metadata,
                                           Column('id', Integer, Sequence('seq_facies_beds', schema=self.schema), primary_key=True, nullable=False),
                                           Column('begin_from_base', Integer, nullable=False, server_default=text('0')),
                                           Column('end_from_base', Integer, nullable=False, server_default=text('100')),
                                           Column('bed_id', Integer, ForeignKey('%s.beds.id' % self.schema), nullable=False),
                                           Column('facies_id', Integer, ForeignKey('%s.facies.id' % self.schema), nullable=False),
                                           Column('description', String, nullable=True),
                                           Column('name', String, nullable=False),
                                           CheckConstraint('end_from_base > begin_from_base', name='chk_facies_beds_end_above_begin'),
                                           CheckConstraint('begin_from_base >= 0 and begin_from_base <= 100', name='chk_facies_beds_begin_in_range'),
                                           CheckConstraint('end_from_base >= 0 and end_from_base <= 100', name='chk_facies_beds_end_in_range'),
                                           CheckConstraint("name <> ''", name="chk_facies_beds_name_not_empty"),
                                           UniqueConstraint('begin_from_base', 'end_from_base', 'bed_id', 'facies_id', name='u_facies_beds'),
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
        mapper(ColumnInProfile, self.tables['profiles_profile_columns'], properties = {
                'id': self.tables['profiles_profile_columns'].c.id,
                'position': self.tables['profiles_profile_columns'].c.position,
                'width': self.tables['profiles_profile_columns'].c.width,
                'profile': relation(Profile, backref='columns'),
                'profileColumn': relation(ProfileColumn)
                },
               order_by=self.tables['profiles_profile_columns'].c.position)
        mapper(ProfileColumn, self.tables['profile_columns'], properties = {
                'id': self.tables['profile_columns'].c.id,
                'name': self.tables['profile_columns'].c.name,
                'description': self.tables['profile_columns'].c.description,
                'headerClassName': self.tables['profile_columns'].c.header_class_name,
                'bedPartClassName': self.tables['profile_columns'].c.bed_part_class_name
                })
        mapper(GrainSizeTypeInProfile, self.tables['grain_size_types_profiles'], properties = {
                'id': self.tables['grain_size_types_profiles'].c.id,
                'grainSizeType': relation(GrainSizeType),
                'profile': relation(Profile, backref='grainSizeTypes')
                })
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
                'shortName': self.tables['grain_sizes'].c.short_name,
                'description': self.tables['grain_sizes'].c.description,
                'grainSizeType': relation(GrainSizeType, backref='grainSizes'),
                'minSize': self.tables['grain_sizes'].c.min,
                'percentFromMinimum': self.tables['grain_sizes'].c.percent_from_minimum,
                'minSizeLengthUnit': relation(LengthUnit,
                                              primaryjoin=self.tables['grain_sizes'].c.min_length_unit_id==self.tables['length_units'].c.id),
                'maxSize': self.tables['grain_sizes'].c.max,
                'maxSizeLengthUnit': relation(LengthUnit,
                                              primaryjoin=self.tables['grain_sizes'].c.max_length_unit_id==self.tables['length_units'].c.id)},
               order_by=self.tables['grain_sizes'].c.percent_from_minimum)
        mapper(GrainSizeType, self.tables['grain_size_types'], properties = {
                'id': self.tables['grain_size_types'].c.id,
                'name': self.tables['grain_size_types'].c.name,
                'description': self.tables['grain_size_types'].c.description})
        mapper(GeologicalMeasurementType, self.tables['geological_measurement_types'], properties = {
                'id': self.tables['geological_measurement_types'].c.id,
                'name': self.tables['geological_measurement_types'].c.name,
                'description': self.tables['geological_measurement_types'].c.description,
                'isPlane': self.tables['geological_measurement_types'].c.is_plane})
        mapper(LithologicalUnitType, self.tables['lithological_unit_types'], properties = {
                'id': self.tables['lithological_unit_types'].c.id,
                'name': self.tables['lithological_unit_types'].c.name,
                'description': self.tables['lithological_unit_types'].c.description})
        mapper(LithologicalUnit, self.tables['lithological_units'], properties = {
                'id': self.tables['lithological_units'].c.id,
                'name': self.tables['lithological_units'].c.name,
                'description': self.tables['lithological_units'].c.description,
                'svgItem': relation(SVGItem, backref='lithologicalUnits'),
                'lithologicalUnitType': relation(LithologicalUnitType, backref='lithologicalUnits')})
        mapper(StratigraphicUnitType, self.tables['stratigraphic_unit_types'], properties = {
                'id': self.tables['stratigraphic_unit_types'].c.id,
                'name': self.tables['stratigraphic_unit_types'].c.name,
                'description': self.tables['stratigraphic_unit_types'].c.description})
        mapper(StratigraphicUnit, self.tables['stratigraphic_units'], properties = {
                'id': self.tables['stratigraphic_units'].c.id,
                'name': self.tables['stratigraphic_units'].c.name,
                'svgItem': relation(SVGItem, backref='stratigraphicUnits'),
                'description': self.tables['stratigraphic_units'].c.description,
                'stratigraphicUnitType': relation(StratigraphicUnitType, backref='stratigraphicUnits')})
        mapper(TectonicUnitType, self.tables['tectonic_unit_types'], properties = {
                'id': self.tables['tectonic_unit_types'].c.id,
                'name': self.tables['tectonic_unit_types'].c.name,
                'description': self.tables['tectonic_unit_types'].c.description})
        mapper(TectonicUnit, self.tables['tectonic_units'], properties = {
                'id': self.tables['tectonic_units'].c.id,
                'name': self.tables['tectonic_units'].c.name,
                'svgItem': relation(SVGItem, backref='tectonicUnits'),
                'description': self.tables['tectonic_units'].c.description,
                'tectonicUnitType': relation(TectonicUnitType, backref='tectonicUnits')})
        mapper(Project, self.tables['projects'], properties = {
                'id': self.tables['projects'].c.id,
                'name': self.tables['projects'].c.name,
                'description': self.tables['projects'].c.description,
                'lithologies': relation(Lithology, backref='project'),
                'colors': relation(Color, backref='project'),
                'outcropTypes': relation(OutcropType, backref='project'),
                'facies': relation(Facies, backref='project'),
                'beddingTypes': relation(BeddingType, backref='project'),
                'sedimentStructures': relation(SedimentStructure, backref='project'),
                'fossils': relation(Fossil, backref='project'),
                'customSymbols': relation(CustomSymbol, backref='project'),
                'boundaryTypes': relation(BoundaryType, backref='project'),
                'profiles': relation(Profile, backref='project'),
                'pointsOfInterest': relation(PointOfInterest, backref='project'),
                'lithologicalUnits': relation(LithologicalUnit, backref='project'),
                'stratigraphicUnits': relation(StratigraphicUnit, backref='project'),
                'tectonicUnits': relation(TectonicUnit, backref='project'),
                'profileAssemblies': relation(ProfileAssembly, backref='project')})
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
                'svgItem': relation(SVGItem, backref='colors')
                })
        mapper(Facies, self.tables['facies'], properties = {
                'id': self.tables['facies'].c.id,
                'name': self.tables['facies'].c.name,
                'description': self.tables['facies'].c.description,
                'svgItem': relation(SVGItem, backref='facies'),
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
        mapper(Bed, self.tables['beds'],
               order_by=self.tables['beds'].c.bed_number,
               properties = {
                'id': self.tables['beds'].c.id,
                'number': self.tables['beds'].c.bed_number,
                'name':  self.tables['beds'].c.name,
                'height': self.tables['beds'].c.height,
                'lengthUnit': relation(LengthUnit),
                'lithologies': relation(LithologyInBed, 
                                        backref='bed', cascade="all, delete"),
                'colors': relation(ColorInBed, backref='bed', 
                                   cascade="all, delete"),
                'outcropTypes': relation(OutcropTypeInBed, backref='bed', 
                                   cascade="all, delete"),
                'facies': relation(FaciesInBed, backref='bed', 
                                   cascade="all, delete"),
                'lithologicalUnits': relation(LithologicalUnitInBed, backref='bed', 
                                              cascade="all, delete"),
                'stratigraphicUnits': relation(StratigraphicUnitInBed, backref='bed', 
                                               cascade="all, delete"),
                'tectonicUnits': relation(TectonicUnitInBed, backref='bed', 
                                          cascade="all, delete"),
                'beddingTypes': relation(BeddingTypeInBed, backref='bed', 
                                         cascade="all, delete"),
                'customSymbols': relation(CustomSymbolInBed, backref='bed', 
                                          cascade="all, delete"),
                'sedimentStructures': relation(SedimentStructureInBed, backref='bed', 
                                               cascade="all, delete"),
                'fossils': relation(FossilInBed, backref='bed', 
                                    cascade="all, delete"),
                'grainSizes': relation(GrainSizeInBed, backref='bed', 
                                       cascade="all, delete"),
                'boundaryTypes': relation(BoundaryTypeInBed, backref='bed', 
                                          cascade="all, delete"),
                'geologicalMeasurements': relation(GeologicalMeasurementInBed, backref='bed', 
                                                   cascade="all, delete")},
               order_by=[desc(self.tables['beds'].c.bed_number)])
        mapper(Profile, self.tables['profiles'], properties = {
                'id': self.tables['profiles'].c.id,
                'name': self.tables['profiles'].c.name,
                'description': self.tables['profiles'].c.description,
                'beds': relation(Bed, backref='profile', cascade="all, delete"),
                'startHeightValue': self.tables['profiles'].c.start_height_value,
                'startHeightLengthUnit': relation(LengthUnit,
                                                  primaryjoin=self.tables['profiles'].c.start_height_length_unit_id==self.tables['length_units'].c.id),
                'scale': self.tables['profiles'].c.scale,
                'colsInLegend': self.tables['profiles'].c.cols_in_legend,
                'bigMarksDistanceValue': self.tables['profiles'].c.big_marks_distance_value,
                'bigMarksDistanceLengthUnit': relation(LengthUnit,
                                               primaryjoin=self.tables['profiles'].c.big_marks_distance_length_unit_id==self.tables['length_units'].c.id),
                'smallMarksDistanceValue': self.tables['profiles'].c.small_marks_distance_value,
                'smallMarksDistanceLengthUnit': relation(LengthUnit,
                                                 primaryjoin=self.tables['profiles'].c.small_marks_distance_length_unit_id==self.tables['length_units'].c.id)
                })
        mapper(ProfileAssembly, self.tables['profile_assemblies'], properties = {
                'id': self.tables['profile_assemblies'].c.id,
                'name': self.tables['profile_assemblies'].c.name,
                'description': self.tables['profile_assemblies'].c.description
                })
        mapper(ProfileInProfileAssembly, self.tables['profiles_profile_assemblies'], properties = {
                'id': self.tables['profiles_profile_assemblies'].c.id,
                'name': self.tables['profiles_profile_assemblies'].c.name,
                'showBigHeightMarks': self.tables['profiles_profile_assemblies'].c.show_big_height_marks,
                'showSmallHeightMarks': self.tables['profiles_profile_assemblies'].c.show_small_height_marks,
                'showBigHeightMarkLabels': self.tables['profiles_profile_assemblies'].c.show_big_height_marks_labels,
                'showSmallHeightMarkLabels': self.tables['profiles_profile_assemblies'].c.show_small_height_marks_labels,
                'showLithology': self.tables['profiles_profile_assemblies'].c.show_lithology,
                'showLithologyNumberInLithology': self.tables['profiles_profile_assemblies'].c.show_lithology_number_in_lithology,
                'showGrainSize': self.tables['profiles_profile_assemblies'].c.show_grain_size,
                'showBeddingTypeInGrainSizeColumn': self.tables['profiles_profile_assemblies'].c.show_bedding_type_in_grain_size_column,
                'showBeddingTypeInColumn': self.tables['profiles_profile_assemblies'].c.show_bedding_type_in_column,
                'showBeddingTypeNumber': self.tables['profiles_profile_assemblies'].c.show_bedding_type_number,
                'showBedNumberInLithology': self.tables['profiles_profile_assemblies'].c.show_bed_number_in_lithology,
                'showBedNumberInColumn': self.tables['profiles_profile_assemblies'].c.show_bed_number_in_column,
                'showBedHeightInLithology': self.tables['profiles_profile_assemblies'].c.show_bed_height_in_lithology,
                'showBedHeightInColumn': self.tables['profiles_profile_assemblies'].c.show_bed_height_in_column,
                'showFossilsInColumn': self.tables['profiles_profile_assemblies'].c.show_fossils_in_column,
                'showFossilsInBeddingType': self.tables['profiles_profile_assemblies'].c.show_fossils_in_bedding_type,
                'showFossilsInLithology': self.tables['profiles_profile_assemblies'].c.show_fossils_in_lithology,
                'showSedimentStructuresInColumn': self.tables['profiles_profile_assemblies'].c.show_sediment_structures_in_column,
                'showSedimentStructuresInBeddingType': self.tables['profiles_profile_assemblies'].c.show_sediment_structures_in_bedding_type,
                'showSedimentStructuresInLithology': self.tables['profiles_profile_assemblies'].c.show_sediment_structures_in_lithology,
                'showCustomSymbolsInColumn': self.tables['profiles_profile_assemblies'].c.show_custom_symbols_in_column,
                'showCustomSymbolsInBeddingType': self.tables['profiles_profile_assemblies'].c.show_custom_symbols_in_bedding_type,
                'showCustomSymbolsInLithology': self.tables['profiles_profile_assemblies'].c.show_custom_symbols_in_lithology,
                'showFaciesInColumn': self.tables['profiles_profile_assemblies'].c.show_facies_in_column,
                'showLithologicalUnitInColumn': self.tables['profiles_profile_assemblies'].c.show_lithological_unit_in_column,
                'showTectonicUnitInColumn': self.tables['profiles_profile_assemblies'].c.show_tectonic_unit_in_column,
                'showStratigraphicUnitInColumn': self.tables['profiles_profile_assemblies'].c.show_stratigraphic_unit_in_column,
                'bedNumbersColumnWidth': self.tables['profiles_profile_assemblies'].c.bed_numbers_column_width,
                'beddingTypesColumnWidth': self.tables['profiles_profile_assemblies'].c.bedding_types_column_width,
                'bedHeightsColumnWidth': self.tables['profiles_profile_assemblies'].c.bed_heights_column_width,
                'lithologiesColumnWidth': self.tables['profiles_profile_assemblies'].c.lithologies_column_width,
                'grainSizesColumnWidth': self.tables['profiles_profile_assemblies'].c.grain_sizes_column_width,
                'fossilsColumnWidth': self.tables['profiles_profile_assemblies'].c.fossils_column_width,
                'sedimentStructuresColumnWidth': self.tables['profiles_profile_assemblies'].c.sediment_structures_column_width,
                'customSymbolsColumnWidth': self.tables['profiles_profile_assemblies'].c.custom_symbols_column_width,
                'faciesColumnWidth': self.tables['profiles_profile_assemblies'].c.facies_column_width,
                'lithologicalUnitsColumnWidth': self.tables['profiles_profile_assemblies'].c.lithological_units_column_width,
                'tectonicUnitsColumnWidth': self.tables['profiles_profile_assemblies'].c.tectonic_units_column_width,
                'stratigraphicUnitsColumnWidth': self.tables['profiles_profile_assemblies'].c.stratigraphic_units_column_width,
                'scale': self.tables['profiles_profile_assemblies'].c.scale,
                'bigHeightMarksDistanceValue': self.tables['profiles_profile_assemblies'].c.big_marks_distance_value,
                'bigHeightMarksDistanceLengthUnit': relation(LengthUnit,
                                                         primaryjoin=self.tables['profiles_profile_assemblies'].c.big_marks_distance_length_unit_id==self.tables['length_units'].c.id),
                'smallHeightMarksDistanceValue': self.tables['profiles_profile_assemblies'].c.small_marks_distance_value,
                'smallHeightMarksDistanceLengthUnit': relation(LengthUnit,
                                                         primaryjoin=self.tables['profiles_profile_assemblies'].c.small_marks_distance_length_unit_id==self.tables['length_units'].c.id),
                'firstBedInView': relation(Bed,
                                           primaryjoin=self.tables['profiles_profile_assemblies'].c.first_bed_id==self.tables['beds'].c.id),
                'lastBedInView': relation(Bed,
                                          primaryjoin=self.tables['profiles_profile_assemblies'].c.last_bed_id==self.tables['beds'].c.id),
                'description': self.tables['profiles_profile_assemblies'].c.description,
                'profileAssembly': relation(ProfileAssembly, backref='profilesInProfileAssembly'),
                'profile': relation(Profile, backref='profileInProfileAssemblies')
                })
        mapper(LithologyInBed, self.tables['lithologies_beds'], properties = {
                'id': self.tables['lithologies_beds'].c.id,
                'begin': self.tables['lithologies_beds'].c.begin_from_base,
                'end': self.tables['lithologies_beds'].c.end_from_base,
                'description':  self.tables['lithologies_beds'].c.description,
                'lithology': relation(Lithology, backref='lithologiesInBed'),
                'name': self.tables['lithologies_beds'].c.name
                })
        mapper(GeologicalMeasurementInBed, self.tables['geological_measurements_beds'], properties = {
                'id': self.tables['geological_measurements_beds'].c.id,
                'name': self.tables['geological_measurements_beds'].c.name,
                'begin': self.tables['geological_measurements_beds'].c.begin_from_base,
                'end': self.tables['geological_measurements_beds'].c.end_from_base,
                'strike': self.tables['geological_measurements_beds'].c.strike,
                'dip': self.tables['geological_measurements_beds'].c.dip,
                'description': self.tables['geological_measurements_beds'].c.description,
                'geologicalMeasurementType': relation(GeologicalMeasurementType, backref='geologicalMeasurements')
                })
        mapper(ColorInBed, self.tables['colors_beds'], properties = {
                'id': self.tables['colors_beds'].c.id,
                'begin': self.tables['colors_beds'].c.begin_from_base,
                'end': self.tables['colors_beds'].c.end_from_base,
                'description': self.tables['colors_beds'].c.description,
                'color': relation(Color, backref='colorsInBed'),
                'name': self.tables['colors_beds'].c.name
                })
        mapper(LithologicalUnitInBed, self.tables['lithological_units_beds'], properties = {
                'id': self.tables['lithological_units_beds'].c.id,
                'begin': self.tables['lithological_units_beds'].c.begin_from_base,
                'end': self.tables['lithological_units_beds'].c.end_from_base,
                'description': self.tables['lithological_units_beds'].c.description,
                'lithologicalUnit': relation(LithologicalUnit, backref='lithologicalUnitsInBed'),
                'name': self.tables['lithological_units_beds'].c.name
                })
        mapper(TectonicUnitInBed, self.tables['tectonic_units_beds'], properties = {
                'id': self.tables['tectonic_units_beds'].c.id,
                'begin': self.tables['tectonic_units_beds'].c.begin_from_base,
                'end': self.tables['tectonic_units_beds'].c.end_from_base,
                'description': self.tables['tectonic_units_beds'].c.description,
                'tectonicUnit': relation(TectonicUnit, backref='tectonicUnitsInBed'),
                'name': self.tables['tectonic_units_beds'].c.name
                })
        mapper(StratigraphicUnitInBed, self.tables['stratigraphic_units_beds'], properties = {
                'id': self.tables['stratigraphic_units_beds'].c.id,
                'begin': self.tables['stratigraphic_units_beds'].c.begin_from_base,
                'end': self.tables['stratigraphic_units_beds'].c.end_from_base,
                'description': self.tables['stratigraphic_units_beds'].c.description,
                'stratigraphicUnit': relation(StratigraphicUnit, backref='stratigraphicUnitsInBed'),
                'name': self.tables['stratigraphic_units_beds'].c.name
                })
        mapper(OutcropType, self.tables['outcrop_types'], properties = {
                'id': self.tables['outcrop_types'].c.id,
                'name': self.tables['outcrop_types'].c.name,
                'description': self.tables['outcrop_types'].c.description,
                'svgItem': relation(SVGItem, backref='outcropTypes'),
                })
        mapper(OutcropTypeInBed, self.tables['outcrop_types_beds'], properties = {
                'id': self.tables['outcrop_types_beds'].c.id,
                'begin': self.tables['outcrop_types_beds'].c.begin_from_base,
                'end': self.tables['outcrop_types_beds'].c.end_from_base,
                'description': self.tables['outcrop_types_beds'].c.description,
                'outcropType': relation(OutcropType, backref='outcrop_typesInBed'),
                'name': self.tables['outcrop_types_beds'].c.name
                })
        mapper(FaciesInBed, self.tables['facies_beds'], properties = {
                'id': self.tables['facies_beds'].c.id,
                'begin': self.tables['facies_beds'].c.begin_from_base,
                'end': self.tables['facies_beds'].c.end_from_base,
                'description': self.tables['facies_beds'].c.description,
                'facies': relation(Facies, backref='faciesInBed'),
                'name': self.tables['facies_beds'].c.name
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
                },
               order_by=self.tables['grain_sizes_beds'].c.begin_from_base)

    def open(self, connectionData):
        self.schema = unicode(connectionData.schema)
        self.setupTables()
        self.setupMapping()
        self.engine = create_engine(connectionData.makeConnectionString(), echo=True)
        self.engine.connect()
        self.session = create_session(bind=self.engine, autocommit=False, autoflush=False)
        self.metadata.bind = self.engine
        if connectionData.createSchema:
            self.metadata.create_all()

    def begin(self):
        return self.session.begin()
    def commit(self):
        self.session.commit()
    def rollback(self):
        self.session.rollback()
