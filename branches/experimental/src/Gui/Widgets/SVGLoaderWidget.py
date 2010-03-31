from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSvg import *

class SVGLoaderWidget(QWidget):
    svgDataChanged = pyqtSignal(QString)
    fileNameChanged = pyqtSignal(QString)

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setLayout(QHBoxLayout(self))
        self.svgData = None
        self.path = None
        self.viewerW = QSvgWidget(self)
        self.pathW = QLineEdit(self.tr("<Not Set>"), self)
        self.viewerW.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.viewerW.setMaximumSize(self.size().height(),
                                    self.size().width() * 0.2)
        self.pathW.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        self.browseW = QPushButton(self.tr("..."), self)
        self.layout().addWidget(self.viewerW)
        self.layout().addWidget(self.pathW)
        self.layout().addWidget(self.browseW)
        
        self.browseW.clicked.connect(self.onBrowse)
    def onBrowse(self):
        fi = QFileInfo()
        if self.path is not None:
            fi.setFile(self.path)
        else:
            fi.setFile(QDir.currentPath())
        newPath = QFileDialog.getOpenFileName(self,
                                              self.tr("Select SVG File"),
                                              fi.canonicalPath(),
                                              self.tr("SVG Files (*.svg *.SVG)"))
        if newPath is None:
            return
        self.path = newPath
        self.pathW.setText(unicode(self.path))
        # load data from file
        f = QFile(unicode(self.path))
        if not f.open(QIODevice.ReadOnly):
            QMessageBox.critical(self,
                                 self.tr("Could Not Read File"),
                                 self.tr("Could not read file '%1': %2")
                                 .arg(self.path)
                                 .arg(f.error()))
            return
        istrm = QTextStream(f)
        self.svgData = istrm.readAll()
        f.close()
        self.showContent()
        self.svgDataChanged.emit(self.svgData)
        self.fileNameChanged.emit(self.path)
    def setDataAndFileName(self, svgData, fileName):
        if svgData is not None:
            self.svgData = QString(svgData)
        else:
            self.svgData = None
        if fileName is not None:
            self.path = QString(fileName)
        else:
            self.path = None
        self.showContent()
    def showContent(self):
        if self.svgData is not None:
            self.viewerW.load(self.svgData.toLocal8Bit())
        if self.path is not None:
            self.pathW.setText(self.path)
