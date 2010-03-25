from Dialog import Dialog

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class DatabaseConnectionDialog(Dialog):
    def __init__(self, connectionData, parent):
        Dialog.__init__(self, parent)
        self.cd = connectionData

        self.setLayout(QVBoxLayout(self))

        self.gb = QGroupBox(self)
        self.gb.setTitle(self.tr('Database Connection'))
        self.bb = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
                                   Qt.Horizontal, self)
        self.bb.accepted.connect(self.accept)
        self.bb.rejected.connect(self.reject)

        self.layout().addWidget(self.gb)
        self.layout().addWidget(self.bb)

        self.setupWidgets()
        self.hostW.setText(unicode(self.cd.host))
        self.portW.setText(unicode(self.cd.port))
        self.dbW.setText(unicode(self.cd.dbName))
        self.schemaW.setText(unicode(self.cd.schema))
        self.loginW.setText(unicode(self.cd.user))
        self.passwordW.setText(unicode(self.cd.password))
        if self.cd.createSchema:
            self.createSchemaW.setCheckState(Qt.Checked)
        if self.cd.insertTemplateData:
            self.insertTemplateDataW.setCheckState(Qt.Checked)
        self.passwordW.setFocus()

    def setupWidgets(self):
        self.gb.setLayout(QGridLayout(self.gb))

        lC = 0;
        wC = 1
        r = 0

        self.hostL = QLabel(self.tr('&Host'), self.gb)
        self.hostW = QLineEdit(self.gb)
        self.hostL.setBuddy(self.hostW)
        self.gb.layout().addWidget(self.hostL, r, lC)
        self.gb.layout().addWidget(self.hostW, r, wC);
        self.hostW.textChanged.connect(self.onHostChange)
        r += 1

        self.portL = QLabel(self.tr('&Port'), self.gb)
        self.portW = QLineEdit(self.gb)
        self.gb.layout().addWidget(self.portL, r, lC)
        self.portL.setBuddy(self.portW)
        self.gb.layout().addWidget(self.portW, r, wC);
        self.portW.textChanged.connect(self.onPortChange)
        r += 1

        self.dbL = QLabel(self.tr('&Database'), self.gb)
        self.dbW = QLineEdit(self.gb)
        self.dbL.setBuddy(self.dbW)
        self.gb.layout().addWidget(self.dbL, r, lC)
        self.gb.layout().addWidget(self.dbW, r, wC);
        self.dbW.textChanged.connect(self.onDatabaseChange)
        r += 1

        self.schemaL = QLabel(self.tr('&Schema'), self.gb)
        self.schemaW = QLineEdit(self.gb)
        self.schemaL.setBuddy(self.schemaW)
        self.gb.layout().addWidget(self.schemaL, r, lC)
        self.gb.layout().addWidget(self.schemaW, r, wC);
        self.schemaW.textChanged.connect(self.onSchemaChange)
        r += 1

        self.loginL = QLabel(self.tr('&Login'), self.gb)
        self.loginW = QLineEdit(self.gb)
        self.loginL.setBuddy(self.loginW)
        self.gb.layout().addWidget(self.loginL, r, lC)
        self.gb.layout().addWidget(self.loginW, r, wC);
        self.loginW.textChanged.connect(self.onLoginChange)
        r += 1

        self.passwordL = QLabel(self.tr('P&assword'), self.gb)
        self.passwordW = QLineEdit(self.gb)
        self.passwordW.setEchoMode(QLineEdit.Password)
        self.passwordL.setBuddy(self.passwordW)
        self.gb.layout().addWidget(self.passwordL, r, lC)
        self.gb.layout().addWidget(self.passwordW, r, wC);
        self.passwordW.textChanged.connect(self.onPasswordChange)
        r += 1

        self.createSchemaW = QCheckBox(self.tr("Create Schema"), self.gb)
        self.gb.layout().addWidget(self.createSchemaW, r, wC);
        self.createSchemaW.toggled.connect(self.onCreateSchemaToggle)
        r += 1

        self.insertTemplateDataW = QCheckBox(self.tr("Insert Template Data"), self.gb)
        self.gb.layout().addWidget(self.insertTemplateDataW, r, wC)
        self.insertTemplateDataW.toggled.connect(self.onInsertTemplateDataToggle)

    def onHostChange(self, txt):
        self.cd.host = unicode(txt)
    def onPortChange(self, port):
        self.cd.port = unicode(port)
    def onDatabaseChange(self, db):
        self.cd.dbName = unicode(db)
    def onSchemaChange(self, s):
        self.cd.schema = s
    def onLoginChange(self, l):
        self.cd.user = unicode(l)
    def onPasswordChange(self, p):
        self.cd.password = unicode(p)
    def onCreateSchemaToggle(self, t):
        self.cd.createSchema = t
    def onInsertTemplateDataToggle(self, t):
        self.cd.insertTemplateData = t
