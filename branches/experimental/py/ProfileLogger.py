import sys

from App.ProfileLogger import ProfileLogger
from Gui.MainWindow import MainWindow

from Model.LengthUnit import LengthUnit
from Model.Project import *
from Model.Lithology import Lithology
from Model.Color import Color
from Model.BeddingType import BeddingType
from Model.SedimentStructure import SedimentStructure
from Model.CustomSymbol import CustomSymbol
from Model.Fossil import Fossil
from Model.GrainSizeType import GrainSizeType
from Model.GrainSize import GrainSize
from Model.BoundaryType import BoundaryType
from Model.PointOfInterest import PointOfInterest
from Model.Profile import Profile
from Model.Bed import Bed

from Model.LithologyInBed import LithologyInBed
from Model.ColorInBed import ColorInBed
from Model.BeddingTypeInBed import BeddingTypeInBed
from Model.CustomSymbolInBed import CustomSymbolInBed
from Model.SedimentStructureInBed import SedimentStructureInBed
from Model.FossilInBed import FossilInBed
from Model.GrainSizeInBed import GrainSizeInBed

from Persistance.ConnectionData import ConnectionData
from Persistance.Database import Database

if '__main__' == __name__:
    app = ProfileLogger(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
