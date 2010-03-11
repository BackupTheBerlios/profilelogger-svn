from Gui.Dialogs.DatasetEditorDialog import *

from PyQt4.QtCore import *

class SVGItemEditorDialog(DatasetEditorDialog):
    def __init__(self, parent, data):
        DatasetEditorDialog.__init__(self, parent, data)
        self.addContentPanel(self.tr("SVG Item"))
        self.addIdDisplay()
        self.addNameEdit()
        self.addSVGLoader(self.tr("SVG Data"))
        self.addDescriptionEdit()
        self.addButtons()

        self.idW.setValue(self.data.id)
        self.nameW.setValue(unicode(self.data.name))
        self.descriptionW.setValue(unicode(self.data.description))
        self.svgLoaderW.setDataAndFileName(QString(self.data.svgData),
                                           QString(self.data.originalPath))
        self.nameW.nameChanged.connect(self.onNameChange)
        self.descriptionW.descriptionChanged.connect(self.onDescriptionChange)
        self.svgLoaderW.svgDataChanged.connect(self.onSvgDataChange)
        self.svgLoaderW.fileNameChanged.connect(self.onFileNameChange)
    def onNameChange(self, txt):
        self.data.name = unicode(txt)
    def onDescriptionChange(self, txt):
        self.data.description = unicode(txt)
    def onSvgDataChange(self, svgData):
        self.data.svgData = unicode(svgData)
    def onFileNameChange(self, fileName):
        self.data.originalPath = unicode(fileName)
