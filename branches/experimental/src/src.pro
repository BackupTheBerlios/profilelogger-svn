TEMPLATE = app
TEMP_DIR = .tmp
OBJECTS_DIR = .obj
MOC_DIR = .moc
DESTDIR = bin
TARGET = exp

INCLUDEPATH += /usr/local/postgres/include
LIBS += -L/usr/local/postgres/lib -lpq
QT += core gui

HEADERS = App/ProfileLogger.h \
	App/Settings.h \
	Gui/MainWindow.h \
	Gui/HostEdit.h \
	Gui/LoginEdit.h \
	Gui/PasswordEdit.h \
	Dialogs/DatabaseConnectionDialog.h \
	Dialogs/DatabaseErrorDialog.h \
	DataModel/Dataset.h \
	DataModel/StandardDataset.h \
	DataModel/Project.h \
	Postgres/PostgresConnection.h \
	Postgres/PostgresConnectionSettings.h \
	Postgres/AbstractDatabaseError.h \
	Postgres/DatabaseError.h \
	DatabaseModel/CheckConstraint.h \
	DatabaseModel/Database.h \
	DatabaseModel/DbInterfacePart.h \
	DatabaseModel/DbInterfacePartInSchema.h \
	DatabaseModel/DbInterfacePartInTable.h \
	DatabaseModel/ForeignKey.h \
	DatabaseModel/PrimaryKey.h \
	DatabaseModel/Schema.h \
	DatabaseModel/Sequence.h \
	DatabaseModel/Table.h \
	DatabaseModel/TableColumn.h \
	DatabaseModel/TableConstraint.h \
	DatabaseModel/TextNotEmptyCheckConstraint.h \
	DatabaseModel/UniqueConstraint.h \
	SqlFactory/SqlFactory.h

SOURCES += main.cpp \
	App/ProfileLogger.cpp \
	App/Settings.cpp \
	Gui/MainWindow.cpp \
	Gui/HostEdit.cpp \
	Gui/LoginEdit.cpp \
	Gui/PasswordEdit.cpp \
	Dialogs/DatabaseConnectionDialog.cpp \
	Dialogs/DatabaseErrorDialog.cpp \
	DataModel/Dataset.cpp \
	DataModel/StandardDataset.cpp \
	DataModel/Project.cpp \
	Postgres/PostgresConnection.cpp \
	Postgres/PostgresConnectionSettings.cpp \
	Postgres/AbstractDatabaseError.cpp \
	Postgres/DatabaseError.cpp \
	DatabaseModel/CheckConstraint.cpp \
	DatabaseModel/Database.cpp \
	DatabaseModel/DbInterfacePart.cpp \
	DatabaseModel/DbInterfacePartInSchema.cpp \
	DatabaseModel/DbInterfacePartInTable.cpp \
	DatabaseModel/ForeignKey.cpp \
	DatabaseModel/PrimaryKey.cpp \
	DatabaseModel/Schema.cpp \
	DatabaseModel/Sequence.cpp \
	DatabaseModel/Table.cpp \
	DatabaseModel/TableColumn.cpp \
	DatabaseModel/TableConstraint.cpp \
	DatabaseModel/TextNotEmptyCheckConstraint.cpp \
	DatabaseModel/UniqueConstraint.cpp \
	SqlFactory/SqlFactory.cpp
