from ToolBar import *

from Gui.Widgets.PointOfInterestSelectionComboBox import *

from Model.PointOfInterest import *

class PointOfInterestToolBar(ToolBar):
    currentPointOfInterestChanged = pyqtSignal(PointOfInterest)
    def __init__(self, title, parent):
        ToolBar.__init__(self, title, parent)
        self.project=None
        self.pointOfInterestsW = PointOfInterestSelectionComboBox(self)
        self.pointOfInterestsW.currentDatasetChanged.connect(self.onPointOfInterestChange)
        self.addWidget(QLabel(self.tr("Points Of Interest:"), self))
        self.addWidget(self.pointOfInterestsW)
        self.setEnabled(False)
    def onPointOfInterestChange(self, p):
        self.currentPointOfInterestChanged.emit(p)
    def onProjectChange(self, p):
        self.project = p
        self.pointOfInterestsW.setProject(p)
        self.setEnabled(self.hasProject())
    def hasProject(self):
        return self.project is not None
    
