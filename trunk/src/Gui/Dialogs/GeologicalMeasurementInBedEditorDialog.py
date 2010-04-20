from Gui.Dialogs.DatasetInBedEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.GeologicalMeasurementTypeItemView import GeologicalMeasurementTypeItemView
from Gui.Widgets.StrikeDipEditorWidget import StrikeDipEditorWidget

class GeologicalMeasurementInBedEditorDialog(DatasetInBedEditorDialog):
    def __init__(self, parent, data):
        DatasetInBedEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Geological Measurement"))
        self.addIdDisplay()
        self.addNameEdit()
        self.addBedSelector()
        self.addGeologicalMeasurementTypeEditor()
        self.addGeologicalMeasurementEditor()
        self.addPercentEditor()
        self.addDescriptionEdit()
        self.addButtons()
        self.nameW.setEnabled(False)

        self.idW.setValue(self.data.id)
        self.nameW.setValue(self.data.name)
        self.geologicalMeasurementTypeW.selectDataset(data.geologicalMeasurementType)
        self.geologicalMeasurementEditorW.setValues(self.data.strike, self.data.dip)
        self.bedW.selectDataset(data.bed)
        self.percentW.setValues(data.begin, data.end)
        self.descriptionW.setValue(unicode(self.data.description))

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
        self.percentW.beginValueChanged.connect(self.onBeginValueChange)
        self.percentW.endValueChanged.connect(self.onEndValueChange)
        
    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def addGeologicalMeasurementTypeEditor(self):
        self.geologicalMeasurementTypeL = self.createMultiLineLabel(self.tr("Measurement &Type"))
        self.geologicalMeasurementTypeW = GeologicalMeasurementTypeItemView(self.contentW)
        self.geologicalMeasurementTypeL.setBuddy(self.geologicalMeasurementTypeW)
        self.addLabelWidgetPair(self.geologicalMeasurementTypeL, self.geologicalMeasurementTypeW)
        self.geologicalMeasurementTypeW.currentDatasetChanged.connect(self.onGeologicalMeasurementTypeChange)
        self.geologicalMeasurementTypeW.reload()
    def onGeologicalMeasurementTypeChange(self, t):
        self.data.geologicalMeasurementType = t
        self.updateName()
    def addGeologicalMeasurementEditor(self):
        self.geologicalMeasurementEditorL = self.createOneLineLabel(self.tr("&Measurement"))
        self.geologicalMeasurementEditorW = StrikeDipEditorWidget(self.contentW)
        self.geologicalMeasurementEditorL.setBuddy(self.geologicalMeasurementEditorW)
        self.addLabelWidgetPair(self.geologicalMeasurementEditorL, self.geologicalMeasurementEditorW)
        self.geologicalMeasurementEditorW.strikeChanged.connect(self.onStrikeChange)
        self.geologicalMeasurementEditorW.dipChanged.connect(self.onDipChange)
    def updateName(self):
        if self.data.geologicalMeasurementType is None:
            self.nameW.setText(self.tr("<Geological Measurement Type not Set>"))
        else:
            strike = self.tr("Strike Missing")
            dip = self.tr("Dip Missing")
            if self.data.strike is not None:
                strike = QString("%1").arg(self.data.strike)
            if self.data.dip is not None:
                dip = QString("%1").arg(self.data.dip)
            self.data.name = unicode(self.tr("%1 - %2: %3: %4/%5").arg(self.data.begin).arg(self.data.end).arg(self.data.geologicalMeasurementType.name).arg(strike).arg(dip))
            self.nameW.setText(self.data.name)
    def onBeginValueChange(self, v):
        self.data.begin = v
        self.updateName()
    def onEndValueChange(self, v):
        self.data.end = v
        self.updateName()
    def onStrikeChange(self, s):
        self.data.strike = s
        self.updateName()
    def onDipChange(self, d):
        self.data.dip = d
        self.updateName()
