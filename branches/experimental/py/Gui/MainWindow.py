from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Gui.ItemModels.LengthUnitItemModel import LengthUnitItemModel
from Gui.ItemModels.ProjectItemModel import ProjectItemModel
from Gui.ItemModels.SVGItemModel import SVGItemModel
from Gui.ItemModels.GrainSizeTypeItemModel import GrainSizeTypeItemModel
from Gui.ItemModels.GrainSizeItemModel import GrainSizeItemModel
from Gui.ItemModels.LithologyItemModel import LithologyItemModel

from Gui.ItemViews.LengthUnitItemView import LengthUnitItemView
from Gui.ItemViews.ProjectItemView import ProjectItemView
from Gui.ItemViews.SVGItemView import SVGItemView
from Gui.ItemViews.GrainSizeTypeItemView import GrainSizeTypeItemView
from Gui.ItemViews.GrainSizeItemView import GrainSizeItemView
from Gui.ItemViews.LithologyItemView import LithologyItemView

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
        self.centralWidget().setEnabled(False)
    def setupProjectTools(self):
        self.projectToolsW = QToolBox(self.centralWidget())
        self.setupLithologyManagement()
        self.centralWidget().addWidget(self.projectToolsW)
    def setupLithologyManagement(self):
        self.lithologiesW = LithologyItemView(self.globalToolsW,
                                              QApplication.instance().lithologyModel)
        self.projectToolsW.addItem(self.lithologiesW, self.tr("Lithologies"))
        self.projectsW.currentDatasetChanged.connect(QApplication.instance().lithologyModel.onProjectChange)

    def setupGlobalTools(self):
        self.globalToolsW = QToolBox(self.centralWidget())
        self.setupLengthUnitManagement()
        self.setupProjectManagement()
        self.setupSVGItemManagement()
        self.setupGrainSizeTypeManagement()
        self.setupGrainSizeManagement()
        self.centralWidget().addWidget(self.globalToolsW)
    def setupLengthUnitManagement(self):
        self.lengthUnitsW = LengthUnitItemView(self.globalToolsW,
                                               QApplication.instance().lengthUnitModel)
        self.globalToolsW.addItem(self.lengthUnitsW, self.tr("Length Units"))
    def setupProjectManagement(self):
        self.projectsW = ProjectItemView(self.globalToolsW,
                                         QApplication.instance().projectModel)
        self.globalToolsW.addItem(self.projectsW, self.tr("Projects"))
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

    def setupMenu(self):
        self.fileM = QMenu(self.tr('&File'), self.menuBar())
        self.dbM = QMenu(self.tr('&Database'), self.menuBar())

        for a in QApplication.instance().getFileActions():
            self.fileM.addAction(a)
        for a in QApplication.instance().getDatabaseActions():
            self.dbM.addAction(a)

        self.menuBar().addMenu(self.fileM)
        self.menuBar().addMenu(self.dbM)

    def setupStatusBar(self):
        self.dbStatusW = QLabel(self.statusBar())
        self.statusBar().addPermanentWidget(self.dbStatusW)
        self.dbStatusW.setText(self.tr('Not Connected'))

    def onDatabaseConnected(self, msg):
        self.dbStatusW.setText(msg)
        self.centralWidget().setEnabled(True)
