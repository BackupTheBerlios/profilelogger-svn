from InteractiveRectItem import *

from BedItem import *

from Gui.Dialogs.DatabaseExceptionDialog import DatabaseExceptionDialog
from Gui.Dialogs.BedEditorDialog import *
from Gui.Dialogs.IntInputDialog import *

from sqlalchemy.exc import *
from sqlalchemy.orm.exc import *

from Model.Bed import *

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
        above = self.profile.bedAbove(bed)
        if above is None:
            QMessageBox.information(QApplication.activeWindow(),
                                    QApplication.translate('profile column item', 'No Item'),
                                    QApplication.translate('profile column item', 'No Bed Above'))
            return
        if above.lengthUnit != bed.lengthUnit:
            QMessageBox.error(QApplication.activeWindow(),
                              QApplication.translate('profile column item', 'Error'),
                              QApplication.translate('profile column item', 'Beds must have same length unit.'))
            return
        if QMessageBox.question(QApplication.activeWindow(),
                                QApplication.translate('profile column item', 'Merge?'),
                                QApplication.translate('profile column item', 
                                                       QString('Merge %1 and %2?').arg(bed.number).arg(above.number)),
                                QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
            return
        try:
            self.profile.mergeBeds(bed, above)
            self.getSession().delete(above)
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
    def mergeWithBelow(self, bed):
        below = self.profile.bedBelow(bed)
        if below is None:
            QMessageBox.information(QApplication.activeWindow(),
                                    QApplication.translate('profile column item', 'No Item'),
                                    QApplication.translate('profile column item', 'No Bed Below'))
            return
        if below.lengthUnit != bed.lengthUnit:
            QMessageBox.error(QApplication.activeWindow(),
                              QApplication.translate('profile column item', 'Error'),
                              QApplication.translate('profile column item', 'Beds must have same length unit.'))
            return
        if QMessageBox.question(QApplication.activeWindow(),
                                QApplication.translate('profile column item', 'Merge?'),
                                QApplication.translate('profile column item', 
                                                       QString('Merge %1 and %2?').arg(bed.number).arg(below.number)),
                                QMessageBox.Yes | QMessageBox.No) != QMessageBox.Yes:
            return
        try:
            self.profile.mergeBeds(below, bed)
            self.getSession().delete(below)
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
    def createBedAbove(self, bed):
        if bed is None:
            return
        nmbr = bed.number + 1
        try:
            for b in reversed(self.profile.beds):
                if b.number > nmbr:
                    b.number += 1
            bed = Bed(self.profile, None, 0, None, nmbr)
            self.editBed(bed)
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
    def createBedBelow(self, bed):
        if bed is None:
            return
        nmbr = bed.number - 1
        try:
            for b in reversed(self.profile.beds):
                if b.number < nmbr:
                    b.number -= 1
            bed = Bed(self.profile, None, 0, None, nmbr)
            self.editBed(bed)
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
    def splitProfileAbove(self, bed):
        pass
    def splitProfileBelow(self, bed):
        pass
    def insertProfileAbove(self, bed):
        pass
    def insertProfileBelow(self, bed):
        pass
    def moveUp(self, bed):
        above = self.profile.bedAbove(bed)
        if above is None:
            QMessageBox.information(QApplication.activeWindow(),
                                    QApplication.translate('profile column item', 'No Item'),
                                    QApplication.translate('profile column item', 'No Bed Above'))
            return
        try:
            aboveNum = above.number
            myNum = bed.number
            above.number = myNum
            bed.number = aboveNum
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
    def moveDown(self, bed):
        below = self.profile.bedBelow(bed)
        if below is None:
            QMessageBox.information(QApplication.activeWindow(),
                                    QApplication.translate('profile column item', 'No Item'),
                                    QApplication.translate('profile column item', 'No Bed Below'))
            return
        try:
            belowNum = below.number
            myNum = bed.number
            below.number = myNum
            bed.number = belowNum
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
