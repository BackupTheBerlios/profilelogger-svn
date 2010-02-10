TEMPLATE = app

TARGET = profilelogger
DESTDIR = ../bin

QT += core gui svg xml sql

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
              dataModel \
              dialogs \
              interfaces \
              items \
              models \
              nonGui \
              views \
              widgets \
              correlationView \
              dbInterface \
              dbModel \
              sqlFactory
INCLUDEPATH += . \
               nonGui \
               items \
               views \
               dataModel \
               columnView \
               widgets \
               dialogs \
               models \
               fileInterfaces \
               correlationView \
               dbInterface \
               dbModel \
               sqlFactory

# Input
HEADERS += widgets/HostEdit.h \
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
           columnView/SymbolLegendItem.h \
           dataModel/ProfileInCorrelation.h \
           dataModel/ProfileCorrelation.h \
           dataModel/BedCorrelation.h \
           dataModel/Bed.h \
           dataModel/BeddingType.h \
           dataModel/BoundaryType.h \
           dataModel/CarbonateGrainSize.h \
           dataModel/ClasticGrainSize.h \
           dataModel/Color.h \
           dataModel/CustomSymbol.h \
           dataModel/PrimitiveDataset.h \
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
           dataModel/Profile.h \
           dataModel/Project.h \
           dataModel/Sample.h \
           dataModel/SedimentStructure.h \
           dialogs/ProfileCorrelationEditorDialog.h \
           dialogs/BeddingTypeEditorDialog.h \
           dialogs/BedEditorDialog.h \
           dialogs/BoundaryTypeEditorDialog.h \
           dialogs/ColorEditorDialog.h \
           dialogs/CsvProfileImportSettingsDialog.h \
           dialogs/CustomSymbolEditorDialog.h \
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
           dialogs/ProfileEditorDialog.h \
           dialogs/ProfileSelectorDialog.h \
           dialogs/SampleEditorDialog.h \
           dialogs/SedimentStructureEditorDialog.h \
           dialogs/SettingsDialog.h \
           fileInterfaces/CsvInterface.h \
           fileInterfaces/CsvProfileImportSettings.h \
           fileInterfaces/ProfileImportSettings.h \
           fileInterfaces/XMLInterface.h \
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
           items/ProfileItem.h \
           items/SampleItem.h \
           items/SedimentStructureItem.h \
           items/StandardItem.h \
           items/ProfileCorrelationItem.h \
           models/ProfileCorrelationItemModel.h \
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
           models/ProfileItemModel.h \
           models/SampleItemModel.h \
           models/SedimentStructureInBedItemModel.h \
           models/SedimentStructureItemModel.h \
           models/StandardItemModel.h \
           nonGui/Image.h \
           nonGui/ProfileLogger.h \
           nonGui/Settings.h \
           nonGui/SymbolFactory.h \
           nonGui/Version.h \
           views/ProfileCorrelationItemView.h \
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
           views/ProfileItemView.h \
           views/SampleItemView.h \
           views/SedimentStructureInBedView.h \
           views/SedimentStructureView.h \
           views/TreeView.h \
           widgets/ProfileCorrelationWidget.h \
           widgets/BedPropertyPage.h \
           widgets/DescriptionEdit.h \
           widgets/FileNameBrowserWidget.h \
           widgets/GrainSizeModeSelectorWidget.h \
           widgets/GrainSizeSelectorWidget.h \
           widgets/IdLabel.h \
           widgets/ImageFileNameBrowserWidget.h \
           widgets/LengthMeasurementWidget.h \
           widgets/LengthUnitsComboBox.h \
           widgets/MainWindow.h \
           widgets/ManagementToolBox.h \
           widgets/NameEdit.h \
           widgets/ProfileWorkWidget.h \
           widgets/QtPatternSelectorWidget.h \
           widgets/WorkWidget.h \
           items/BedCorrelationItem.h \
           views/BedCorrelationItemView.h \
           models/BedCorrelationItemModel.h \
           dialogs/BedCorrelationEditorDialog.h \
           correlationView/BedCorrelationView.h \
           dbModel/DbInterfacepart.h \
           dbModel/Database.h \
           dbModel/Schema.h \
           dbModel/DbInterfacePartInSchema.h \
           dbModel/Sequence.h \
           dbModel/Table.h \
           dbModel/DbInterfacePartInTable.h \
           dbModel/TableColumn.h \
           dbModel/TableConstraint.h \
           dbModel/PrimaryKey.h \
           dbModel/UniqueConstraint.h \
           dbModel/CheckConstraint.h \
           dbModel/TextNotEmptyCheckConstraint.h \
           dbModel/ForeignKey.h \
           nonGui/ProfileLoggerDatabase.h \
           sqlFactory/SqlFactory.h \
           widgets/LoginEdit.h \
           widgets/PasswordEdit.h \
           widgets/DatabaseConnectionDialog.h \
           dbInterface/DatabaseConnectionSettings.h \
           dbInterface/DatabaseConnection.h \
           dbInterface/AbstractDatabaseError.h \
           dbInterface/QueryError.h \
           dbInterface/TransactionError.h \
           dialogs/DatabaseErrorDialog.h \
           dbInterface/ConnectionError.h

 SOURCES += main.cpp \
dbInterface/ConnectionError.cpp \
 widgets\LoginEdit.cpp \
 widgets\PasswordEdit.cpp \
 widgets\DatabaseConnectionDialog.cpp \
dbInterface\DatabaseConnectionSettings.cpp \
           widgets/HostEdit.cpp \
           items/BedCorrelationItem.cpp \
           views/BedCorrelationItemView.cpp \
           models/BedCorrelationItemModel.cpp \
           dialogs/BedCorrelationEditorDialog.cpp \
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
           columnView/SymbolLegendItem.cpp \
           dataModel/ProfileInCorrelation.cpp \
           dataModel/BedCorrelation.cpp \
           dataModel/ProfileCorrelation.cpp \
           dataModel/Bed.cpp \
           dataModel/BeddingType.cpp \
           dataModel/BoundaryType.cpp \
           dataModel/CarbonateGrainSize.cpp \
           dataModel/ClasticGrainSize.cpp \
           dataModel/Color.cpp \
           dataModel/CustomSymbol.cpp \
           dataModel/PrimitiveDataset.cpp \
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
           dataModel/Profile.cpp \
           dataModel/Project.cpp \
           dataModel/Sample.cpp \
           dataModel/SedimentStructure.cpp \
           dialogs/ProfileCorrelationEditorDialog.cpp \
           dialogs/BeddingTypeEditorDialog.cpp \
           dialogs/BedEditorDialog.cpp \
           dialogs/BoundaryTypeEditorDialog.cpp \
           dialogs/ColorEditorDialog.cpp \
           dialogs/CsvProfileImportSettingsDialog.cpp \
           dialogs/CustomSymbolEditorDialog.cpp \
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
           dialogs/ProfileEditorDialog.cpp \
           dialogs/ProfileSelectorDialog.cpp \
           dialogs/SampleEditorDialog.cpp \
           dialogs/SedimentStructureEditorDialog.cpp \
           dialogs/SettingsDialog.cpp \
           fileInterfaces/CsvInterface.cpp \
           fileInterfaces/CsvProfileImportSettings.cpp \
           fileInterfaces/ProfileImportSettings.cpp \
           fileInterfaces/XMLInterface.cpp \
           items/ProfileCorrelationItem.cpp \
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
           items/ProfileItem.cpp \
           items/SampleItem.cpp \
           items/SedimentStructureItem.cpp \
           items/StandardItem.cpp \
           models/ProfileCorrelationItemModel.cpp \
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
           models/ProfileItemModel.cpp \
           models/SampleItemModel.cpp \
           models/SedimentStructureInBedItemModel.cpp \
           models/SedimentStructureItemModel.cpp \
           models/StandardItemModel.cpp \
           nonGui/Image.cpp \
           nonGui/ProfileLogger.cpp \
           nonGui/Settings.cpp \
           nonGui/SymbolFactory.cpp \
           views/ProfileCorrelationItemView.cpp \
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
           views/ProfileItemView.cpp \
           views/SampleItemView.cpp \
           views/SedimentStructureInBedView.cpp \
           views/SedimentStructureView.cpp \
           views/TreeView.cpp \
           widgets/ProfileCorrelationWidget.cpp \
           widgets/BedPropertyPage.cpp \
           widgets/DescriptionEdit.cpp \
           widgets/FileNameBrowserWidget.cpp \
           widgets/GrainSizeModeSelectorWidget.cpp \
           widgets/GrainSizeSelectorWidget.cpp \
           widgets/IdLabel.cpp \
           widgets/ImageFileNameBrowserWidget.cpp \
           widgets/LengthMeasurementWidget.cpp \
           widgets/LengthUnitsComboBox.cpp \
           widgets/MainWindow.cpp \
           widgets/ManagementToolBox.cpp \
           widgets/NameEdit.cpp \
           widgets/ProfileWorkWidget.cpp \
           widgets/QtPatternSelectorWidget.cpp \
           widgets/WorkWidget.cpp \
           correlationView/BedCorrelationView.cpp \
           dbModel/DbInterfacePart.cpp \
           dbModel/Database.cpp \
           dbModel/Schema.cpp \
           dbModel/DbInterfacePartInSchema.cpp \
           dbModel/Sequence.cpp \
           dbModel/Table.cpp \
           dbModel/DbInterfacePartInTable.cpp \
           dbModel/TableColumn.cpp \
           dbModel/TableConstraint.cpp \
           dbModel/PrimaryKey.cpp \
           dbModel/UniqueConstraint.cpp \
           dbModel/CheckConstraint.cpp \
           dbModel/TextNotEmptyCheckConstraint.cpp \
           nonGui/ProfileLoggerDatabase.cpp \
           sqlFactory/SqlFactory.cpp \
           dbModel/ForeignKey.cpp \
           dbInterface/DatabaseConnection.cpp \
           dbInterface/AbstractDatabaseError.cpp \
           dbInterface/QueryError.cpp \
           dbInterface/TransactionError.cpp \
           dialogs/DatabaseErrorDialog.cpp
