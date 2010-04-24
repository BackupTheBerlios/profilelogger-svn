from custom.Logic.Application.TestApp import *
from custom.Gui.Widgets.MainWindow.MainWindow import *

import sys

if '__main__' == __name__:
    print 'starting up...'
    a = TestApp(sys.argv)
    w = MainWindow()
    w.show()
    a.lastWindowClosed.connect(a.quit)
    sys.exit(a.exec_())
