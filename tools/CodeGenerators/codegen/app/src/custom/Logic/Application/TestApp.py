from PyQt4.QtCore import *
from PyQt4.QtGui import *

from custom.Logic.Persistance.Database import *

class TestApp(QApplication):
    def __init__(self, argv):
        QApplication.__init__(self, argv)
        self.db = None
    def connectToDatabase(self):
        if self.db is None:
            self.db = Database()
        cd = ConnectionData('192.168.196.137',
                            '5432',
                            'codegen',
                            'jolo',
                            'nix',
                            True)
        self.db.open(cd)
    def closeDatabaseConnection(self):
        pass
