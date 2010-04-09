from Gui.Dialogs.DatasetEditorDialog import *

from PyQt4.QtCore import *

class GeologicalMeasurementTypeEditorDialog(DatasetEditorDialog):
    def __init__(self, parent, data):
        DatasetEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Geological Measurement Type"))
        self.addIdDisplay()
        self.addNameEdit()
        self.addModeSelector()
        self.addDescriptionEdit()
        self.addButtons()

        self.idW.setValue(self.data.id)
        self.nameW.setValue(unicode(self.data.name))
        if data.isPlane:
            self.modePlaneW.setChecked(True)
        else:
            self.modeLinearW.setChecked(True)
        self.descriptionW.setValue(unicode(self.data.description))

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def addModeSelector(self):
        self.modesW = QGroupBox(self.tr("&Mode"), self.contentW)
        self.modePlaneW = QRadioButton(self.tr("Plane"), self.modesW)
        self.modeLinearW = QRadioButton(self.tr("Linear"), self.modesW)
        self.modesW.setLayout(QHBoxLayout(self.modesW))
        self.modesW.layout().addWidget(self.modePlaneW)
        self.modesW.layout().addWidget(self.modeLinearW)
        self.contentW.layout().addWidget(self.modesW, self.currentContentRow, self.widgetCol)
        self.currentContentRow += 1
        self.modePlaneW.toggled.connect(self.onModePlaneToggled)
        self.modeLinearW.toggled.connect(self.onModeLinearToggled)
    def onModePlaneToggled(self, b):
        self.data.isPlane = b
    def onModeLinearToggled(self, b):
        self.data.isPlane = (not b)
