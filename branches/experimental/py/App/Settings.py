from PyQt4.QtCore import *

from Persistance.ConnectionData import ConnectionData

class Settings:
    def __init__(self):
        pass
    def saveConnectionData(self, c):
        s = QSettings()
        s.setValue('ConnectionData/Host', str(c.host))
        s.setValue('ConnectionData/Port', str(c.port))
        s.setValue('ConnectionData/Database', str(c.dbName))
        s.setValue('ConnectionData/Schema', str(c.schema))
        s.setValue('ConnectionData/User', str(c.user))
        s.setValue('ConnectionData/DropSchema', self.boolToString(c.dropSchema))
        s.setValue('ConnectionData/CreateSchema', self.boolToString(c.createSchema))
        s.setValue('ConnectionData/InsertTemplateData', self.boolToString(c.insertTemplateData))

    def loadConnectionData(self):
        s = QSettings()
        return ConnectionData(str(s.value('ConnectionData/Host').toString()),
                              str(s.value('ConnectionData/Port').toString()),
                              str(s.value('ConnectionData/Database').toString()),
                              str(s.value('ConnectionData/Schema').toString()),
                              str(s.value('ConnectionData/User').toString()),
                              '',
                              self.stringToBool(str(s.value('ConnectionData/DropSchema').toString())),
                              self.stringToBool(str(s.value('ConnectionData/CreateSchema').toString())),
                              self.stringToBool(str(s.value('ConnectionData/InsertTemplateData').toBool())))

    def boolToString(self, arg):
        if arg:
            return str('Yes')
        else:
            return str('No')

    def stringToBool(self, s):
        if 'Yes' == s:
            return True
        else:
            return False
