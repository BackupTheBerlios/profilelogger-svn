from PythonEntity import *
from PythonClass import *
from PythonFinderClass import *
from PythonComboBoxClass import *
from PythonItemModelClass import *
from PythonTreeViewClass import *
from PythonManagementDialogClass import *

class PythonModule(PythonEntity):
    def __init__(self, parentModule, name):
        PythonEntity.__init__(self, parentModule, name)
        self.pythonModules = {}
        self.classes = {}
        self.finderClasses = {}
        self.comboBoxClasses = {}
        self.itemModelClasses = {}
        self.treeViewClasses = {}
        self.managementDialogClasses = {}
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
    def createManagementDialogClass(self, dataClassName, template, name=None, header=None):
        n = name
        if n is None:
            n = '%sManagementDialog' % dataClassName
        self.managementDialogClasses[n] = PythonManagementDialogClass(self, n, dataClassName, template, header)
        return self.managementDialogClassByName(n)
    def createFinderClass(self, dataClassName, template, name=None):
        n = name
        if n is None:
            n = '%sFinder' % dataClassName
        self.finderClasses[n] = PythonFinderClass(self, n, dataClassName, template)
        return self.finderClassByName(n)
    def createItemModelClass(self, dataClassName, template, name=None, headerStrings=[]):
        n = name
        if n is None:
            n = '%sItemModel' % dataClassName
        self.itemModelClasses[n] = PythonItemModelClass(self, n, dataClassName, template, headerStrings)
        return self.itemModelClassByName(n)
    def createTreeViewClass(self, dataClassName, template, name=None):
        n = name
        if n is None:
            n = '%sTreeView' % dataClassName
        self.treeViewClasses[n] = PythonTreeViewClass(self, n, dataClassName, template)
        return self.treeViewClassByName(n)
    def createComboBoxClass(self, dataClassName, template, name=None):
        n = name
        if n is None:
            n = '%sComboBox' % dataClassName
        self.comboBoxClasses[n] = PythonComboBoxClass(self, n, dataClassName, template)
        return self.comboBoxClassByName(n)
    def comboBoxClassByName(self, name):
        return self.comboBoxClasses[name]
    def finderClassByName(self, name):
        return self.finderClasses[name]
    def managementDialogClassByName(self, name):
        return self.managementDialogClasses[name]
    def itemModelClassByName(self, name):
        return self.itemModelClasses[name]
    def treeViewClassByName(self, name):
        return self.treeViewClasses[name]
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
   
