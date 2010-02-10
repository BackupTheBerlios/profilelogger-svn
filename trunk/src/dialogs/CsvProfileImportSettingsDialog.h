/* 
 * File:   CsvProfileImportSettingsDialog.h
 * Author: jolo
 *
 * Created on 27. Januar 2010, 21:11
 */

#ifndef _CSVPROFILEIMPORTSETTINGSDIALOG_H
#define	_CSVPROFILEIMPORTSETTINGSDIALOG_H

#include <QDialog>

#include "CsvProfileImportSettings.h"

class QWidget;
class QDialogButtonBox;
class QLineEdit;
class QGridLayout;
class QVBoxLayout;
class QPushButton;
class QLabel;
class QCheckBox;
class CsvProfileImportSettings;

class CsvProfileImportSettingsDialog: public QDialog {
    Q_OBJECT
public:
    CsvProfileImportSettingsDialog(QWidget* p, CsvProfileImportSettings* s);
    virtual ~CsvProfileImportSettingsDialog();

public slots:
    virtual void slotBrowseFile();
    virtual void slotIgnoreFirstLineToggled(bool b);
    virtual void slotFieldSeparatorChanged(const QString& s);
    virtual void slotQuoteCharChanged(const QString& s);
    virtual void slotAccept();
    virtual void slotReject();
    
private:
    void setupContentWidget();
    void showData();
    
    CsvProfileImportSettings* _settings;
    
    QLineEdit* _fileNameW;
    QPushButton* _browseFileNameW;
    QCheckBox* _ignoreFirstLineW;
    QLineEdit* _fieldSepW;
    QLineEdit* _quoteCharW;
    QDialogButtonBox* _bbW;
};

#endif	/* _CSVPROFILEIMPORTSETTINGSDIALOG_H */

