/* 
 * File:   DatasetEditorDialog.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 21:22
 */

#ifndef _DATASETEDITORDIALOG_H
#define	_DATASETEDITORDIALOG_H

#include <QDialog>

#include "IdLabel.h"

class QDialogButtonBox;
class IdLabel;
class NameEdit;
class DescriptionEdit;
class QGroupBox;
class QTabWidget;

class Dataset;

class DatasetEditorDialog : public QDialog {
    Q_OBJECT
public:
    DatasetEditorDialog(QWidget* p = 0, Dataset* d = 0);
    virtual ~DatasetEditorDialog();

signals:
    void showDatasetRequest(Dataset* d);
    void validationRequest();

public slots:
    virtual void reject();
    virtual void close();

protected slots:
    virtual void slotNameChanged(const QString& s);
    virtual void slotDescriptionChanged(const QString& s);
    virtual void slotShowDataset(Dataset* d);
    virtual void clear();

protected:

    bool hasIdWidget() const {
        return 0 != _idW;
    }

    bool hasNameWidget() const {
        return 0 != _nameW;
    }

    bool hasDescriptionWidget() const {
        return 0 != _descriptionW;
    }

    Dataset* getDataset() {
        return _data;
    }

    NameEdit* getNameEdit() {
        return _nameW;
    }

    DescriptionEdit* getDescriptionEdit() {
        return _descriptionW;
    }

    IdLabel* getIdLabel() {
        return _idW;
    }

    QTabWidget* getTabWidget() {
        return _tabW;
    }

    QWidget* addMainPage(const QString& title);
    NameEdit* addNameEdit();
    DescriptionEdit* addDescriptionEdit();
    IdLabel* addIdLabel();
    QDialogButtonBox* addButtons();

    QWidget* getMainPage() const {
        return _mainPageW;
    }

    int r;
    int lC;
    int wC;

private:
    Dataset* _data;

    QTabWidget* _tabW;
    IdLabel* _idW;
    QWidget* _mainPageW;
    NameEdit* _nameW;
    DescriptionEdit* _descriptionW;
    QDialogButtonBox* _bbW;
};

#endif	/* _DATASETEDITORDIALOG_H */

