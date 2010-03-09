import sys

#from app.ProfileLogger import ProfileLogger

from Model.LengthUnit import LengthUnit
from Model.Project import *
from Model.Lithology import Lithology
from Model.Color import Color
from Model.BeddingType import BeddingType
from Model.SedimentStructure import SedimentStructure
from Model.CustomSymbol import CustomSymbol
from Model.Fossil import Fossil
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
    cd = ConnectionData('192.168.196.133', 5432, 'profilelogger', 'data', 'jolo', 'nix')
    cd.dropSchema = True
    cd.createSchema = True

    db = Database()
    db.open(cd)

    mm = LengthUnit(1, 1, "mm")
    cm = LengthUnit(1, 10, 'cm')
    dm = LengthUnit(1, 100, 'dm')
    m = LengthUnit(1, 1000, 'm')
    
    p = Project(0, "test", "nix")

    s = db.begin()
    s.add(p)
    s.commit()

    chert = Lithology(p, 0, "Chert")
    chalk = Lithology(p, 1, "Chalk")

    red = Color(p, 0, "red");
    blue = Color(p, 1, "blue");
    black = Color(p, 2, "black");

    planar = BeddingType(p, 0, "Planar")
    massive = BeddingType(p, 1, "Massive")
    channel = SedimentStructure(p, 0, "Channel")
    bivalve = Fossil(p, 0, "Bivalve")
    samplePoint = CustomSymbol(p, 0, "Sampling Point")
    mudstone = GrainSize(p, 0, "Mudstone")
    sharpPlanar = BoundaryType(p, 0, "Sharp Planar")
    hg = PointOfInterest(p, 0, u"Hoellgraben")
    hg1 = Profile(p, 0, u"Hoellgraben 1")
    hg2 = Profile(p, 0, u"Hoellgraben 2")
    
    b1 = Bed(hg1, 0, 1, m, 1)
    LithologyInBed(b1, 0, chert, 0, 100)
    ColorInBed(b1, 0, black, 20, 100)
    BeddingTypeInBed(b1, 0, planar, 0, 100)
    CustomSymbolInBed(b1, 0, samplePoint, 30, 35)
    SedimentStructureInBed(b1, 0, channel, 65, 90)
    FossilInBed(b1, 0, bivalve, 80, 83)
    GrainSizeInBed(b1, 0, mudstone, 0, 80)
    b2 = Bed(hg1, 1, 1, m, 2)

    p.debug()

    sys.exit(0)
