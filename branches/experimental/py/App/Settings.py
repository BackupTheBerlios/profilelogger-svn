from PyQt4.QtCore import *

from Persistance.ConnectionData import ConnectionData

class Settings:
    def __init__(self):
        pass
    def saveConnectionData(self, c):
        s = QSettings()
        s.setValue('ConnectionData/Host', unicode(c.host))
        s.setValue('ConnectionData/Port', unicode(c.port))
        s.setValue('ConnectionData/Database', unicode(c.dbName))
        s.setValue('ConnectionData/Schema', unicode(c.schema))
        s.setValue('ConnectionData/User', unicode(c.user))
        s.setValue('ConnectionData/DropSchema', self.boolToString(c.dropSchema))
        s.setValue('ConnectionData/CreateSchema', self.boolToString(c.createSchema))
        s.setValue('ConnectionData/InsertTemplateData', self.boolToString(c.insertTemplateData))

    def loadConnectionData(self):
        s = QSettings()
        return ConnectionData(unicode(s.value('ConnectionData/Host').toString()),
                              unicode(s.value('ConnectionData/Port').toString()),
                              unicode(s.value('ConnectionData/Database').toString()),
                              unicode(s.value('ConnectionData/Schema').toString()),
                              unicode(s.value('ConnectionData/User').toString()),
                              '',
                              self.stringToBool(unicode(s.value('ConnectionData/DropSchema').toString())),
                              self.stringToBool(unicode(s.value('ConnectionData/CreateSchema').toString())),
                              self.stringToBool(unicode(s.value('ConnectionData/InsertTemplateData').toString())))

    def boolToString(self, arg):
        if arg:
            return unicode('Yes')
        else:
            return unicode('No')

    def stringToBool(self, s):
        if 'Yes' == s:
            return True
        else:
            return False
