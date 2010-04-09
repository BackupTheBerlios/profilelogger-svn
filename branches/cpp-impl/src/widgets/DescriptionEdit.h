/* 
 * File:   DescriptionEdit.h
 * Author: jolo
 *
 * Created on 10. Dezember 2009, 20:54
 */

#ifndef _DESCRIPTIONEDIT_H
#define	_DESCRIPTIONEDIT_H

#include <QTextEdit>

class QLabel;

class DescriptionEdit : public QTextEdit {
    Q_OBJECT
public:
    DescriptionEdit(QWidget* p = 0);

    virtual ~DescriptionEdit();
    QLabel* getLabel();

signals:
    void descriptionChanged(const QString& s);

public slots:
    void slotTextChanged();

private:
    QLabel* _lbl;
};

#endif	/* _DESCRIPTIONEDIT_H */

