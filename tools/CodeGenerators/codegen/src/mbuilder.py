import sys
import os
from Entity import *
from Model import *
from DataType import *
from Constraint import *
from Database import *
from Schema import *
from Table import *
from PrimaryKey import *
from ForeignKey import *
from TableColumn import *
from Sequence import *
from Debugger import *
from PythonEntity import *
from PythonModule import *
from PythonField import *
from PythonClassSorting import *
from PythonClass import *
from PythonModelBuilder import *
from MyModel import *

def run():
    m = MyModel()

    d = Debugger()
    d.debug(m)

    pyModelBuilder = PythonModelBuilder()
    pyModelBuilder.build(m)

if '__main__' == __name__:
    run()
    sys.exit(0)
