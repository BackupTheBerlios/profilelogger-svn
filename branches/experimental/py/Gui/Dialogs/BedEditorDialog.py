from Gui.Dialogs.DatasetInProfileEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.GrainSizeItemView import GrainSizeItemView
from Gui.Widgets.LengthInputWidget import LengthInputWidget
from Gui.Widgets.IntLineEdit import IntLineEdit

class BedEditorDialog(DatasetInProfileEditorDialog):
    def __init__(self, parent, data):
        DatasetInProfileEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Bed"))
        self.addIdDisplay()
        self.addProfileSelector()
        self.addHeightEdit()
        self.addBedNumberEdit()
        self.addNameEdit()
        self.addDescriptionEdit()
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
        self.data.name = unicode(self.tr("%1/%2/Bed #%3").arg(self.data.profile.project.name).arg(self.data.profile.name).arg(v))
        self.data.number = v
        self.nameW.setText(self.data.name)
    def onHeightValueChange(self, v):
        self.data.height = v
    def onHeightUnitChange(self, u):
        self.data.lengthUnit = u
    def addDetailsWidget(self):
        self.detailsW = QTabWidget(self.contentW)
        self.contentW.layout().addWidget(self.detailsW, self.currentContentRow, self.widgetCol)
        self.currentContentRow += 1
        self.detailsW.addTab(QLabel('test', self.detailsW), 'test')
