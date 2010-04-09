from Gui.Dialogs.DatasetInProfileAssemblyEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.ProfileAssemblyItemView import ProfileAssemblyItemView
from Gui.ItemViews.ProfileItemView import ProfileItemView
from Gui.ItemViews.BedItemView import BedItemView
from Gui.ItemModels.BedItemModel import BedItemModel

from ProfileInProfileAssemblyConfigurationDialog import *

class ProfileInProfileAssemblyEditorDialog(DatasetInProfileAssemblyEditorDialog):
    def __init__(self, parent, data):
        DatasetInProfileAssemblyEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Profile In Profile Assembly"))
        self.addIdDisplay()
        self.addNameEdit()
        self.addProfileAssemblySelector()
        self.addProfileSelector()
        self.addCustomBedsSelector()
        self.addDescriptionEdit()
        self.addConfigurationButton()
        self.addButtons()

        self.nameW.setEnabled(False)
        self.profileAssemblyW.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
        self.profileW.currentDatasetChanged.connect(self.onProfileChange)
        self.baseBedW.currentDatasetChanged.connect(self.onBaseBedChange)
        self.topBedW.currentDatasetChanged.connect(self.onTopBedChange)
        self.profileW.currentDatasetChanged.connect(self.baseBedM.onProfileChange)
        self.profileW.currentDatasetChanged.connect(self.topBedM.onProfileChange)
        QApplication.instance().profileModel.setProject(self.data.profileAssembly.project)
        QApplication.instance().profileModel.reload()

        self.profileW.selectDataset(self.data.profile)
        self.baseBedM.setProfile(self.data.profile)
        self.topBedM.setProfile(self.data.profile)
        self.baseBedM.reload()
        self.topBedM.reload()

        self.baseBedW.selectDataset(self.data.firstBedInView)
        self.topBedW.selectDataset(self.data.lastBedInView)
        self.idW.setValue(self.data.id)
        self.profileAssemblyW.selectDataset(data.profileAssembly)
        self.nameW.setValue(unicode(self.data.name))
        self.descriptionW.setValue(unicode(self.data.description))
    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def onProfileChange(self, p):
        self.data.profile = p
        self.updateName()
    def addProfileSelector(self):
        self.profileL = self.createMultiLineLabel(self.tr("&Profile"))
        self.profileW = ProfileItemView(self.contentW, QApplication.instance().profileModel)
        self.profileL.setBuddy(self.profileW)
        self.addLabelWidgetPair(self.profileL, self.profileW)
    def updateName(self):
        pa = self.tr("<Profile Assembly Missing>")
        p = self.tr("<Profile Missing>")
        bb = self.tr("<Base Bed Missing>")
        tb = self.tr("<Top Bed Missing>")
        if self.data.profileAssembly is not None:
            pa = self.data.profileAssembly.name
        if self.data.profile is not None:
            p = self.data.profile.name
        if self.data.firstBedInView is not None:
            bb = self.data.firstBedInView.name
        if self.data.lastBedInView is not None:
            tb = self.data.lastBedInView.name
        self.data.name = unicode(QString("%1 - %2: %3 - %4").arg(pa).arg(p).arg(bb).arg(tb))
        self.nameW.setValue(self.data.name)
    def addConfigurationButton(self):
        self.configW = QPushButton(self.tr("Configure Features..."), self.contentW)
        self.contentW.layout().addWidget(self.configW, self.currentContentRow, self.widgetCol)
        self.currentContentRow += 1
        self.configW.clicked.connect(self.onConfigureFeatures)
    def onConfigureFeatures(self):
        dlg = ProfileInProfileAssemblyConfigurationDialog(self, self.data)
        dlg.exec_()
    def onBaseBedChange(self, b):
        self.data.firstBedInView = b
        self.updateName()
    def onTopBedChange(self, b):
        self.data.lastBedInView = b
        self.updateName()
    def addCustomBedsSelector(self):
        w = QWidget(self.contentW)
        w.setLayout(QGridLayout(w))
        
        self.baseBedM = BedItemModel(self)
        self.topBedM = BedItemModel(self)
        self.baseBedW = BedItemView(self, self.baseBedM)
        self.topBedW = BedItemView(self, self.topBedM)

        w.layout().addWidget(QLabel(self.tr("Base Bed"), w), 0, 0)
        w.layout().addWidget(QLabel(self.tr("Top Bed"), w), 0, 1)
        w.layout().addWidget(self.baseBedW, 1, 0)
        w.layout().addWidget(self.topBedW, 1, 1)

        self.contentW.layout().addWidget(w, self.currentContentRow, self.widgetCol)
        self.currentContentRow += 1
