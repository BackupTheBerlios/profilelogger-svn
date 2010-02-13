/* 
 * File:   BedPropertyPage.h
 * Author: jolo
 *
 * Created on 14. Dezember 2009, 19:19
 */

#ifndef _BEDPROPERTYPAGE_H
#define	_BEDPROPERTYPAGE_H

#include <QWidget>

class BedPropertyPage : public QWidget {
    Q_OBJECT
public:
    BedPropertyPage(QWidget* p = 0);
    virtual ~BedPropertyPage();

    void addWidgets(const QString& leftCaption,
            const QString& rightCaption,
            QWidget* leftW,
            QWidget* rightW);
    void addWidgets(const QString& leftCaption,
            const QString& rightCaption,
            QWidget* leftW,
            QWidget* rightW,
            QWidget* buttonPanel);
    void addWidgets(const QString& caption,
            QWidget* widget);
};

#endif	/* _BEDPROPERTYPAGE_H */

