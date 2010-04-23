from Entity import *
from Database import *
from PythonModule import *
from DataType import *

class Model(Entity):
    def __init__(self, name):
        Entity.__init__(self, name)
        self.dataTypes = {}
        self.pythonModules = {}
        self.pythonDataModule = None
        self.comoboBoxModule = None
        self.itemModelModule = None
        self.treeViewModule = None
        self.editorDialogModule=None
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
    def createComboBoxClasses(self, module, classNameTemplatePairs):
        for i in classNameTemplatePairs:
            module.createComboBoxClass(i[0], i[1])
    def createFinderClasses(self, module, classNameTemplatePairs):
        for i in classNameTemplatePairs:
            module.createFinderClass(i[0], i[1])
    def createTreeViewClasses(self, module, classNameTemplatePairs):
        for i in classNameTemplatePairs:
            module.createTreeViewClass(i[0], i[1])
    def createItemModelClasses(self, module, classNameTemplateHeadersList):
        for i in classNameTemplateHeadersList:
            module.createItemModelClass(i[0], i[1], headerStrings=i[2])
    def createManagementDialogClasses(self, module, classNameTemplateHeaderList):
        for i in classNameTemplateHeaderList:
            module.createManagementDialogClass(i[0], i[1], header=i[2])
    def createEditorDialogClasses(self, module, classNameTemplatePairs):
        for i in classNameTemplatePairs:
            module.createEditorDialogClass(i[0], i[1])
    def createEditorDialogClasses(self, module, classNameTemplatePairs):
        for i in classNameTemplatePairs:
            module.createEditorDialogClass(i[0], i[1])
