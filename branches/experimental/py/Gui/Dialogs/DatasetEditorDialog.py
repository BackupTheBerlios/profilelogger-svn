from Dialog import Dialog

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Gui.Widgets.IdLabel import IdLabel
from Gui.Widgets.NameEdit import NameEdit
from Gui.Widgets.DescriptionEdit import DescriptionEdit
from Gui.Widgets.IntLineEdit import IntLineEdit
from Gui.Widgets.SVGLoaderWidget import SVGLoaderWidget

from Gui.Dialogs.DatabaseExceptionDialog import DatabaseExceptionDialog

from sqlalchemy.exc import *
from sqlalchemy.orm.exc import *

class DatasetEditorDialog(Dialog):
    def __init__(self, parent, data):
        Dialog.__init__(self, parent)
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
    def addLabelWidgetPair(self, labelW, widget):
        self.contentW.layout().addWidget(labelW, self.currentContentRow, self.labelCol)
        self.contentW.layout().addWidget(widget, self.currentContentRow, self.widgetCol)
        self.currentContentRow += 1
    def addIdDisplay(self):
        self.idL = self.createOneLineLabel(self.tr("ID"))
        self.idW = IdLabel(self.contentW)
        self.addLabelWidgetPair(self.idL, self.idW)
    def addIntEdit(self, label, min=1, max=999999):
        self.intL = self.createOneLineLabel(label)
        self.intW = IntLineEdit(self)
        self.intL.setBuddy(self.intW)
        self.intW.validator().setRange(min, max)
        self.addLabelWidgetPair(self.intL, self.intW)
    def addNameEdit(self, label=None):
        lbl = label
        if lbl is None:
            lbl = self.tr("&Name")
        self.nameL = self.createOneLineLabel(lbl)
        self.nameW = NameEdit(self.contentW)
        self.nameL.setBuddy(self.nameW)
        self.addLabelWidgetPair(self.nameL, self.nameW)
    def addDescriptionEdit(self, label=None):
        lbl = label
        if lbl is None:
            lbl = self.tr("&Description")
        self.descriptionL = self.createMultiLineLabel(lbl)
        self.descriptionW = DescriptionEdit(self.contentW)
        self.descriptionL.setBuddy(self.descriptionW)
        self.addLabelWidgetPair(self.descriptionL, self.descriptionW)
    def addSVGLoader(self, label=None):
        lbl = label
        if lbl is None:
            lbl = self.tr("&SVG File")
        self.svgLoaderL = self.createOneLineLabel(lbl)
        self.svgLoaderW = SVGLoaderWidget(self.contentW)
        self.svgLoaderL.setBuddy(self.svgLoaderW)
        self.addLabelWidgetPair(self.svgLoaderL, self.svgLoaderW)
    def createOneLineLabel(self, lbl):
        lbl = QLabel(lbl, self.contentW)
        lbl.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        return lbl
    def createMultiLineLabel(self, lbl):
        lbl = QLabel(lbl, self.contentW)
        lbl.setAlignment(Qt.AlignTop | Qt.AlignRight)
        return lbl
    def validate(self):
        return True
    def accept(self):
        if not self.validate():
            return
        try:
            if not self.data.hasId():
                QApplication.instance().db.session.add(self.data)
            QApplication.instance().db.session.commit()
            self.done(QDialog.Accepted)
        except IntegrityError, e:
            dlg = DatabaseExceptionDialog(QApplication.activeWindow(), e)
            dlg.exec_()
            QApplication.instance().db.session.rollback()
        except ConcurrentModificationError, e:
            dlg = DatabaseExceptionDialog(QApplication.activeWindow(), e)
            dlg.exec_()
            QApplication.instance().db.session.rollback()
        except ProgrammingError, e:
            dlg = DatabaseExceptionDialog(QApplication.activeWindow(), e)
            dlg.exec_()
            QApplication.instance().db.session.rollback()

    def reject(self):
        if self.data.hasId():
            QApplication.instance().db.session.refresh(self.data)
        self.done(QDialog.Rejected)
