from Gui.Dialogs.DatasetInProfileAssemblyEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.ProfileAssemblyItemView import ProfileAssemblyItemView
from Gui.ItemViews.ProfileItemView import ProfileItemView

class ProfileInProfileAssemblyEditorDialog(DatasetInProfileAssemblyEditorDialog):
    def __init__(self, parent, data):
        DatasetInProfileAssemblyEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Profile In Profile Assembly"))
        self.addIdDisplay()
        self.addNameEdit()
        self.addProfileAssemblySelector()
        self.addProfileSelector()
        self.addDescriptionEdit()
        self.addButtons()

        self.nameW.setEnabled(False)
        self.profileAssemblyW.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.idW.setValue(self.data.id)
        self.profileAssemblyW.selectDataset(data.profileAssembly)
        self.profileW.selectDataset(data.profile)
        self.nameW.setValue(unicode(self.data.name))
        self.descriptionW.setValue(unicode(self.data.description))

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
        self.profileW.currentDatasetChanged.connect(self.onProfileChange)
        QApplication.instance().profileModel.setProject(self.data.profileAssembly.project)
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
        if self.data.profileAssembly is not None:
            pa = self.data.profileAssembly.name
        if self.data.profile is not None:
            p = self.data.profile.name
        self.data.name = unicode(QString("%1 - %2").arg(pa).arg(p))
        self.nameW.setValue(self.data.name)
