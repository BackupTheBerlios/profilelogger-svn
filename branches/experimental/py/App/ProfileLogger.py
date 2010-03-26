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
from Gui.ItemModels.PenStyleItemModel import PenStyleItemModel
from Gui.ItemModels.PenJoinStyleItemModel import PenJoinStyleItemModel
from Gui.ItemModels.PenCapStyleItemModel import PenCapStyleItemModel
from Gui.ItemModels.BrushStyleItemModel import BrushStyleItemModel
from Gui.ItemModels.DrawingItemModel import DrawingItemModel
from Gui.ItemModels.PenItemModel import PenItemModel
from Gui.ItemModels.BrushItemModel import BrushItemModel
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
        self.penStyleModel = PenStyleItemModel(self)
        self.penJoinStyleModel = PenJoinStyleItemModel(self)
        self.penCapStyleModel = PenCapStyleItemModel(self)
        self.brushStyleModel = BrushStyleItemModel(self)
        self.drawingModel = DrawingItemModel(self)
        self.penModel = PenItemModel(self)
        self.brushModel = BrushItemModel(self)
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
        d['Qt.NoPen'] = PenStyle(None, unicode(self.tr("No Pen")), '', 0)
        d['Qt.SolidLine'] = PenStyle(None, unicode(self.tr("Solid Line")), '', 1)
        d['Qt.DashLine'] = PenStyle(None, unicode(self.tr("Dash Line")), '', 2)
        d['Qt.DotLine'] = PenStyle(None, unicode(self.tr("Dot Line")), '', 3)
        d['Qt.DashDotLine'] = PenStyle(None, unicode(self.tr("Dash Dot Line")), '', 4)
        d['Qt.DashDoDottLine'] = PenStyle(None, unicode(self.tr("Dash Dot Dot Line")), '', 5)
        d['Qt.FlatCap'] = PenCapStyle(None, unicode(self.tr("Flat Cap")), '', 0x00)
        d['Qt.SquareCap'] = PenCapStyle(None, unicode(self.tr("Square Cap")), '', 0x10)
        d['Qt.RoundCap'] = PenCapStyle(None, unicode(self.tr("Round Cap")), '', 0x20)
        d['Qt.MiterJoin'] = PenJoinStyle(None, unicode(self.tr("Miter Join")), '', 0x00)
        d['Qt.BevelJoin'] = PenJoinStyle(None, unicode(self.tr("Bevel Join")), '', 0x40)
        d['Qt.RoundJoin'] = PenJoinStyle(None, unicode(self.tr("Round Join")), '', 0x80)
        d['Qt.SvgMiterJoin'] = PenJoinStyle(None, unicode(self.tr("SVG Miter Join")), '', 0x100)
        d['Qt.NoBrush'] = BrushStyle(None, unicode(self.tr("No brush pattern")), '', 0)
        d['Qt.SolidPattern'] = BrushStyle(None, unicode(self.tr("Uniform Color")), '', 1)
        d['Qt.Dense1Pattern'] = BrushStyle(None, unicode(self.tr("Extremely dense brush pattern")), '', 2)
        d['Qt.Dense2Pattern'] = BrushStyle(None, unicode(self.tr("Very dense brush pattern")), '', 3)
        d['Qt.Dense3Pattern'] = BrushStyle(None, unicode(self.tr("Somewhat dense brush apttern")), '', 4)
        d['Qt.Dense4Pattern'] = BrushStyle(None, unicode(self.tr("Half dense brush pattern")), '', 5)
        d['Qt.Dense5Pattern'] = BrushStyle(None, unicode(self.tr("Somewhat sparse brush pattern")), '', 6)
        d['Qt.Dense6Pattern'] = BrushStyle(None, unicode(self.tr("Very sparse brush pattern")), '', 7)
        d['Qt.Dense7Pattern'] = BrushStyle(None, unicode(self.tr("Extremely sparse brush pattern")), '', 8)
        d['Qt.HorPattern'] = BrushStyle(None, unicode(self.tr("Horizontal Lines")), '', 9)
        d['Qt.VerPattern'] = BrushStyle(None, unicode(self.tr("Vertical Lines")), '', 10)
        d['Qt.CrossPattern'] = BrushStyle(None, unicode(self.tr("Crossing horizontal and vertical lines")), '', 11)
        d['Qt.BDiagPattern'] = BrushStyle(None, unicode(self.tr("Backward diagonal lines")), '', 12)
        d['Qt.FDiagPattern'] = BrushStyle(None, unicode(self.tr("Forward diagonal lines")), '', 13)
        d['Qt.DiagCrossPattern'] = BrushStyle(None, unicode(self.tr("Diagonal crossing lines")), '', 14)
        d['artistic pen'] = Pen(None, unicode(self.tr("Artistic Pen")), '', 0, 0, 0, 255, 1, d['Qt.RoundCap'], d['Qt.RoundJoin'], d['Qt.SolidLine'])
        d['test drawing'] = Drawing(None, unicode(self.tr("Test Drawing")))
        d['straight line'] = StraightLine(None, d['test drawing'], 0, 0, 20, 20, d['artistic pen'])
        d['rectangle'] = Rectangle(None, d['test drawing'], 0, 0, 0, 0, 40, 40, d['artistic pen'])
        d['ellipsis'] = Ellipse(None, d['test drawing'], 0, 0, 0, 0, 40, 40, d['artistic pen'])
        d['polygon'] = Polygon(None, d['test drawing'], 0, 0, [], d['artistic pen'])
        d['polygon'].polygonPoints = [PolygonPoint(None, d['polygon'], 0, 0, 0),
                                      PolygonPoint(None, d['polygon'], 10, 10, 1),
                                      PolygonPoint(None, d['polygon'], 20, 10, 2)]
        d['painter path'] = PainterPath(None, d['test drawing'], 0, 0, [], d['artistic pen'])
        d['painter path'].painterPathPoints = [PainterPathPoint(None, d['painter path'], 0, 0, 0),
                                               PainterPathPoint(None, d['painter path'], 10, 10, 1),
                                               PainterPathPoint(None, d['painter path'], 20, 10, 2)]        
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
        d['colloid'] = GrainSize(d['Folk1964'], None, unicode('Colloid'), '', None, None, 1, d['um'], 6)
        d['clay'] = GrainSize(d['Folk1964'], None, unicode('Clay'), '', 1, d['um'], 4, d['um'], 12)
        d['silt'] = GrainSize(d['Folk1964'], None, unicode('Silt'), '', 4, d['um'], 62, d['um'], 18)
        d['vfs'] = GrainSize(d['Folk1964'], None, unicode('Very Fine Sand'), '', 62, d['um'], 125, d['um'], 24)
        d['fs'] = GrainSize(d['Folk1964'], None, unicode('Fine Sand'), '', 125, d['um'], 250, d['um'], 30)
        d['mfs'] = GrainSize(d['Folk1964'], None, unicode('Medium Sand'), '', 250, d['um'], 500, d['um'], 36)
        d['cs'] = GrainSize(d['Folk1964'], None, unicode('Coarse Sand'), '', 500, d['um'], 1, d['mm'], 42)
        d['vcs'] = GrainSize(d['Folk1964'], None, unicode('Very Coarse Sand'), '', 1, d['mm'], 2, d['mm'], 48)
        d['granule'] = GrainSize(d['Folk1964'], None, unicode('Granule'), '', 2, d['mm'], 4, d['mm'], 54)
        d['vfp'] = GrainSize(d['Folk1964'], None, unicode('Very Fine Pebble'), '', 4, d['mm'], 8, d['mm'], 60)
        d['fp'] = GrainSize(d['Folk1964'], None, unicode('Fine Pebble'), '', 8, d['mm'], 16, d['mm'], 66)
        d['p'] = GrainSize(d['Folk1964'], None, unicode('Pebble'), '', 16, d['mm'], 32, d['mm'], 72)
        d['cp'] = GrainSize(d['Folk1964'], None, unicode('Coarse Pebble'), '', 32, d['mm'], 64, d['mm'], 78)
        d['cobble'] = GrainSize(d['Folk1964'], None, unicode('Cobble'), '', 64, d['mm'], 256, d['mm'], 84)
        d['boulder'] = GrainSize(d['Folk1964'], None, unicode('Boulder'), '', 256, d['mm'], None, None, 100)
        d['mudstone'] = GrainSize(d['Dunham1962'], None, unicode('Mudstone'), '', None, None, None, None, 16)
        d['wackestone'] = GrainSize(d['Dunham1962'], None, unicode('Wackestone'), '', None, None, None, None, 32)
        d['packstone'] = GrainSize(d['Dunham1962'], None, unicode('Packstone'), '', None, None, None, None, 48)
        d['grainstone'] = GrainSize(d['Dunham1962'], None, unicode('Grainstone'), '', None, None, None, None, 64)
        d['boundstone'] = GrainSize(d['Dunham1962'], None, unicode('Boundstone'), '', None, None, None, None, 80)
        d['crystalline'] = GrainSize(d['Dunham1962'], None, unicode('Crystalline'), '', None, None, None, None, 100)

        d['Test project'] = Project(None, unicode('Test Project'))
        d['Limestone Mudstone'] = Lithology(d['Test project'], None, unicode('Limestone Mudstone'), None, unicode(''), d['mudstone'])
        d['red'] = Color(d['Test project'], None, unicode('Red'), None, unicode(''))
        d['massive'] = BeddingType(d['Test project'], None, unicode('Massive'), None, unicode(''))
        d['slump'] = SedimentStructure(d['Test project'], None, unicode('Slump'), None, unicode(''))
        d['snail'] = Fossil(d['Test project'], None, unicode('Snail'), None, unicode(''))
        d['sampling'] = CustomSymbol(d['Test project'], None, unicode('Sampling Point'), None, unicode(''))
        d['sharp planar'] = BoundaryType(d['Test project'], None, unicode('Sharp Planar'), None, unicode(''))
        d['oc1'] = PointOfInterest(d['Test project'], None, unicode('Outcrop 1'), None, unicode(''))
        d['Profile 1'] = Profile(d['Test project'], None, unicode('Profile 1'), unicode(''), 0, d['m'])
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
