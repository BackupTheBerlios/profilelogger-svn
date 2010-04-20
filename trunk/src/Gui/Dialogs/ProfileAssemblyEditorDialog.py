from Gui.Dialogs.DatasetInProjectEditorDialog import *

from PyQt4.QtCore import *

from Gui.ItemViews.GrainSizeItemView import GrainSizeItemView
from Gui.ItemViews.ProfileInProfileAssemblyItemView import ProfileInProfileAssemblyItemView

class ProfileAssemblyEditorDialog(DatasetInProjectEditorDialog):
    def __init__(self, parent, data):
        DatasetInProjectEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("Profile Assembly"))
        self.addIdDisplay()
        self.addProjectSelector()
        self.addNameEdit()
        self.addDescriptionEdit()
        self.addSaveProfileAssemblyButton()
        self.addDetailsWidget()
        self.addButtons()

        self.idW.setValue(self.data.id)
        self.projectW.reload()
        self.projectW.selectDataset(data.project)
        self.nameW.setValue(unicode(self.data.name))
        self.descriptionW.setValue(unicode(self.data.description))

        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
        self.setDetailsWidgetStatus(self.data.hasId())
    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt) 
    def onSaveRequest(self):
        if self.save():
            self.enableDetailsWidget()
        else:
            self.disableDetailsWidget()
    def addSaveProfileAssemblyButton(self):
        self.saveProfileAssemblyW = QPushButton(self.tr("&Save Profile Assembly"), self.contentW)
        self.contentW.layout().addWidget(self.saveProfileAssemblyW, self.currentContentRow, self.widgetCol)
        self.currentContentRow += 1
        self.saveProfileAssemblyW.clicked.connect(self.onSaveRequest)
    def addDetailsWidget(self):
        self.detailsW = QTabWidget(self.contentW)
        self.profileInProfileAssemblyW = ProfileInProfileAssemblyItemView(self.detailsW)
        self.detailsW.addTab(self.profileInProfileAssemblyW, self.tr("Profiles"))
        self.contentW.layout().addWidget(self.detailsW, self.currentContentRow, self.widgetCol)
        self.currentContentRow += 1
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
            self.profileInProfileAssemblyW.setProfileAssembly(self.data)
        else:
            self.profileInProfileAssemblyW.setProfileAssembly(None)
