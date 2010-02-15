TEMPLATE = app

TARGET = profilelogger
DESTDIR = ../bin

QT += core gui svg xml sql

# include postgres stuff
INCLUDEPATH += /usr/local/postgres/include
LIBS += -L/usr/local/postgres/lib -lpq

unix {
message(building on unix)
CONFIG += debug core gui svg xml sql
QMAKE_CXXFLAGS += -Werror
}

win {
message(Building on windows)
CONFIG += release core gui svg xml sql
QMAKE_CXXFLAGS += -Werror
}

mac {
message(Building on Mac)
CONFIG += debug core gui svg xml sql
QMAKE_CXXFLAGS += -Werror
}

MOC_DIR = .moc
OBJECTS_DIR = .obj
TEMP_DIR = .tmp

TRANSLATIONS = i18n/profilelogger_en.ts \
i18n/profilelogger_de.ts

CODECFORTR = UTF-8

DEPENDPATH += .
INCLUDEPATH += .

message(Qt version: $$[QT_VERSION])
message(Qt is installed in $$[QT_INSTALL_PREFIX])
message(Qt resources can be found in the following locations:)
message(Documentation: $$[QT_INSTALL_DOCS])
message(Header files: $$[QT_INSTALL_HEADERS])
message(Libraries: $$[QT_INSTALL_LIBS])
message(Binary files (executables): $$[QT_INSTALL_BINS])
message(Plugins: $$[QT_INSTALL_PLUGINS])
message(Data files: $$[QT_INSTALL_DATA])
message(Translation files: $$[QT_INSTALL_TRANSLATIONS])
message(Settings: $$[QT_INSTALL_SETTINGS])
message(Examples: $$[QT_INSTALL_EXAMPLES])
message(Demonstrations: $$[QT_INSTALL_DEMOS])

DEPENDPATH += . \
              columnView \
              correlationView \
              dataManager \
              dataModel \
              dbModel \
              dialogs \
              fileInterfaces \
              i18n \
              items \
              models \
              nonGui \
              pgInterface \
              sqlFactory \
              views \
              widgets
INCLUDEPATH += . \
               nonGui \
               items \
               views \
               dataModel \
               columnView \
               widgets \
               dialogs \
               models \
               correlationView \
               dbModel \
               sqlFactory \
               dataManager \
               pgInterface \
               fileInterfaces

COLUMN_VIEW_HEADERS = \
           columnView/BeddingTypeLegendItem.h \
           columnView/BoundaryTypeLegendItem.h \
           columnView/ColorLegendItem.h \
           columnView/CustomSymbolLegendItem.h \
           columnView/FaciesLegendItem.h \
           columnView/FossilLegendItem.h \
           columnView/GraphicBedItem.h \
           columnView/GraphicColumnBody.h \
           columnView/GraphicColumnHeader.h \
           columnView/GraphicColumnWidget.h \
           columnView/GraphicLegendItem.h \
           columnView/GraphicSvgItem.h \
           columnView/LegendItem.h \
           columnView/LithologyLegendItem.h \
           columnView/OutcropQualityLegendItem.h \
           columnView/PatternLegendItem.h \
           columnView/SedimentStructureLegendItem.h \
           columnView/SymbolLegendItem.h 

CORRELATION_VIEW_HEADERS = \
           correlationView/BedCorrelationView.h 

DATA_MANAGER_HEADERS = \
           dataManager/DataManager.h \
           dataManager/ProjectManager.h 

DATA_MODEL_HEADERS = \
           dataModel/Bed.h \
           dataModel/BedCorrelation.h \
           dataModel/BeddingType.h \
           dataModel/BoundaryType.h \
           dataModel/CarbonateGrainSize.h \
           dataModel/ClasticGrainSize.h \
           dataModel/Color.h \
           dataModel/CustomSymbol.h \
           dataModel/Dataset.h \
           dataModel/DatasetWithFileName.h \
           dataModel/Facies.h \
           dataModel/Fossil.h \
           dataModel/GrainSize.h \
           dataModel/GrainSizeModes.h \
           dataModel/LengthMeasurement.h \
           dataModel/LengthUnit.h \
           dataModel/LithologicalUnit.h \
           dataModel/LithologicalUnitType.h \
           dataModel/Lithology.h \
           dataModel/OutcropQuality.h \
           dataModel/PrimitiveDataset.h \
           dataModel/Profile.h \
           dataModel/ProfileCorrelation.h \
           dataModel/ProfileInCorrelation.h \
           dataModel/Project.h \
           dataModel/Sample.h \
           dataModel/SedimentStructure.h 

DB_MODEL_HEADERS = \
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
           dbModel/UniqueConstraint.h 

DIALOG_HEADERS = \
           dialogs/DatabaseConnectionDialog.h \
           dialogs/BedCorrelationEditorDialog.h \
           dialogs/BeddingTypeEditorDialog.h \
           dialogs/BedEditorDialog.h \
           dialogs/BoundaryTypeEditorDialog.h \
           dialogs/ColorEditorDialog.h \
           dialogs/CsvProfileImportSettingsDialog.h \
           dialogs/CustomSymbolEditorDialog.h \
           dialogs/DatabaseErrorDialog.h \
           dialogs/DatasetEditorDialog.h \
           dialogs/DatasetWithFileNameEditorDialog.h \
           dialogs/FaciesEditorDialog.h \
           dialogs/FossilEditorDialog.h \
           dialogs/ImageEditorDialog.h \
           dialogs/ListSelectorDialog.h \
           dialogs/LithologicalUnitEditorDialog.h \
           dialogs/LithologicalUnitTypeEditorDialog.h \
           dialogs/LithologyEditorDialog.h \
           dialogs/OutcropQualityEditorDialog.h \
           dialogs/ProfileCorrelationEditorDialog.h \
           dialogs/ProfileEditorDialog.h \
           dialogs/ProfileSelectorDialog.h \
           dialogs/SampleEditorDialog.h \
           dialogs/SedimentStructureEditorDialog.h \
           dialogs/SettingsDialog.h \
           dialogs/ProjectEditorDialog.h 

FILE_INTERFACE_HEADERS = \
           fileInterfaces/CsvInterface.h \
           fileInterfaces/CsvProfileImportSettings.h \
           fileInterfaces/ProfileImportSettings.h \
           fileInterfaces/XMLInterface.h 

ITEM_HEADERS = \
           items/BedCorrelationItem.h \
           items/BeddingTypeItem.h \
           items/BedItem.h \
           items/BoundaryTypeItem.h \
           items/CarbonateGrainSizeItem.h \
           items/ClasticGrainSizeItem.h \
           items/ColorItem.h \
           items/CustomSymbolItem.h \
           items/FaciesItem.h \
           items/FossilItem.h \
           items/GrainSizeItem.h \
           items/ImageItem.h \
           items/LithologicalUnitItem.h \
           items/LithologicalUnitTypeItem.h \
           items/LithologyItem.h \
           items/OutcropQualityItem.h \
           items/ProfileCorrelationItem.h \
           items/ProfileItem.h \
           items/SampleItem.h \
           items/SedimentStructureItem.h \
           items/StandardItem.h \
           items/ProjectItem.h 

MODEL_HEADERS = \
           models/ProjectItemModel.h \
           models/BedCorrelationItemModel.h \
           models/BeddingTypeItemModel.h \
           models/BedItemModel.h \
           models/BoundaryTypeItemModel.h \
           models/CarbonateGrainSizeItemModel.h \
           models/ClasticGrainSizeItemModel.h \
           models/ColorItemModel.h \
           models/CustomSymbolInBedItemModel.h \
           models/CustomSymbolItemModel.h \
           models/FaciesItemModel.h \
           models/FossilInBedItemModel.h \
           models/FossilItemModel.h \
           models/GrainSizeItemModel.h \
           models/ImageItemModel.h \
           models/LithologicalUnitItemModel.h \
           models/LithologicalUnitTypeItemModel.h \
           models/LithologyItemModel.h \
           models/OutcropQualityItemModel.h \
           models/ProfileCorrelationItemModel.h \
           models/ProfileItemModel.h \
           models/SampleItemModel.h \
           models/SedimentStructureInBedItemModel.h \
           models/SedimentStructureItemModel.h \
           models/StandardItemModel.h 

NON_GUI_HEADERS = \
           nonGui/AppDatabase.h \
           nonGui/Image.h \
           nonGui/ProfileLogger.h \
           nonGui/ProfileLoggerDatabase.h \
           nonGui/Settings.h \
           nonGui/SymbolFactory.h \
           nonGui/Version.h 

PG_INTERFACE_HEADERS = \
           pgInterface/AbstractDatabaseError.h \
           pgInterface/DatabaseError.h \
           pgInterface/Postgres.h \
           pgInterface/DatabaseConnectionSettings.h 

SQL_FACTORY_HEADERS = \
           sqlFactory/SqlFactory.h 

VIEW_HEADERS = \
           views/BedCorrelationItemView.h \
           views/BeddingTypeView.h \
           views/BedItemView.h \
           views/BoundaryTypeView.h \
           views/CarbonateGrainSizeView.h \
           views/ClasticGrainSizeView.h \
           views/ColorView.h \
           views/CustomSymbolInBedView.h \
           views/CustomSymbolView.h \
           views/FaciesView.h \
           views/FossilInBedView.h \
           views/FossilView.h \
           views/GrainSizeView.h \
           views/GraphicColumnBody.h \
           views/ImageItemView.h \
           views/LithologicalUnitTypeView.h \
           views/LithologicalUnitView.h \
           views/LithologyView.h \
           views/OutcropQualityView.h \
           views/ProfileCorrelationItemView.h \
           views/ProfileItemView.h \
           views/SampleItemView.h \
           views/SedimentStructureInBedView.h \
           views/SedimentStructureView.h \
           views/TreeView.h \
           views/ProjectView.h 

WIDGET_HEADERS = \
           widgets/BedPropertyPage.h \
           widgets/DescriptionEdit.h \
           widgets/FileNameBrowserWidget.h \
           widgets/GrainSizeModeSelectorWidget.h \
           widgets/GrainSizeSelectorWidget.h \
           widgets/HostEdit.h \
           widgets/IdLabel.h \
           widgets/ImageFileNameBrowserWidget.h \
           widgets/LengthMeasurementWidget.h \
           widgets/LengthUnitsComboBox.h \
           widgets/LoginEdit.h \
           widgets/MainWindow.h \
           widgets/ManagementToolBox.h \
           widgets/NameEdit.h \
           widgets/PasswordEdit.h \
           widgets/ProfileCorrelationWidget.h \
           widgets/ProfileWorkWidget.h \
           widgets/QtPatternSelectorWidget.h \
           widgets/WorkWidget.h \
           widgets/DbWorkWidget.h

HEADERS += $$COLUMN_VIEW_HEADERS \
           $$CORRELATION_VIEW_HEADERS \
           $$DATA_MANAGER_HEADERS \
           $$DATA_MODEL_HEADERS \
           $$DB_MODEL_HEADERS \
           $$DIALOG_HEADERS \
           $$FILE_INTERFACE_HEADERS \
           $$ITEM_HEADERS \
           $$MODEL_HEADERS \
           $$NON_GUI_HEADERS \
           $$PG_INTERFACE_HEADERS \
           $$SQL_FACTORY_HEADERS \
           $$VIEW_HEADERS \
           $$WIDGET_HEADERS

COLUMN_VIEW_SRC = \
           columnView/BeddingTypeLegendItem.cpp \
           columnView/BoundaryTypeLegendItem.cpp \
           columnView/ColorLegendItem.cpp \
           columnView/CustomSymbolLegendItem.cpp \
           columnView/FaciesLegendItem.cpp \
           columnView/FossilLegendItem.cpp \
           columnView/GraphicBedItem.cpp \
           columnView/GraphicColumnBody.cpp \
           columnView/GraphicColumnHeader.cpp \
           columnView/GraphicColumnWidget.cpp \
           columnView/GraphicLegendItem.cpp \
           columnView/GraphicSvgItem.cpp \
           columnView/LegendItem.cpp \
           columnView/LithologyLegendItem.cpp \
           columnView/OutcropQualityLegendItem.cpp \
           columnView/PatternLegendItem.cpp \
           columnView/SedimentStructureLegendItem.cpp \
           columnView/SymbolLegendItem.cpp 

CORRELATION_VIEW_SRC = \
           correlationView/BedCorrelationView.cpp 

DATA_MANAGER_SRC = \
           dataManager/DataManager.cpp \
           dataManager/ProjectManager.cpp 

DATA_MODEL_SRC = \
           dataModel/Bed.cpp \
           dataModel/BedCorrelation.cpp \
           dataModel/BeddingType.cpp \
           dataModel/BoundaryType.cpp \
           dataModel/CarbonateGrainSize.cpp \
           dataModel/ClasticGrainSize.cpp \
           dataModel/Color.cpp \
           dataModel/CustomSymbol.cpp \
           dataModel/Dataset.cpp \
           dataModel/DatasetWithFileName.cpp \
           dataModel/Facies.cpp \
           dataModel/Fossil.cpp \
           dataModel/GrainSize.cpp \
           dataModel/LengthMeasurement.cpp \
           dataModel/LengthUnit.cpp \
           dataModel/LithologicalUnit.cpp \
           dataModel/LithologicalUnitType.cpp \
           dataModel/Lithology.cpp \
           dataModel/OutcropQuality.cpp \
           dataModel/PrimitiveDataset.cpp \
           dataModel/Profile.cpp \
           dataModel/ProfileCorrelation.cpp \
           dataModel/ProfileInCorrelation.cpp \
           dataModel/Project.cpp \
           dataModel/Sample.cpp \
           dataModel/SedimentStructure.cpp

DB_MODEL_SRC = \
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
           dbModel/UniqueConstraint.cpp 

DIALOGS_SRC = \
           dialogs/DatabaseConnectionDialog.cpp \
           dialogs/BedCorrelationEditorDialog.cpp \
           dialogs/BeddingTypeEditorDialog.cpp \
           dialogs/BedEditorDialog.cpp \
           dialogs/BoundaryTypeEditorDialog.cpp \
           dialogs/ColorEditorDialog.cpp \
           dialogs/CsvProfileImportSettingsDialog.cpp \
           dialogs/CustomSymbolEditorDialog.cpp \
           dialogs/DatabaseErrorDialog.cpp \
           dialogs/DatasetEditorDialog.cpp \
           dialogs/DatasetWithFileNameEditorDialog.cpp \
           dialogs/FaciesEditorDialog.cpp \
           dialogs/FossilEditorDialog.cpp \
           dialogs/ImageEditorDialog.cpp \
           dialogs/ListSelectorDialog.cpp \
           dialogs/LithologicalUnitEditorDialog.cpp \
           dialogs/LithologicalUnitTypeEditorDialog.cpp \
           dialogs/LithologyEditorDialog.cpp \
           dialogs/OutcropQualityEditorDialog.cpp \
           dialogs/ProfileCorrelationEditorDialog.cpp \
           dialogs/ProfileEditorDialog.cpp \
           dialogs/ProfileSelectorDialog.cpp \
           dialogs/SampleEditorDialog.cpp \
           dialogs/SedimentStructureEditorDialog.cpp \
           dialogs/SettingsDialog.cpp \
           dialogs/ProjectEditorDialog.cpp 

FILE_INTERFACES_SRC = \
           fileInterfaces/CsvInterface.cpp \
           fileInterfaces/CsvProfileImportSettings.cpp \
           fileInterfaces/ProfileImportSettings.cpp \
           fileInterfaces/XMLInterface.cpp 

ITEMS_SRC = \
           items/BedCorrelationItem.cpp \
           items/BeddingTypeItem.cpp \
           items/BedItem.cpp \
           items/BoundaryTypeItem.cpp \
           items/CarbonateGrainSizeItem.cpp \
           items/ClasticGrainSizeItem.cpp \
           items/ColorItem.cpp \
           items/CustomSymbolItem.cpp \
           items/FaciesItem.cpp \
           items/FossilItem.cpp \
           items/GrainSizeItem.cpp \
           items/ImageItem.cpp \
           items/LithologicalUnitItem.cpp \
           items/LithologicalUnitTypeItem.cpp \
           items/LithologyItem.cpp \
           items/OutcropQualityItem.cpp \
           items/ProfileCorrelationItem.cpp \
           items/ProfileItem.cpp \
           items/SampleItem.cpp \
           items/SedimentStructureItem.cpp \
           items/StandardItem.cpp \
           items/ProjectItem.cpp 

MODELS_SRC = \
           models/ProjectItemModel.cpp \
           models/BedCorrelationItemModel.cpp \
           models/BeddingTypeItemModel.cpp \
           models/BedItemModel.cpp \
           models/BoundaryTypeItemModel.cpp \
           models/CarbonateGrainSizeItemModel.cpp \
           models/ClasticGrainSizeItemModel.cpp \
           models/ColorItemModel.cpp \
           models/CustomSymbolInBedItemModel.cpp \
           models/CustomSymbolItemModel.cpp \
           models/FaciesItemModel.cpp \
           models/FossilInBedItemModel.cpp \
           models/FossilItemModel.cpp \
           models/GrainSizeItemModel.cpp \
           models/ImageItemModel.cpp \
           models/LithologicalUnitItemModel.cpp \
           models/LithologicalUnitTypeItemModel.cpp \
           models/LithologyItemModel.cpp \
           models/OutcropQualityItemModel.cpp \
           models/ProfileCorrelationItemModel.cpp \
           models/ProfileItemModel.cpp \
           models/SampleItemModel.cpp \
           models/SedimentStructureInBedItemModel.cpp \
           models/SedimentStructureItemModel.cpp \
           models/StandardItemModel.cpp 

NON_GUI_SRC = \
           nonGui/AppDatabase.cpp \
           nonGui/Image.cpp \
           nonGui/ProfileLogger.cpp \
           nonGui/ProfileLoggerDatabase.cpp \
           nonGui/Settings.cpp \
           nonGui/SymbolFactory.cpp 

PG_INTERFACE_SRC = \
           pgInterface/AbstractDatabaseError.cpp \
           pgInterface/DatabaseError.cpp \
           pgInterface/Postgres.cpp \
           pgInterface/DatabaseConnectionSettings.cpp 

SQL_FACTORY_SRC = \
           sqlFactory/SqlFactory.cpp 

VIEW_SRC = \
           views/BedCorrelationItemView.cpp \
           views/BeddingTypeView.cpp \
           views/BedItemView.cpp \
           views/BoundaryTypeView.cpp \
           views/CarbonateGrainSizeView.cpp \
           views/ClasticGrainSizeView.cpp \
           views/ColorView.cpp \
           views/CustomSymbolInBedView.cpp \
           views/CustomSymbolView.cpp \
           views/FaciesView.cpp \
           views/FossilInBedView.cpp \
           views/FossilView.cpp \
           views/GrainSizeView.cpp \
           views/ImageItemView.cpp \
           views/LithologicalUnitTypeView.cpp \
           views/LithologicalUnitView.cpp \
           views/LithologyView.cpp \
           views/OutcropQualityView.cpp \
           views/ProfileCorrelationItemView.cpp \
           views/ProfileItemView.cpp \
           views/SampleItemView.cpp \
           views/SedimentStructureInBedView.cpp \
           views/SedimentStructureView.cpp \
           views/TreeView.cpp \
           views/ProjectView.cpp 

WIDGETS_SRC = \
           widgets/BedPropertyPage.cpp \
           widgets/DescriptionEdit.cpp \
           widgets/FileNameBrowserWidget.cpp \
           widgets/GrainSizeModeSelectorWidget.cpp \
           widgets/GrainSizeSelectorWidget.cpp \
           widgets/HostEdit.cpp \
           widgets/IdLabel.cpp \
           widgets/ImageFileNameBrowserWidget.cpp \
           widgets/LengthMeasurementWidget.cpp \
           widgets/LengthUnitsComboBox.cpp \
           widgets/LoginEdit.cpp \
           widgets/MainWindow.cpp \
           widgets/ManagementToolBox.cpp \
           widgets/NameEdit.cpp \
           widgets/PasswordEdit.cpp \
           widgets/ProfileCorrelationWidget.cpp \
           widgets/ProfileWorkWidget.cpp \
           widgets/QtPatternSelectorWidget.cpp \
           widgets/WorkWidget.cpp \
           widgets/DbWorkWidget.cpp

SOURCES += main.cpp \
           $$COLUMN_VIEW_SRC \
              $$DATA_MANAGER_SRC \
              $$DATA_MODEL_SRC \
              $$DB_MODEL_SRC \
              $$DIALOGS_SRC \
              $$FILE_INTERFACES_SRC \
              $$ITEMS_SRC \
              $$MODELS_SRC \
              $$NON_GUI_SRC \
              $$PG_INTERFACE_SRC \
              $$SQL_FACTORY_SRC \
              $$VIEW_SRC \
              $$WIDGETS_SRC \
              $$CORRELATION_VIEW_SRC 

TRANSLATIONS += i18n/profilelogger_de.ts i18n/profilelogger_en.ts
