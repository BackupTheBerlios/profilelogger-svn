from PyQt4.QtGui import *
from PyQt4.QtCore import *

from sqlalchemy.exc import *

from Persistance.Database import *
from Persistance.ConnectionData import *

from Model.LengthUnit import LengthUnit
from Model.Project import Project

from App.Settings import Settings

from Gui.Dialogs.DatabaseConnectionDialog import DatabaseConnectionDialog
from Gui.Dialogs.DatabaseExceptionDialog import DatabaseExceptionDialog

from Gui.ItemModels.LengthUnitItemModel import LengthUnitItemModel
from Gui.ItemModels.ProjectItemModel import ProjectItemModel
from Gui.ItemModels.SVGItemModel import SVGItemModel
from Gui.ItemModels.GrainSizeTypeItemModel import GrainSizeTypeItemModel
from Gui.ItemModels.GrainSizeItemModel import GrainSizeItemModel
from Gui.ItemModels.LithologyItemModel import LithologyItemModel
from Gui.ItemModels.ColorItemModel import ColorItemModel
from Gui.ItemModels.BeddingTypeItemModel import BeddingTypeItemModel
from Gui.ItemModels.SedimentStructureItemModel import SedimentStructureItemModel
from Gui.ItemModels.FossilItemModel import FossilItemModel
from Gui.ItemModels.CustomSymbolItemModel import CustomSymbolItemModel
from Gui.ItemModels.BoundaryTypeItemModel import BoundaryTypeItemModel
from Gui.ItemModels.PointOfInterestItemModel import PointOfInterestItemModel
from Gui.ItemModels.ProfileItemModel import ProfileItemModel
from Gui.ItemModels.ProfileAssemblyItemModel import ProfileAssemblyItemModel
from Gui.ItemModels.ProfileInProfileAssemblyItemModel import ProfileInProfileAssemblyItemModel
from Gui.ItemModels.BedItemModel import BedItemModel
from Gui.ItemModels.LithologyInBedItemModel import LithologyInBedItemModel
from Gui.ItemModels.ColorInBedItemModel import ColorInBedItemModel
from Gui.ItemModels.BeddingTypeInBedItemModel import BeddingTypeInBedItemModel
from Gui.ItemModels.CustomSymbolInBedItemModel import CustomSymbolInBedItemModel
from Gui.ItemModels.SedimentStructureInBedItemModel import SedimentStructureInBedItemModel
from Gui.ItemModels.FossilInBedItemModel import FossilInBedItemModel
from Gui.ItemModels.GrainSizeInBedItemModel import GrainSizeInBedItemModel
from Gui.ItemModels.BoundaryTypeInBedItemModel import BoundaryTypeInBedItemModel
from Gui.ItemModels.LithologicalUnitTypeItemModel import LithologicalUnitTypeItemModel
from Gui.ItemModels.LithologicalUnitItemModel import LithologicalUnitItemModel
from Gui.ItemModels.StratigraphicUnitTypeItemModel import StratigraphicUnitTypeItemModel
from Gui.ItemModels.StratigraphicUnitItemModel import StratigraphicUnitItemModel
from Gui.ItemModels.TectonicUnitTypeItemModel import TectonicUnitTypeItemModel
from Gui.ItemModels.TectonicUnitItemModel import TectonicUnitItemModel
from Gui.ItemModels.FaciesItemModel import FaciesItemModel
from Gui.ItemModels.OutcropTypeItemModel import OutcropTypeItemModel
from Gui.ItemModels.OutcropTypeInBedItemModel import OutcropTypeInBedItemModel
from Gui.ItemModels.FaciesInBedItemModel import FaciesInBedItemModel
from Gui.ItemModels.LithologicalUnitInBedItemModel import LithologicalUnitInBedItemModel
from Gui.ItemModels.StratigraphicUnitInBedItemModel import StratigraphicUnitInBedItemModel
from Gui.ItemModels.TectonicUnitInBedItemModel import TectonicUnitInBedItemModel
from Gui.ItemModels.GeologicalMeasurementTypeItemModel import GeologicalMeasurementTypeItemModel
from Gui.ItemModels.GeologicalMeasurementInBedItemModel import GeologicalMeasurementInBedItemModel
from Gui.ItemModels.GrainSizeTypeInProfileItemModel import GrainSizeTypeInProfileItemModel

class ProfileLogger(QApplication):
    databaseConnected = pyqtSignal(QString)
    databaseClosed = pyqtSignal(QString)

    def __init__(self, argv):
        QApplication.__init__(self, argv)
        self.setApplicationName('ProfileLogger')
        self.setApplicationVersion('2.0')
        self.setOrganizationName('lochisoft')
        self.setOrganizationDomain('lochisoft.org')

        self.setupActions()
        self.db = Database()
        self.lengthUnitModel = LengthUnitItemModel(self)
        self.projectModel = ProjectItemModel(self)
        self.svgItemModel = SVGItemModel(self)
        self.grainSizeTypeModel = GrainSizeTypeItemModel(self)
        self.grainSizeModel = GrainSizeItemModel(self)
        self.lithologyModel = LithologyItemModel(self)
        self.colorModel = ColorItemModel(self)
        self.beddingTypeModel = BeddingTypeItemModel(self)
        self.sedimentStructureModel = SedimentStructureItemModel(self)
        self.fossilModel = FossilItemModel(self)
        self.customSymbolModel = CustomSymbolItemModel(self)
        self.boundaryTypeModel = BoundaryTypeItemModel(self)
        self.pointOfInterestModel = PointOfInterestItemModel(self)
        self.profileModel = ProfileItemModel(self)
        self.profileAssemblyModel = ProfileAssemblyItemModel(self)
        self.bedModel = BedItemModel(self)
        self.lithologyInBedModel = LithologyInBedItemModel(self)
        self.colorInBedModel = ColorInBedItemModel(self)
        self.beddingTypeInBedModel = BeddingTypeInBedItemModel(self)
        self.customSymbolInBedModel = CustomSymbolInBedItemModel(self)
        self.sedimentStructureInBedModel = SedimentStructureInBedItemModel(self)
        self.fossilInBedModel = FossilInBedItemModel(self)
        self.grainSizeInBedModel = GrainSizeInBedItemModel(self)
        self.boundaryTypeInBedModel = BoundaryTypeInBedItemModel(self)
        self.lithologicalUnitTypeModel = LithologicalUnitTypeItemModel(self)
        self.lithologicalUnitModel = LithologicalUnitItemModel(self)
        self.stratigraphicUnitTypeModel = StratigraphicUnitTypeItemModel(self)
        self.stratigraphicUnitModel = StratigraphicUnitItemModel(self)
        self.tectonicUnitTypeModel = TectonicUnitTypeItemModel(self)
        self.tectonicUnitModel = TectonicUnitItemModel(self)
        self.faciesModel = FaciesItemModel(self)
        self.outcropTypeModel = OutcropTypeItemModel(self)
        self.outcropTypeInBedModel = OutcropTypeInBedItemModel(self)
        self.faciesInBedModel = FaciesInBedItemModel(self)
        self.lithologicalUnitInBedModel = LithologicalUnitInBedItemModel(self)
        self.stratigraphicUnitInBedModel = StratigraphicUnitInBedItemModel(self)
        self.tectonicUnitInBedModel = TectonicUnitInBedItemModel(self)
        self.geologicalMeasurementTypeModel = GeologicalMeasurementTypeItemModel(self)
        self.geologicalMeasurementInBedModel = GeologicalMeasurementInBedItemModel(self)
        self.profileInProfileAssemblyModel = ProfileInProfileAssemblyItemModel(self)
        self.grainSizeTypeInProfileModel = GrainSizeTypeInProfileItemModel(self)

    def setupActions(self):
        self.quitA = QAction(self.tr('&Quit'), self)
        self.quitA.setShortcut(QKeySequence('Ctrl+q'))
        self.quitA.triggered.connect(QApplication.instance().quit);

        self.openDbA = QAction(self.tr('&Open Database...'), self)
        self.openDbA.setShortcut(QKeySequence('Ctrl+o'))
        self.openDbA.triggered.connect(self.onOpenDatabase)

        self.closeDbA = QAction(self.tr('&Close Database...'), self)
        self.closeDbA.triggered.connect(self.onCloseDatabase)
    def getFileActions(self):
        ret = []
        ret.append(self.quitA)
        return ret
    def getToolActions(self):
        ret = []
        return ret
    def getDatabaseActions(self):
        ret = []
        ret.append(self.openDbA)
        return ret;
    def onOpenDatabase(self):
        cd = Settings().loadConnectionData()
        dlg = DatabaseConnectionDialog(cd, self.activeWindow())
        if QDialog.Accepted == dlg.exec_():
            Settings().saveConnectionData(cd)
            try:
                self.db.open(cd)
                if (cd.insertTemplateData):
                    self.insertTemplateData()
                    self.lengthUnitModel.reload()
                self.databaseConnected.emit(cd.makeInfoString())
            except OperationalError, e:
                dlg = DatabaseExceptionDialog(QApplication.activeWindow(), e)
                dlg.exec_()
                
    def insertTemplateData(self):
        d = dict()
        d['um'] = LengthUnit(None, 1, unicode(self.tr('um')))
        d['mm'] = LengthUnit(None, 1000, unicode(self.tr('mm')))
        d['cm'] = LengthUnit(None, 10000, unicode(self.tr('cm')))
        d['dm'] = LengthUnit(None, 100000, unicode(self.tr('dm')))
        d['m'] = LengthUnit(None, 1000000, unicode(self.tr('m')))
        d['Krumbein1963'] = GrainSizeType(None, unicode('Krumbein, 1963'),
                                          unicode('W.C. Krumbein and L.L. Sloss(1963): Stratigraphy and Sedimentation, 2nd edition. Freeman, San Francisco'))
        d['Folk1964'] = GrainSizeType(None, unicode('Folk, 1964 (Wentworth Scale)'),
                                      unicode('Folk, 1964: A Review of Grain-Size Parameters. Sedimentology 6:2:73-93'))
        d['Dunham1962'] = GrainSizeType(None, unicode('Dunhame, 1962'),
                                        unicode('Dunhame, 1962: Classification of carbonate rocks according to depositional texture, in Ham, W.E. ed., Classification of carbonate rocks: Amierican Association of Petroleum Geologists Memoir 1, p. 108-121'))
        d['colloid'] = GrainSize(d['Folk1964'], None, unicode('Colloid'), '', None, None, 1, d['um'], 6, unicode('coll'))
        d['clay'] = GrainSize(d['Folk1964'], None, unicode('Clay'), '', 1, d['um'], 4, d['um'], 12, unicode('clay'))
        d['silt'] = GrainSize(d['Folk1964'], None, unicode('Silt'), '', 4, d['um'], 62, d['um'], 18, unicode('silt'))
        d['vfs'] = GrainSize(d['Folk1964'], None, unicode('Very Fine Sand'), '', 62, d['um'], 125, d['um'], 24, unicode('vfs'))
        d['fs'] = GrainSize(d['Folk1964'], None, unicode('Fine Sand'), '', 125, d['um'], 250, d['um'], 30, unicode('fs'))
        d['mfs'] = GrainSize(d['Folk1964'], None, unicode('Medium Sand'), '', 250, d['um'], 500, d['um'], 36, unicode('ms'))
        d['cs'] = GrainSize(d['Folk1964'], None, unicode('Coarse Sand'), '', 500, d['um'], 1, d['mm'], 42, unicode('cs'))
        d['vcs'] = GrainSize(d['Folk1964'], None, unicode('Very Coarse Sand'), '', 1, d['mm'], 2, d['mm'], 48, unicode('vcs'))
        d['granule'] = GrainSize(d['Folk1964'], None, unicode('Granule'), '', 2, d['mm'], 4, d['mm'], 54, unicode('gr'))
        d['vfp'] = GrainSize(d['Folk1964'], None, unicode('Very Fine Pebble'), '', 4, d['mm'], 8, d['mm'], 60, unicode('vfp'))
        d['fp'] = GrainSize(d['Folk1964'], None, unicode('Fine Pebble'), '', 8, d['mm'], 16, d['mm'], 66, unicode('fp'))
        d['p'] = GrainSize(d['Folk1964'], None, unicode('Pebble'), '', 16, d['mm'], 32, d['mm'], 72, unicode('p'))
        d['cp'] = GrainSize(d['Folk1964'], None, unicode('Coarse Pebble'), '', 32, d['mm'], 64, d['mm'], 78, unicode('cp'))
        d['cobble'] = GrainSize(d['Folk1964'], None, unicode('Cobble'), '', 64, d['mm'], 256, d['mm'], 84, unicode('cobble'))
        d['boulder'] = GrainSize(d['Folk1964'], None, unicode('Boulder'), '', 256, d['mm'], None, None, 96, unicode('boulder'))
        d['mudstone'] = GrainSize(d['Dunham1962'], None, unicode('Mudstone'), '', None, None, None, None, 16, unicode('mud'))
        d['wackestone'] = GrainSize(d['Dunham1962'], None, unicode('Wackestone'), '', None, None, None, None, 32, unicode('wacke'))
        d['packstone'] = GrainSize(d['Dunham1962'], None, unicode('Packstone'), '', None, None, None, None, 48, unicode('pack'))
        d['grainstone'] = GrainSize(d['Dunham1962'], None, unicode('Grainstone'), '', None, None, None, None, 64, unicode('grain'))
        d['boundstone'] = GrainSize(d['Dunham1962'], None, unicode('Boundstone'), '', None, None, None, None, 80, unicode('bound'))
        d['crystalline'] = GrainSize(d['Dunham1962'], None, unicode('Crystalline'), '', None, None, None, None, 96, unicode('cryst'))

        d['Test project'] = Project(None, unicode('Test Project'))
        d['Limestone Mudstone'] = Lithology(d['Test project'], None, unicode('Limestone Mudstone'), None, unicode(''), d['mudstone'])
        d['red'] = Color(d['Test project'], None, unicode('Red'), None, unicode(''))
        d['massive'] = BeddingType(d['Test project'], None, unicode('Massive'), None, unicode(''))
        d['slump'] = SedimentStructure(d['Test project'], None, unicode('Slump'), None, unicode(''))
        d['snail'] = Fossil(d['Test project'], None, unicode('Snail'), None, unicode(''))
        d['sampling'] = CustomSymbol(d['Test project'], None, unicode('Sampling Point'), None, unicode(''))
        d['sharp planar'] = BoundaryType(d['Test project'], None, unicode('Sharp Planar'), None, unicode(''))
        d['oc1'] = PointOfInterest(d['Test project'], None, unicode('Outcrop 1'), None, unicode(''))
        d['Profile 1'] = Profile(d['Test project'], None, unicode('Profile 1'), unicode(''), 0, d['m'],
                                 10,
                                 1, d['m'], 10, d['cm'])
        d['Bed 1'] = Bed(d['Profile 1'], None, 1, d['cm'], 1, unicode('Bed 1'), unicode(''))
        try: 
            s = self.db.session
            for k, v in d.iteritems():
                s.add(v)
            s.commit()
        except SQLError, e:
            dlg = DatabaseExceptionDialog(self.activeWindow(), e)
            dlg.exec_()
            try:
                s.rollback()
            except SQLError, re:
                dlg = DatabaseExceptionDialog(self.activeWindow(), re)
                dlg.exec_()
            

    def onCloseDatabase(self):
        self.databaseClosed.emit()