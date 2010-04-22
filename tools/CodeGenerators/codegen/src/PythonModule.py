from PythonEntity import *
from PythonClass import *

class PythonModule(PythonEntity):
    def __init__(self, parentModule, name):
        PythonEntity.__init__(self, parentModule, name)
        self.pythonModules = {}
        self.classes = {}
    def createClass(self, name, parentClass, table, 
                    createIdField=False, 
                    createNameField=False, 
                    createDescriptionField=False, 
                    template=None):
        self.classes[name] = PythonClass(self, parentClass, name, table, 
                                         createIdField=createIdField, 
                                         createNameField=createNameField, 
                                         createDescriptionField=createDescriptionField,
                                         template=template)
        return self.classByName(name)
    def classByName(self, name):
        return self.classes[name]
    def createPythonModule(self, name):
        self.pythonModules[name] = PythonModule(self, name)
        return self.pythonModule(name)
    def pythonModule(self, name):
        return self.pythonModules[name]
    def __str__(self):
        if self.parent is not None:
            return '%s.%s' % (self.parent.__str__(), self.name)
        else:
            return self.name
