TEMPLATE = app
DESTDIR = bin
MOC_DIR = .moc
TEMP_DIR = .tmp
OBJECTS_DIR = .obj
INCLUDEPATH += /usr/local/postgres/include
LIBS += -L/usr/local/postgres/lib -lpq

SOURCES += main.cpp \
DatabaseError.cpp \
Postgres.cpp

HEADERS += DatabaseError.h \
Postgres.h
