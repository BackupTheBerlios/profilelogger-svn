import sys

from App.ProfileLogger import ProfileLogger
from Gui.MainWindow import MainWindow

from Gui.Dialogs.DatabaseExceptionDialog import DatabaseExceptionDialog

from sqlalchemy.exc import *

if '__main__' == __name__:
    try:
        app = ProfileLogger(sys.argv)
        w = MainWindow()
        w.show()
        sys.exit(app.exec_())
    except DisconnectionError, e:
        dlg = DatabaseExceptionDialog(app.activeWindow(), e)
        dlg.exec_()
    except InternalError, e:
        dlg = DatabaseExceptionDialog(app.activeWindow(), e)
        dlg.exec_()
        
    

