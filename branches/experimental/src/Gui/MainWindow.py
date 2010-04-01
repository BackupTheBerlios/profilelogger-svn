from PyQt4.QtGui import *
from PyQt4.QtCore import *

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

from Gui.SimpleGraphicProfile.SimpleProfileView import SimpleProfileView

from Gui.ToolBars.GlobalToolsToolBar import *
from Gui.ToolBars.ProjectToolsToolBar import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupMenu()
        self.setupToolBar()
        self.setupStatusBar()
        self.setupCentralWidget()
        QApplication.instance().databaseConnected.connect(self.onDatabaseConnected)
    def setupCentralWidget(self):
        self.setCentralWidget(QTabWidget(self))
        self.centralWidget().setEnabled(False)    
    def setupMenu(self):
        self.fileM = QMenu(self.tr('&File'), self.menuBar())
        self.dbM = QMenu(self.tr('&Database'), self.menuBar())
        self.toolM = QMenu(self.tr("&Tools"), self.menuBar())
        self.globalM = QMenu(self.tr("&Global"), self.menuBar())

        for a in QApplication.instance().getFileActions():
            self.fileM.addAction(a)
        for a in QApplication.instance().getDatabaseActions():
            self.dbM.addAction(a)
        for a in QApplication.instance().getGlobalManagementActions():
            self.globalM.addAction(a)
        for a in QApplication.instance().getToolActions():
            self.toolM.addAction(a)

        self.menuBar().addMenu(self.fileM)
        self.menuBar().addMenu(self.dbM)
        self.menuBar().addMenu(self.toolM)
        self.menuBar().addMenu(self.globalM)

    def setupStatusBar(self):
        self.dbStatusW = QLabel(self.statusBar())
        self.statusBar().addPermanentWidget(self.dbStatusW)
        self.dbStatusW.setText(self.tr('Not Connected'))

    def onDatabaseConnected(self, msg):
        self.dbStatusW.setText(msg)
        self.centralWidget().setEnabled(True)
    def setupProfileViewer(self):
        self.profileViewW = SimpleProfileView(self.centralWidget())
        self.centralWidget().addTab(self.profileViewW, self.tr("View"))
    def setupToolBar(self):
        self.globalToolsTb = GlobalToolsToolBar(self.tr("Global Tools"), self)
        self.projectToolsTb = ProjectToolsToolBar(self.tr("Project Tools"), self)

        self.addToolBar(Qt.RightToolBarArea, self.globalToolsTb)
        self.addToolBar(Qt.LeftToolBarArea, self.projectToolsTb)
