/* 
 * File:   SettingsDialog.h
 * Author: jolo
 *
 * Created on 15. Dezember 2009, 10:22
 */

#ifndef _SETTINGSDIALOG_H
#define	_SETTINGSDIALOG_H

#include <QDialog>

class QPushButton;
class QLineEdit;
class QDialogButtonBox;
class QSpinBox;

class Settings;

class SettingsDialog: public QDialog {
    Q_OBJECT
public:
    SettingsDialog(QWidget* p);
    virtual ~SettingsDialog();

public slots:
    void slotBrowseLithologiesPatternPath();
    void slotBrowseBeddingTypesPatternPath();
    void slotBrowseFossilsPath();
    void slotBrowseSedimentStructuresPath();
    void slotBrowseCustomSymbolsPath();
    void slotBrowseBoundaryTypesPath();
    void slotBrowseFaciesPath();
    void slotBrowseOutcropQualitiesPath();
    void slotBrowseImagePath();
    void slotGraphicsViewScaleStepChanged(int i);
    void slotBrowseLanguageFile();

private:

    QLineEdit* _lithologiesPatternPathW;
    QPushButton* _browseLithologiesPatternPathW;
    
    QLineEdit* _beddingTypesPatternPathW;
    QPushButton* _browseBeddingTypesPatternPathW;

    QLineEdit* _fossilsPathW;
    QPushButton* _browseFossilsPathW;

    QLineEdit* _sedimentStructuresPathW;
    QPushButton* _browseSedimentStructuresPathW;

    QLineEdit* _customSymbolsPathW;
    QPushButton* _browseCustomSymbolsPathW;

    QLineEdit* _boundaryTypesPathW;
    QPushButton* _browseBoundaryTypesPathW;

    QLineEdit* _faciesPathW;
    QPushButton* _browseFaciesPathW;

    QLineEdit* _imagePathW;
    QPushButton* _browseImagePathW;

    QLineEdit* _outcropQualitiesPathW;
    QPushButton* _browseOutcropQualitiesPathW;

    QLineEdit* _languageFileW;
    QPushButton* _browseLanguageFileW;
    
    QSpinBox* _graphicsViewScaleStepW;

    QDialogButtonBox* _bbW;

    Settings* _settings;
};

#endif	/* _SETTINGSDIALOG_H */

