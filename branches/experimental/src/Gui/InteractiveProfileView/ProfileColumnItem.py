from InteractiveRectItem import *

from BedItem import *

from Gui.Dialogs.DatabaseExceptionDialog import DatabaseExceptionDialog
from Gui.Dialogs.BedEditorDialog import *
from Gui.Dialogs.IntInputDialog import *

from sqlalchemy.exc import *
from sqlalchemy.orm.exc import *

class ProfileColumnItem(InteractiveRectItem):
    def __init__(self, parent, scene, rect, pos, legendFont, profile):
        InteractiveRectItem.__init__(self, parent, scene, rect, pos)
        self.legendFont = legendFont
        self.profile = profile
        self.drawBeds()
    def getSession(self):
        return QApplication.instance().db.session
    def drawBeds(self):
        self.maxY = 0
        self.clearChildren()
        for bed in self.profile.beds:
            itm = BedItem(self, self.scene(),
                          QRectF(0, 0, self.rect().width(), bed.heightInPixel()),
                          QPointF(0, self.maxY),
                          self.legendFont, 
                          bed)
            self.maxY += itm.rect().height()
            self.setRect(QRectF(0, 0, self.rect().width(), self.maxY))
    def editBed(self, bed):
        oldNumber = bed.number
        oldHeight = bed.heightInMillimetres
        dlg = BedEditorDialog(QApplication.activeWindow(), bed)
        if QDialog.Accepted == dlg.exec_():
            if oldNumber != bed.number or oldHeight != bed.heightInMillimetres:
                self.getSession().expire(self.profile)
            self.drawBeds()
        else:
            if not bed.hasId():
                self.getSession().expunge(bed)
    def createBedOnTop(self):
        self.editBed(self.profile.createBedOnTop())
    def createBedAtBottom(self):
        self.editBed(self.profile.createBedAtBottom())
    def deleteBed(self, bed):
        if QMessageBox.warning(QApplication.activeWindow(),
                               QCoreApplication.translate('Profile Column Item', 
                                                          "Delete?"),
                               QCoreApplication.translate('Profile Column Item', 
                                                          "Delete Bed %1?").arg(bed.number),
                               QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
            return
        try:
            self.getSession().delete(bed)
            self.getSession().expire(self.profile)
            self.getSession().commit();
            self.drawBeds()
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
    def splitBed(self, bed):
        pass
    def deleteBedsAbove(self, bed):
        delBeds = self.profile.getBedsAbove(bed)
        
        if QMessageBox.warning(QApplication.activeWindow(),
                               QCoreApplication.translate('Profile Column Item', 
                                                          "Delete?"),
                               QCoreApplication.translate('Profile Column Item', 
                                                          "Delete Beds %1-%2?").arg(delBeds[0].number).arg(delBeds[len(delBeds) - 1].number),
                               QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
            return
        try:
            for bed in delBeds:
                self.getSession().delete(bed)
            self.getSession().expire(self.profile)
            self.getSession().commit();
            self.drawBeds()
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
    def deleteBedsBelow(self, bed):
        delBeds = self.profile.getBedsBelow(bed)
        
        if QMessageBox.warning(QApplication.activeWindow(),
                               QCoreApplication.translate('Profile Column Item', 
                                                          "Delete?"),
                               QCoreApplication.translate('Profile Column Item', 
                                                          "Delete Beds %1-%2?").arg(delBeds[0].number).arg(delBeds[len(delBeds) - 1].number),
                               QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
            return
        try:
            for bed in delBeds:
                self.getSession().delete(bed)
            self.getSession().expire(self.profile)
            self.getSession().commit();
            self.drawBeds()
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
    def renumberFromBase(self):
        v = 0
        if self.profile.hasBeds():
            v = self.profile.beds[-1].number
        dlg = IntInputDialog(QApplication.activeWindow(),
                             QCoreApplication.translate('profile item rect',
                                                        'Base Bed Number'),
                             v)
        if dlg.exec_() != QDialog.Accepted:
            return
        v = dlg.getValue()
        try:
            tmpV = self.profile.getMaxBedNumber() + 1
            for bed in reversed(self.profile.beds):
                print bed.number," -> ",tmpV
                bed.number = tmpV
                tmpV += 1
            for bed in reversed(self.profile.beds):
                print bed.number," -> ",v
                bed.number = v
                v += 1
            self.getSession().commit();
            self.getSession().expire(self.profile)
            self.drawBeds()
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
    def renumberFromTop(self):
        v = 0
        if self.profile.hasBeds():
            v = self.profile.beds[-1].number
        dlg = IntInputDialog(QApplication.activeWindow(),
                             QCoreApplication.translate('profile item rect',
                                                        'Base Bed Number'),
                             v)
        if dlg.exec_() != QDialog.Accepted:
            return
        v = dlg.getValue()
        try:
            tmpV = self.profile.getMaxBedNumber() + 1
            for bed in reversed(self.profile.beds):
                print bed.number," -> ",tmpV
                bed.number = tmpV
                tmpV += 1
            for bed in self.profile.beds:
                print bed.number," -> ",v
                bed.number = v
                v -= 1
            self.getSession().commit();
            self.getSession().expire(self.profile)
            self.drawBeds()
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

    def mergeWithAbove(self, bed):
        pass
    def mergeWithBelow(self, bed):
        pass
    def createBedAbove(self, bed):
        pass
    def createBedBelow(self, bed):
        pass
    def splitProfileAbove(self, bed):
        pass
    def splitProfileBelow(self, bed):
        pass
    def insertProfileAbove(self, bed):
        pass
    def insertProfileBelow(self, bed):
        pass
