from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Gui.Widgets.IdLabel import IdLabel
from Gui.Widgets.NameEdit import NameEdit
from Gui.Widgets.DescriptionEdit import DescriptionEdit
from Gui.Widgets.IntLineEdit import IntLineEdit

class DatasetEditorDialog(QDialog):
    def __init__(self, parent, data):
        QDialog.__init__(self, parent)
        self.data = data
        self.setLayout(QVBoxLayout(self))
    def addContentPanel(self, title):
        self.contentW = QGroupBox(title, self)
        self.contentW.setLayout(QGridLayout(self.contentW))
        self.layout().addWidget(self.contentW)
        self.currentContentRow = 0
        self.labelCol = 0
        self.widgetCol = 1
    def addButtons(self):
        self.bbW = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel,
                                    Qt.Horizontal,
                                    self)
        self.bbW.accepted.connect(self.accept)
        self.bbW.rejected.connect(self.reject)
        self.layout().addWidget(self.bbW)
    def addIdDisplay(self):
        self.idL = self.createOneLineLabel(self.tr("ID"))
        self.idW = IdLabel(self.contentW)
        self.contentW.layout().addWidget(self.idL, self.currentContentRow, self.labelCol)
        self.contentW.layout().addWidget(self.idW, self.currentContentRow, self.widgetCol)
        self.currentContentRow += 1
    def addIntEdit(self, label):
        self.intL = self.createOneLineLabel(label)
        self.intW = IntLineEdit(self)
        self.intL.setBuddy(self.intW)
        self.contentW.layout().addWidget(self.intL, self.currentContentRow, self.labelCol)
        self.contentW.layout().addWidget(self.intW, self.currentContentRow, self.widgetCol)
        self.currentContentRow += 1

    def addNameEdit(self, label=None):
        lbl = label
        if lbl is None:
            lbl = self.tr("&Name")
        self.nameL = self.createOneLineLabel(lbl)
        self.nameW = NameEdit(self.contentW)
        self.nameL.setBuddy(self.nameW)
        self.contentW.layout().addWidget(self.nameL, self.currentContentRow, self.labelCol)
        self.contentW.layout().addWidget(self.nameW, self.currentContentRow, self.widgetCol)
        self.currentContentRow += 1
    def addDescriptionEdit(self, label=None):
        lbl = label
        if lbl is None:
            lbl = self.tr("&Description")
        self.descriptionL = self.createMultiLineLabel(lbl)
        self.descriptionW = DescriptionEdit(self.contentW)
        self.descriptionL.setBuddy(self.descriptionW)
        self.contentW.layout().addWidget(self.descriptionL, self.currentContentRow, self.labelCol)
        self.contentW.layout().addWidget(self.descriptionW, self.currentContentRow, self.widgetCol)
        self.currentContentRow += 1

    def createOneLineLabel(self, lbl):
        lbl = QLabel(lbl, self.contentW)
        lbl.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        return lbl
    def createMultiLineLabel(self, lbl):
        lbl = QLabel(lbl, self.contentW)
        lbl.setAlignment(Qt.AlignTop | Qt.AlignRight)
        return lbl
