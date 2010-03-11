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

    def setupActions(self):
        self.quitA = QAction(self.tr('&Quit'), self)
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
                self.databaseConnected.emit(cd.makeInfoString())
                if (cd.insertTemplateData):
                    self.insertTemplateData()
                    self.lengthUnitModel.reload()
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
        d['Folk1964'] = GrainSizeType(None, unicode('Folk, 1964'),
                                      unicode('Folk, 1964: A Review of Grain-Size Parameters. Sedimentology 6:2:73-93'))
        d['clay'] = GrainSize(d['Krumbein1963'], None, unicode('Clay'), '', 1, d['um'], 4, d['um'])
        d['Test project'] = Project(None, unicode('Test Project'))
        d['Limestone Mudstone'] = Lithology(d['Test project'], None, unicode('Limestone Mudstone'), None, unicode(''), d['clay'])
        d['red'] = Color(d['Test project'], None, unicode('Red'), None, unicode(''))
        d['massive'] = BeddingType(d['Test project'], None, unicode('Massive'), None, unicode(''))
        d['slump'] = SedimentStructure(d['Test project'], None, unicode('Slump'), None, unicode(''))
        d['snail'] = Fossil(d['Test project'], None, unicode('Snail'), None, unicode(''))
        d['sampling'] = CustomSymbol(d['Test project'], None, unicode('Sampling Point'), None, unicode(''))
        d['sharp planar'] = BoundaryType(d['Test project'], None, unicode('Sharp Planar'), None, unicode(''))
        d['oc1'] = PointOfInterest(d['Test project'], None, unicode('Outcrop 1'), None, unicode(''))
        d['Profile 1'] = Profile(d['Test project'], None, unicode('Profile 1'), unicode(''))
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
