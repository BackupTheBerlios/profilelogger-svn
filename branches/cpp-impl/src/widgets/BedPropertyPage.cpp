/* 
 * File:   BedPropertyPage.cpp
 * Author: jolo
 * 
 * Created on 14. Dezember 2009, 19:19
 */

#include "BedPropertyPage.h"

#include <QLayout>
#include <QLabel>

BedPropertyPage::BedPropertyPage(QWidget* p)
: QWidget(p) {
    setLayout(new QGridLayout(this));
}

BedPropertyPage::~BedPropertyPage() {
}

void BedPropertyPage::addWidgets(const QString& leftCaption,
        const QString& rightCaption,
        QWidget* leftW,
        QWidget* rightW) {
    QLabel* leftL = new QLabel(leftCaption, this);
    QLabel* rightL = new QLabel(rightCaption, this);

    QGridLayout* l = (QGridLayout*)layout();
    l->addWidget(leftL, 0, 0);
    l->addWidget(rightL, 0, 1);
    l->addWidget(leftW, 1, 0);
    l->addWidget(rightW, 1, 1);
}

void BedPropertyPage::addWidgets(const QString& leftCaption,
        const QString& rightCaption,
        QWidget* leftW,
        QWidget* rightW,
        QWidget* buttonsP) {
    QLabel* leftL = new QLabel(leftCaption, this);
    QLabel* rightL = new QLabel(rightCaption, this);

    QGridLayout* l = (QGridLayout*)layout();
    l->addWidget(leftL, 0, 0);
    l->addWidget(rightL, 0, 2);
    l->addWidget(buttonsP, 1, 1);
    l->addWidget(leftW, 1, 0);
    l->addWidget(rightW, 1, 2);
}

void BedPropertyPage::addWidgets(const QString& caption, QWidget* widget) {
    QLabel* cL = new QLabel(caption, this);

    QGridLayout* l = (QGridLayout*)layout();
    l->addWidget(cL, 0, 0);
    l->addWidget(widget, 1, 0);
}
