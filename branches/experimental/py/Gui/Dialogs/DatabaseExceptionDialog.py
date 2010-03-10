from PyQt4.QtGui import *

from sqlalchemy.exc import *
from sqlalchemy.orm.exc import *

class DatabaseExceptionDialog(QMessageBox):
    def __init__(self, parent, exception):
        QMessageBox.__init__(self, parent)
        self.setIcon(QMessageBox.Critical)
        self.setWindowTitle(self.tr("Database Exception"))
        errType = exception.__class__.__name__
        if exception.__class__ == IntegrityError:
            errType = self.tr("Integrity")
        if exception.__class__ == SQLError:
            errType = self.tr("Generic Sql")
        if exception.__class__ == ArgumentError:
            errType = self.tr("Argument")
        if exception.__class__ == CircularDependencyError:
            errType = self.tr("Circular Dependency")
        if exception.__class__ == CompileError:
            errType = self.tr("Compile")
        if exception.__class__ == IdentifierError:
            errType = self.tr("Identifier")
        if exception.__class__ == ConcurrentModificationError:
            errType = self.tr("Concurrent Modification")
        if exception.__class__ == DisconnectionError:
            errType = self.tr("Disconnection")
        if exception.__class__ == FlushError:
            errType = self.tr("Flush Error")
        if exception.__class__ == TimeoutError:
            errType = self.tr("Timeout")
        if exception.__class__ == InvalidRequestError:
            errType = self.tr("Invalid Request")
        if exception.__class__ == NoSuchColumnError:
            errType = self.tr("No Such Column")
        if exception.__class__ == NoReferenceError:
            errType = self.tr("No Reference")
        if exception.__class__ == NoReferencedTableError:
            errType = self.tr("No Referenced Table")
        if exception.__class__ == NoReferencedColumnError:
            errType = self.tr("No Referenced Column")
        if exception.__class__ == NoSuchTableError:
            errType = self.tr("No Such Table")
        if exception.__class__ == UnboundExecutionError:
            errType = self.tr("Unbound Execution")
        if exception.__class__ == UnmappedColumnError:
            errType = self.tr("Unmapped Column")
        if exception.__class__ == DBAPIError:
            errType = self.tr("Database API")
        if exception.__class__ == InterfaceError:
            errType = self.tr("Interface")
        if exception.__class__ == DatabaseError:
            errType = self.tr("Database")
        if exception.__class__ == DataError:
            errType = self.tr("Data")
        if exception.__class__ == OperationalError:
            errType = self.tr("Operational")
        if exception.__class__ == IntegrityError:
            errType = self.tr("Integrity")
        if exception.__class__ == InternalError:
            errType = self.tr("Internal")
        if exception.__class__ == ProgrammingError:
            errType = self.tr("Programming")
        if exception.__class__ == NotSupportedError:
            errType = self.tr("Not Supported")
        self.setText(self.tr("A %1 Database Error Occured").arg(errType))
        self.setInformativeText(exception.__str__())
        self.addButton(QMessageBox.Ok)
