from PythonEntity import *
from PythonClass import *
from PythonFinderClass import *

class PythonModule(PythonEntity):
    def __init__(self, parentModule, name):
        PythonEntity.__init__(self, parentModule, name)
        self.pythonModules = {}
        self.classes = {}
        self.finderClasses = {}
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
    def createFinderClass(self, dataClassName, template, name=None):
        n = name
        if n is None:
            n = '%sFinder' % dataClassName
        self.finderClasses[n] = PythonFinderClass(self, n,
                                                  dataClassName, template)
        return self.finderClassByName(n)
    def finderClassByName(self, name):
        return self.finderClasses[name]
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
    def fullName(self):
        if self.hasParent():
            return '%s.%s' % (self.parent.fullName(), self.name)
        return self.name
   
