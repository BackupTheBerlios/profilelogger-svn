from Entity import *
from Database import *
from PythonModule import *
from DataType import *

class Model(Entity):
    def __init__(self, name):
        Entity.__init__(self, name)
        self.dataTypes = {}
        self.pythonModules = {}
        self.pythonDataClasses = None
        self.comoboBoxModule = None
    def createDatabase(self, name):
        self.database = Database(self, name)
        return self.database
    def createDataType(self, name):
        self.dataTypes[name] = DataType(self, name)
        return self.dataType(name)
    def dataType(self, name):
        return self.dataTypes[name]
    def createPythonModule(self, name):
        self.pythonModules[name] = PythonModule(None, name)
        return self.pythonModule(name)
    def pythonModule(self, name):
        return self.pythonModules[name]
