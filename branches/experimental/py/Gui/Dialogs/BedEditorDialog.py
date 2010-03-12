from Gui.Dialogs.DatasetInProfileEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.GrainSizeItemView import GrainSizeItemView
from Gui.ItemViews.LithologyInBedItemView import LithologyInBedItemView
from Gui.ItemViews.ColorInBedItemView import ColorInBedItemView

from Gui.Widgets.LengthInputWidget import LengthInputWidget
from Gui.Widgets.IntLineEdit import IntLineEdit

class BedEditorDialog(DatasetInProfileEditorDialog):
    def __init__(self, parent, data):
        DatasetInProfileEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Bed"))
        self.addIdDisplay()
        self.addNameEdit()
        self.addProfileSelector()
        self.addHeightEdit()
        self.addBedNumberEdit()
        self.addDescriptionEdit()
        self.addSaveBedButton()
        self.addDetailsWidget()
        self.addButtons()

        self.nameW.setEnabled(False)

        self.idW.setValue(self.data.id)
        self.profileW.selectDataset(data.profile)
        self.nameW.setValue(unicode(self.data.name))
        self.heightW.setValue(self.data.height, self.data.lengthUnit)
        self.bedNumberW.setValue(self.data.number)
        self.descriptionW.setValue(unicode(self.data.description))
        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
        self.setDetailsWidgetStatus(self.data.hasId())
    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def addHeightEdit(self):
        self.heightL = self.createOneLineLabel(self.tr("&Height"))
        self.heightW = LengthInputWidget(self.contentW)
        self.heightL.setBuddy(self.heightW)
        self.addLabelWidgetPair(self.heightL, self.heightW)
        self.heightW.valueChanged.connect(self.onHeightValueChange)
        self.heightW.lengthUnitChanged.connect(self.onHeightUnitChange)
    def addBedNumberEdit(self):
        self.bedNumberL = self.createOneLineLabel(self.tr("Bed &Number"))
        self.bedNumberW = IntLineEdit(self.contentW)
        self.bedNumberL.setBuddy(self.bedNumberW)
        self.addLabelWidgetPair(self.bedNumberL, self.bedNumberW)
        self.bedNumberW.valueChanged.connect(self.onBedNumberChange)
    def onBedNumberChange(self, v):
        self.data.name = unicode(self.tr("%1/%2/Bed #%3").arg(self.data.profile.project.name).arg(self.data.profile.name).arg(v, 5, 10, QChar('0')))
        self.data.number = v
        self.nameW.setText(self.data.name)
    def onHeightValueChange(self, v):
        self.data.height = v
    def onHeightUnitChange(self, u):
        self.data.lengthUnit = u
    def addSaveBedButton(self):
        self.saveBedW = QPushButton(self.tr("&Save Bed"), self.contentW)
        self.contentW.layout().addWidget(self.saveBedW, self.currentContentRow, self.widgetCol)
        self.currentContentRow += 1
        self.saveBedW.clicked.connect(self.onSaveRequest)
    def addDetailsWidget(self):
        self.detailsW = QTabWidget(self.contentW)
        self.contentW.layout().addWidget(self.detailsW, self.currentContentRow, self.widgetCol)
        self.currentContentRow += 1

        self.lithologyInBedW = LithologyInBedItemView(self.detailsW, QApplication.instance().lithologyInBedModel)
        self.colorInBedW = ColorInBedItemView(self.detailsW, QApplication.instance().colorInBedModel)
        self.detailsW.addTab(self.lithologyInBedW, self.tr("Lithology"))
        self.detailsW.addTab(self.colorInBedW, self.tr("Color"))

        self.detailsW.setEnabled(False)
    def onSaveRequest(self):
        if self.save():
            self.enableDetailsWidget()
        else:
            self.disableDetailsWidget()
    def enableDetailsWidget(self):
        self.setDetailsWidgetStatus(True)
    def disableDetailsWidget(self):
        self.setDetailsWidgetStatus(False)
    def setDetailsWidgetStatus(self, isEnabled):
        self.detailsW.setEnabled(isEnabled)
        if isEnabled:
            QApplication.instance().lithologyInBedModel.setBed(self.data)
            QApplication.instance().colorInBedModel.setBed(self.data)
        else:
            QApplication.instance().lithologyInBedModel.setBed(None)
            QApplication.instance().colorInBedModel.setBed(None)
