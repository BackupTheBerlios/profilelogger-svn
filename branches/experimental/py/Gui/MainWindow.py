from PyQt4.QtGui import *
from PyQt4.QtCore import *

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
from Gui.ItemModels.BedItemModel import BedItemModel
from Gui.ItemModels.LithologicalUnitTypeItemModel import LithologicalUnitTypeItemModel
from Gui.ItemModels.LithologicalUnitItemModel import LithologicalUnitItemModel
from Gui.ItemModels.StratigraphicUnitTypeItemModel import StratigraphicUnitTypeItemModel
from Gui.ItemModels.StratigraphicUnitItemModel import StratigraphicUnitItemModel
from Gui.ItemModels.TectonicUnitTypeItemModel import TectonicUnitTypeItemModel
from Gui.ItemModels.TectonicUnitItemModel import TectonicUnitItemModel
from Gui.ItemModels.FaciesItemModel import FaciesItemModel
from Gui.ItemModels.OutcropTypeItemModel import OutcropTypeItemModel
from Gui.ItemModels.GeologicalMeasurementTypeItemModel import GeologicalMeasurementTypeItemModel
from Gui.ItemModels.ProfileAssemblyItemModel import ProfileAssemblyItemModel

from Gui.ItemViews.LengthUnitItemView import LengthUnitItemView
from Gui.ItemViews.ProjectItemView import ProjectItemView
from Gui.ItemViews.SVGItemView import SVGItemView
from Gui.ItemViews.GrainSizeTypeItemView import GrainSizeTypeItemView
from Gui.ItemViews.GrainSizeItemView import GrainSizeItemView
from Gui.ItemViews.LithologyItemView import LithologyItemView
from Gui.ItemViews.ColorItemView import ColorItemView
from Gui.ItemViews.BeddingTypeItemView import BeddingTypeItemView
from Gui.ItemViews.SedimentStructureItemView import SedimentStructureItemView
from Gui.ItemViews.FossilItemView import FossilItemView
from Gui.ItemViews.CustomSymbolItemView import CustomSymbolItemView
from Gui.ItemViews.BoundaryTypeItemView import BoundaryTypeItemView
from Gui.ItemViews.PointOfInterestItemView import PointOfInterestItemView
from Gui.ItemViews.ProfileItemView import ProfileItemView
from Gui.ItemViews.BedItemView import BedItemView
from Gui.ItemViews.LithologicalUnitTypeItemView import LithologicalUnitTypeItemView
from Gui.ItemViews.LithologicalUnitItemView import LithologicalUnitItemView
from Gui.ItemViews.StratigraphicUnitTypeItemView import StratigraphicUnitTypeItemView
from Gui.ItemViews.StratigraphicUnitItemView import StratigraphicUnitItemView
from Gui.ItemViews.TectonicUnitTypeItemView import TectonicUnitTypeItemView
from Gui.ItemViews.TectonicUnitItemView import TectonicUnitItemView
from Gui.ItemViews.FaciesItemView import FaciesItemView
from Gui.ItemViews.OutcropTypeItemView import OutcropTypeItemView
from Gui.ItemViews.GeologicalMeasurementTypeItemView import GeologicalMeasurementTypeItemView
from Gui.ItemViews.ProfileAssemblyItemView import ProfileAssemblyItemView
from Gui.Graphics.ProfileView import ProfileView
from Gui.ItemViews.PenStyleSelector import PenStyleSelector
from Gui.ItemViews.PenJoinStyleSelector import PenJoinStyleSelector
from Gui.ItemViews.PenCapStyleSelector import PenCapStyleSelector
from Gui.ItemViews.BrushStyleSelector import BrushStyleSelector
from Gui.ItemViews.DrawingItemView import DrawingItemView

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupMenu()
        self.setupStatusBar()
        self.setupCentralWidget()
        QApplication.instance().databaseConnected.connect(self.onDatabaseConnected)
    def setupCentralWidget(self):
        self.setCentralWidget(QSplitter(Qt.Horizontal, self))
        self.setupGlobalTools()
        self.setupProjectTools()
        self.setupBedTools()
        self.setupProfileViewer()
        self.centralWidget().setEnabled(False)    
    def setupGlobalTools(self):
        self.globalToolsW = QToolBox(self.centralWidget())
        self.setupProjectManagement()
        self.setupDrawingManagement()
        self.setupLengthUnitManagement()
        self.setupSVGItemManagement()
        self.setupLithologicalUnitTypeManagement()
        self.setupStratigraphicUnitTypeManagement()
        self.setupTectonicUnitTypeManagement()
        self.setupGeologicalMeasurementTypeManagement()
        self.setupGrainSizeTypeManagement()
        self.setupGrainSizeManagement()
        self.setupPenStyleSelector()
        self.setupPenJoinStyleSelector()
        self.setupPenCapStyleSelector()
        self.setupBrushStyleSelector()
        self.centralWidget().addWidget(self.globalToolsW)
    def setupBedTools(self):
        self.bedToolsW = QToolBox(self.centralWidget())
        self.setupBedManagement()
        self.centralWidget().addWidget(self.bedToolsW)
    def setupProjectTools(self):
        self.projectToolsW = QToolBox(self.centralWidget())
        self.setupProfileManagement()
        self.setupProfileAssemblyManagement()
        self.setupLithologyManagement()
        self.setupColorManagement()
        self.setupOutcropTypeManagement()
        self.setupFaciesManagement()
        self.setupLithologicalUnitManagement()
        self.setupStratigraphicUnitManagement()
        self.setupTectonicUnitManagement()
        self.setupBeddingTypeManagement()
        self.setupSedimentStructureManagement()
        self.setupFossilManagement()
        self.setupCustomSymbolManagement()
        self.setupBoundaryTypeManagement()
        self.setupPointOfInterestManagement()
        self.centralWidget().addWidget(self.projectToolsW)
    def setupBedManagement(self):
        self.bedsW = ColorItemView(self.bedToolsW,
                                   QApplication.instance().bedModel)
        self.bedToolsW.addItem(self.bedsW, self.tr("Beds"))
        self.profilesW.currentDatasetChanged.connect(QApplication.instance().bedModel.onProfileChange)
    def setupLithologyManagement(self):
        self.lithologiesW = LithologyItemView(self.globalToolsW,
                                              QApplication.instance().lithologyModel)
        self.projectToolsW.addItem(self.lithologiesW, self.tr("Lithologies"))
        self.projectsW.currentDatasetChanged.connect(QApplication.instance().lithologyModel.onProjectChange)
    def setupColorManagement(self):
        self.colorsW = ColorItemView(self.globalToolsW,
                                          QApplication.instance().colorModel)
        self.projectToolsW.addItem(self.colorsW, self.tr("Colors"))
        self.projectsW.currentDatasetChanged.connect(QApplication.instance().colorModel.onProjectChange)
    def setupFaciesManagement(self):
        self.faciessW = FaciesItemView(self.globalToolsW,
                                       QApplication.instance().faciesModel)
        self.projectToolsW.addItem(self.faciessW, self.tr("Facies"))
        self.projectsW.currentDatasetChanged.connect(QApplication.instance().faciesModel.onProjectChange)
    def setupProfileManagement(self):
        self.profilesW = ProfileItemView(self.globalToolsW,
                                         QApplication.instance().profileModel)
        self.projectToolsW.addItem(self.profilesW, self.tr("Profiles"))
        self.projectsW.currentDatasetChanged.connect(QApplication.instance().profileModel.onProjectChange)
    def setupProfileAssemblyManagement(self):
        self.profileAssemblysW = ProfileAssemblyItemView(self.globalToolsW,
                                                         QApplication.instance().profileAssemblyModel)
        self.projectToolsW.addItem(self.profileAssemblysW, self.tr("Profile Assemblies"))
        self.projectsW.currentDatasetChanged.connect(QApplication.instance().profileAssemblyModel.onProjectChange)
    def setupPointOfInterestManagement(self):
        self.pointsOfInterestW = PointOfInterestItemView(self.globalToolsW,
                                                         QApplication.instance().pointOfInterestModel)
        self.projectToolsW.addItem(self.pointsOfInterestW, self.tr("Points Of Interest"))
        self.projectsW.currentDatasetChanged.connect(QApplication.instance().pointOfInterestModel.onProjectChange)
    def setupBoundaryTypeManagement(self):
        self.boundaryTypeView = BoundaryTypeItemView(self.globalToolsW,
                                                     QApplication.instance().boundaryTypeModel)
        self.projectToolsW.addItem(self.boundaryTypeView, self.tr("BoundaryTypes"))
        self.projectsW.currentDatasetChanged.connect(QApplication.instance().boundaryTypeModel.onProjectChange)
    def setupCustomSymbolManagement(self):
        self.customSymbolView = CustomSymbolItemView(self.globalToolsW,
                                                     QApplication.instance().customSymbolModel)
        self.projectToolsW.addItem(self.customSymbolView, self.tr("Custom Symbols"))
        self.projectsW.currentDatasetChanged.connect(QApplication.instance().customSymbolModel.onProjectChange)
    def setupFossilManagement(self):
        self.fossilsW = FossilItemView(self.globalToolsW,
                                       QApplication.instance().fossilModel)
        self.projectToolsW.addItem(self.fossilsW, self.tr("Fossils"))
        self.projectsW.currentDatasetChanged.connect(QApplication.instance().fossilModel.onProjectChange)
    def setupSedimentStructureManagement(self):
        self.sedimentStructuresW = SedimentStructureItemView(self.globalToolsW,
                                                             QApplication.instance().sedimentStructureModel)
        self.projectToolsW.addItem(self.sedimentStructuresW, self.tr("Sediment Structures"))
        self.projectsW.currentDatasetChanged.connect(QApplication.instance().sedimentStructureModel.onProjectChange)
    def setupBeddingTypeManagement(self):
        self.lithologiesW = BeddingTypeItemView(self.globalToolsW,
                                                QApplication.instance().beddingTypeModel)
        self.projectToolsW.addItem(self.lithologiesW, self.tr("Bedding Types"))
        self.projectsW.currentDatasetChanged.connect(QApplication.instance().beddingTypeModel.onProjectChange)
    def setupLengthUnitManagement(self):
        self.lengthUnitsW = LengthUnitItemView(self.globalToolsW,
                                               QApplication.instance().lengthUnitModel)
        self.globalToolsW.addItem(self.lengthUnitsW, self.tr("Length Units"))
    def setupProjectManagement(self):
        self.projectsW = ProjectItemView(self.globalToolsW,
                                         QApplication.instance().projectModel)
        self.globalToolsW.addItem(self.projectsW, self.tr("Projects"))
    def setupDrawingManagement(self):
        self.drawingsW = DrawingItemView(self.globalToolsW,
                                         QApplication.instance().drawingModel)
        self.globalToolsW.addItem(self.drawingsW, self.tr("Drawings"))
    def setupGrainSizeManagement(self):
        self.grainSizesW = GrainSizeItemView(self.globalToolsW,
                                             QApplication.instance().grainSizeModel)
        self.globalToolsW.addItem(self.grainSizesW, self.tr("Grain Sizes"))
    def setupSVGItemManagement(self):
        self.SVGItemsW = SVGItemView(self.globalToolsW,
                                     QApplication.instance().svgItemModel)
        self.globalToolsW.addItem(self.SVGItemsW, self.tr("SVG Items"))
    def setupGrainSizeTypeManagement(self):
        self.grainSizeTypesW = GrainSizeTypeItemView(self.globalToolsW,
                                                     QApplication.instance().grainSizeTypeModel)
        self.globalToolsW.addItem(self.grainSizeTypesW, self.tr("Grain Size Types"))
    def setupLithologicalUnitTypeManagement(self):
        self.lithologicalUnitTypesW = LithologicalUnitTypeItemView(self.globalToolsW,
                                                                   QApplication.instance().lithologicalUnitTypeModel)
        self.globalToolsW.addItem(self.lithologicalUnitTypesW, self.tr("Lithological Unit Types"))
    def setupGeologicalMeasurementTypeManagement(self):
        self.geologicalMeasurementTypesW = GeologicalMeasurementTypeItemView(self.globalToolsW,
                                                                   QApplication.instance().geologicalMeasurementTypeModel)
        self.globalToolsW.addItem(self.geologicalMeasurementTypesW, self.tr("Geological Measurement Types"))
    def setupOutcropTypeManagement(self):
        self.outcropTypesW = OutcropTypeItemView(self.globalToolsW,
                                                 QApplication.instance().outcropTypeModel)
        self.projectToolsW.addItem(self.outcropTypesW, self.tr("Outcrop Types"))
        self.projectsW.currentDatasetChanged.connect(QApplication.instance().outcropTypeModel.onProjectChange)
    def setupLithologicalUnitManagement(self):
        self.lithologicalUnitsW = LithologicalUnitItemView(self.globalToolsW,
                                                           QApplication.instance().lithologicalUnitModel)
        self.projectToolsW.addItem(self.lithologicalUnitsW, self.tr("Lithological Units"))
        self.projectsW.currentDatasetChanged.connect(QApplication.instance().lithologicalUnitModel.onProjectChange)
    def setupStratigraphicUnitTypeManagement(self):
        self.stratigraphicUnitTypesW = StratigraphicUnitTypeItemView(self.globalToolsW,
                                                                     QApplication.instance().stratigraphicUnitTypeModel)
        self.globalToolsW.addItem(self.stratigraphicUnitTypesW, self.tr("Stratigraphic Unit Types"))
    def setupStratigraphicUnitManagement(self):
        self.stratigraphicUnitsW = StratigraphicUnitItemView(self.projectToolsW,
                                                             QApplication.instance().stratigraphicUnitModel)
        self.projectToolsW.addItem(self.stratigraphicUnitsW, self.tr("Stratigraphic Units"))
        self.projectsW.currentDatasetChanged.connect(QApplication.instance().stratigraphicUnitModel.onProjectChange)
    def setupTectonicUnitTypeManagement(self):
        self.tectonicUnitTypesW = TectonicUnitTypeItemView(self.globalToolsW,
                                                           QApplication.instance().tectonicUnitTypeModel)
        self.globalToolsW.addItem(self.tectonicUnitTypesW, self.tr("Tectonic Unit Types"))
    def setupStratigraphicUnitManagement(self):
        self.stratigraphicUnitsW = StratigraphicUnitItemView(self.projectToolsW,
                                                             QApplication.instance().stratigraphicUnitModel)
        self.projectToolsW.addItem(self.stratigraphicUnitsW, self.tr("Stratigraphic Units"))
        self.projectsW.currentDatasetChanged.connect(QApplication.instance().stratigraphicUnitModel.onProjectChange)
    def setupTectonicUnitManagement(self):
        self.tectonicUnitsW = TectonicUnitItemView(self.projectToolsW,
                                                   QApplication.instance().tectonicUnitModel)
        self.projectToolsW.addItem(self.tectonicUnitsW, self.tr("Tectonic Units"))
        self.projectsW.currentDatasetChanged.connect(QApplication.instance().tectonicUnitModel.onProjectChange)
    def setupPenStyleSelector(self):
        self.penStylesW = PenStyleSelector(self.globalToolsW,
                                           QApplication.instance().penStyleModel)
        self.globalToolsW.addItem(self.penStylesW, self.tr("Pen Styles"))
        self.penStylesW.currentDatasetChanged.connect(self.onPenStyleChange)
    def onPenStyleChange(self, s):
        print "style: ", s
    def setupBrushStyleSelector(self):
        self.brushStylesW = BrushStyleSelector(self.globalToolsW,
                                           QApplication.instance().brushStyleModel)
        self.globalToolsW.addItem(self.brushStylesW, self.tr("Brush Styles"))
        self.brushStylesW.currentDatasetChanged.connect(self.onBrushStyleChange)
    def onBrushStyleChange(self, s):
        print "style: ", s
    def setupPenJoinStyleSelector(self):
        self.penJoinStylesW = PenJoinStyleSelector(self.globalToolsW,
                                                   QApplication.instance().penJoinStyleModel)
        self.globalToolsW.addItem(self.penJoinStylesW, self.tr("Pen Join Styles"))
        self.penJoinStylesW.currentDatasetChanged.connect(self.onPenJoinStyleChange)
    def onPenJoinStyleChange(self, s):
        print "joinStyle: ", s
    def setupPenCapStyleSelector(self):
        self.penCapStylesW = PenCapStyleSelector(self.globalToolsW,
                                                   QApplication.instance().penCapStyleModel)
        self.globalToolsW.addItem(self.penCapStylesW, self.tr("Pen Cap Styles"))
        self.penCapStylesW.currentDatasetChanged.connect(self.onPenCapStyleChange)
    def onPenCapStyleChange(self, s):
        print "capStyle: ", s

    def setupMenu(self):
        self.fileM = QMenu(self.tr('&File'), self.menuBar())
        self.dbM = QMenu(self.tr('&Database'), self.menuBar())
        self.toolM = QMenu(self.tr("&Tools"), self.menuBar())

        for a in QApplication.instance().getFileActions():
            self.fileM.addAction(a)
        for a in QApplication.instance().getDatabaseActions():
            self.dbM.addAction(a)
        for a in QApplication.instance().getToolActions():
            self.toolM.addAction(a)

        self.menuBar().addMenu(self.fileM)
        self.menuBar().addMenu(self.dbM)
        self.menuBar().addMenu(self.toolM)

    def setupStatusBar(self):
        self.dbStatusW = QLabel(self.statusBar())
        self.statusBar().addPermanentWidget(self.dbStatusW)
        self.dbStatusW.setText(self.tr('Not Connected'))

    def onDatabaseConnected(self, msg):
        self.dbStatusW.setText(msg)
        self.centralWidget().setEnabled(True)
    def setupProfileViewer(self):
        self.profileViewW = ProfileView(self.centralWidget())
        self.centralWidget().addWidget(self.profileViewW)
        self.profilesW.currentDatasetChanged.connect(QApplication.instance().profileScene.onProfileChange)
