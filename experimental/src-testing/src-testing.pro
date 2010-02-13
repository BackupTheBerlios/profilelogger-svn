TEMPLATE = app
DESTDIR = bin
MOC_DIR = .moc
TEMP_DIR = .tmp
OBJECTS_DIR = .obj
INCLUDEPATH += /usr/local/postgres/include
LIBS += -L/usr/local/postgres/lib -lpq
DEPENDPATH += dbModel sqlFactory dataModel
INCLUDEPATH += dbModel sqlFactory dataModel
QMAKE_CXXFLAGS += -Werror -ansi -Wall -pedantic -Wnon-virtual-dtor -Wno-long-long

SOURCES += main.cpp \
dbModel/AbstractDatabaseError.cpp \
sqlFactory/SqlFactory.cpp \
dbModel/DatabaseError.cpp \
pgInterface/Postgres.cpp \
DataManager.cpp \
ProjectManager.cpp \
dataModel/Dataset.cpp \
dbModel/CheckConstraint.cpp \
dbModel/Database.cpp \
dbModel/DbInterfacePart.cpp \
dbModel/DbInterfacePartInSchema.cpp \
dbModel/DbInterfacePartInTable.cpp \
dbModel/ForeignKey.cpp \
dbModel/PrimaryKey.cpp \
dbModel/Schema.cpp \
dbModel/Sequence.cpp \
dbModel/Table.cpp \
dbModel/TableColumn.cpp \
dbModel/TableConstraint.cpp \
dbModel/TextNotEmptyCheckConstraint.cpp \
dbModel/UniqueConstraint.cpp \
dbModel/AppDatabase.cpp \
dataModel/Project.cpp

HEADERS += dbModel/DatabaseError.h \
dbModel/AbstractDatabaseError.h \
dataModel/Project.h \
sqlFactory/SqlFactory.h \
pgInterface/Postgres.h \
DataManager.h \
ProjectManager.h \
dataModel/Dataset.h \
dbModel/CheckConstraint.h \
dbModel/Database.h \
dbModel/DbInterfacePart.h \
dbModel/DbInterfacePartInSchema.h \
dbModel/DbInterfacePartInTable.h \
dbModel/ForeignKey.h \
dbModel/PrimaryKey.h \
dbModel/Schema.h \
dbModel/Sequence.h \
dbModel/Table.h \
dbModel/TableColumn.h \
dbModel/TableConstraint.h \
dbModel/TextNotEmptyCheckConstraint.h \
dbModel/UniqueConstraint.h \
dbModel/AppDatabase.h
