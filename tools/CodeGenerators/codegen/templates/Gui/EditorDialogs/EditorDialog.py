from Dialog import Dialog

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Gui.Dialogs.DatabaseExceptionDialog import DatabaseExceptionDialog

from sqlalchemy.exc import *
from sqlalchemy.orm.exc import *

class EditorDialog(Dialog):
    def __init__(self, parent, entity):
        Dialog.__init__(self, parent)
        self.entity = entity
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
    def showFailedValidation(self):
        QMessageBox.information(self,
                                self.tr("Input incomplete"),
                                self.tr("Please Check Your Input. It's incomplete"))
    def save(self):
        if not self.validate():
            self.showFailedValidation()
            return
        try:
            if not self.entity.hasId():
                QApplication.instance().db.session.add(self.entity)
            QApplication.instance().db.session.commit()
            return True
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
        return False
    def accept(self):
        if not self.validate():
            self.showFailedValidation()
            return
        if self.save():
            self.done(QDialog.Accepted)
    def reject(self):
        if self.entity.hasId():
            QApplication.instance().db.session.refresh(self.entity)
        self.done(QDialog.Rejected)
