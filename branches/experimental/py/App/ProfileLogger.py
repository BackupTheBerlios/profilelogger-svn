from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Persistance.Database import *
from Persistance.ConnectionData import *

from Gui.Dialogs.DatabaseConnectionDialog import DatabaseConnectionDialog
from Gui.ItemModels.LengthUnitItemModel import LengthUnitItemModel

from Model.LengthUnit import LengthUnit

from App.Settings import Settings

class ProfileLogger(QApplication):
    databaseConnected = pyqtSignal(QString)
    
    def __init__(self, argv):
        QApplication.__init__(self, argv)
        self.setApplicationName('ProfileLogger')
        self.setApplicationVersion('2.0')
        self.setOrganizationName('lochisoft')
        self.setOrganizationDomain('lochisoft.org')

        self.setupActions()
        self.db = Database()
        self.lengthUnitModel = LengthUnitItemModel(self)

    def setupActions(self):
        self.quitA = QAction(self.tr('&Quit'), self)
        self.quitA.triggered.connect(QApplication.instance().quit);

        self.openDbA = QAction(self.tr('&Open Database...'), self)
        self.openDbA.setShortcut(QKeySequence('Ctrl+o'))
        self.openDbA.triggered.connect(self.onOpenDatabase)

        self.closeDbA = QAction(self.tr('&Close Database...'), self)
        self.closeDbA.triggered.connect(self.onCloseDatabase)

    def getFileActions(self):
        ret = []
        ret.append(self.quitA)
        return ret

    def getDatabaseActions(self):
        ret = []
        ret.append(self.openDbA)
        return ret;
    def onOpenDatabase(self):
        cd = Settings().loadConnectionData()
        dlg = DatabaseConnectionDialog(cd, self.activeWindow())
        if QDialog.Accepted == dlg.exec_():
            Settings().saveConnectionData(cd)
            print cd.makeInfoString()
            self.db.open(cd)
            self.databaseConnected.emit(cd.makeInfoString())
            if (cd.insertTemplateData):
                self.insertTemplateData()
            self.lengthUnitModel.reload()

    def insertTemplateData(self):
        self.db.begin()
        self.db.session.add(LengthUnit(None, 1, str(self.tr('mm'))))
        self.db.session.add(LengthUnit(None, 10, str(self.tr('cm'))))
        self.db.session.add(LengthUnit(None, 100, str(self.tr('dm'))))
        self.db.session.add(LengthUnit(None, 1000, str(self.tr('m'))))
        self.db.commit()

    def onCloseDatabase(self):
        print 'close database'
