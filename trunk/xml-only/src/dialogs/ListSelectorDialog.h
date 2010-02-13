/* 
 * File:   ListSelectorDialog.h
 * Author: jolo
 *
 * Created on 23. Januar 2010, 08:41
 */

#ifndef _LISTSELECTORDIALOG_H
#define	_LISTSELECTORDIALOG_H

#include <QDialog>
#include <QLayout>
#include <QDialogButtonBox>

class TreeView;
class Dataset;

class ListSelectorDialog : public QDialog {
    Q_OBJECT
public:
    ListSelectorDialog(QWidget* p, const QString& title = QObject::tr("Select Dataset"));
    virtual ~ListSelectorDialog();

    Dataset* getSelectedDataset() {
        return _currentDataset;
    }

public slots:
    virtual void slotSelectionChanged(Dataset* d);

protected:
    void setView(TreeView* v);

    Dataset* _currentDataset;

private:
    QString _title;
    QDialogButtonBox* _bb;
};

#endif	/* _LISTSELECTORDIALOG_H */
