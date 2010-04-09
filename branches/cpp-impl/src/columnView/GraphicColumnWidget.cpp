/* 
 * File:   GraphicColumnWidget.cpp
 * Author: jolo
 * 
 * Created on 16. Dezember 2009, 13:41
 */

#include "GraphicColumnWidget.h"

#include <QGraphicsScene>
#include <QGraphicsRectItem>
#include <QGraphicsGridLayout>
#include <QMenu>
#include <QAction>
#include <QPrinter>
#include <QFileDialog>
#include <QMessageBox>
#include <QSvgGenerator>
#include <QImageWriter>
#include <QPrintDialog>

#include "Profile.h"
#include "Bed.h"

#include "GraphicColumnHeader.h"
#include "GraphicColumnBody.h"
#include "GraphicBedItem.h"
#include "WorkWidget.h"
#include "Settings.h"
#include "GraphicLegendItem.h"

GraphicColumnWidget::GraphicColumnWidget(QWidget* p)
: QGraphicsView(p),
_profile(0),
_scene(0),
_header(0),
_body(0),
_legend(0),
_scale(5.0),
_scaleStep(0.02) {
    setEnabled(_profile);
    
    _scene = new QGraphicsScene(this);
    setScene(_scene);
}

GraphicColumnWidget::~GraphicColumnWidget() {
}

void GraphicColumnWidget::slotCurrentProfileChanged(Profile* p) {
    _profile = p;
    setEnabled(_profile);

    _scene->clear();
    reload();
}

void GraphicColumnWidget::slotCurrentBedChanged(Bed* b) {
    if (!b) {
        return;
    }

    reload();
    selectBed(b);
}

void GraphicColumnWidget::reload() {
    _scene->clear();

    _header = new GraphicColumnHeader();
    _body = new GraphicColumnBody();
    _legend = new GraphicLegendItem();

    _header->setProfile(_profile);
    _legend->setProfileAndHeader(_profile, _header);
    _body->setProfileAndHeader(_profile, _header);

    _scene->addItem(_legend);
    _scene->addItem(_header);
    _scene->addItem(_body);
}

void GraphicColumnWidget::slotExportToSvg(Profile* p) {
    if (!p) {
        return;
    }

    slotCurrentProfileChanged(p);

}

void GraphicColumnWidget::selectBed(Bed* b) {
    if (!_body) {
        return;
    }

    _body->selectBed(b);
}

void GraphicColumnWidget::keyPressEvent(QKeyEvent* e) {
    if (!e) {
        return;
    }

    if (e->matches(QKeySequence::ZoomIn)) {
        QMatrix m = matrix();
        qreal s = 1.0 + (static_cast<ProfileLogger*> (QApplication::instance()))->getSettings()->getGraphicsViewScaleStep();
        m.scale(s, s);
        setMatrix(m);
        e->accept();
        return;
    }

    if (e->matches(QKeySequence::ZoomOut)) {
        QMatrix m = matrix();
        qreal s = 1.0 - (static_cast<ProfileLogger*> (QApplication::instance()))->getSettings()->getGraphicsViewScaleStep();
        m.scale(s, s);
        setMatrix(m);
        e->accept();
        return;
    }

    e->ignore();
}

void GraphicColumnWidget::slotPrint() {
    QPrinter printer;

    QPrintDialog dlg(&printer, this);

    dlg.exec();
}

void GraphicColumnWidget::slotExportToSvg() {
    QString fn = QFileDialog::getSaveFileName(this,
            tr("Export Profile To SVG..."),
            QDir::currentPath(),
            tr("SVG Files (*.svg)"));
    if (fn.isEmpty()) {
        return;
    }

    QSvgGenerator gen;
    gen.setFileName(fn);
    gen.setSize(QSize((int)(_scene->width()), (int)(_scene->height())));

    QPainter painter(&gen);

    _scene->render(&painter);

    painter.end();

    QMessageBox::information(this, tr("Export Completed"),
            tr("Profile exported to <b>%1</b>.").arg(fn));
}

void GraphicColumnWidget::slotExportToPdf() {
    QString fn = QFileDialog::getSaveFileName(this,
            tr("Export Profile To PDF..."),
            QDir::currentPath(),
            tr("PDF Files (*.pdf)"));
    if (fn.isEmpty()) {
        return;
    }

    QPrinter printer;
    //printer.setPaperSize(QPrinter::A0);
    printer.setOutputFormat(QPrinter::PdfFormat);
    printer.setOutputFileName(fn);
    QPainter painter(&printer);
    _scene->render(&painter);
    painter.end();

    QMessageBox::information(this, tr("Export Completed"),
            tr("Profile exported to <b>%1</b>.").arg(fn));
}

void GraphicColumnWidget::slotExportToJpg() {
    QString fn = QFileDialog::getSaveFileName(this,
            tr("Export Profile To JPG..."),
            QDir::currentPath(),
            tr("JPG Files (*.jpg *.JPG)"));
    if (fn.isEmpty()) {
        return;
    }

    QImageWriter w;
    w.setFileName(fn);
    w.setFormat("JPG");
    w.setQuality(100);

    QImage img(QSize((int)(_scene->width()), (int)(_scene->height())), QImage::Format_RGB32);
    QPainter painter(&img);
    painter.setRenderHint(QPainter::Antialiasing);
    _scene->render(&painter);
    painter.end();

    if (w.write(img)) {
        QMessageBox::information(this, tr("Export Completed"),
                tr("Profile exported to <b>%1</b>.").arg(fn));
    } else {
        QMessageBox::critical(this, tr("Export Failed"),
                tr("Could not export Profile: %1").arg(w.errorString()));
    }
}

void GraphicColumnWidget::slotExportToPng() {
    QString fn = QFileDialog::getSaveFileName(this,
            tr("Export Profile To PNG..."),
            QDir::currentPath(),
            tr("PNG Files (*.png *.PNG)"));
    if (fn.isEmpty()) {
        return;
    }

    QImageWriter w;
    w.setFileName(fn);
    w.setFormat("png");

    QImage img(QSize((int)(_scene->width()), (int)(_scene->height())), QImage::Format_RGB32);
    QPainter painter(&img);
    painter.setRenderHint(QPainter::Antialiasing);
    _scene->render(&painter);
    painter.end();

    if (w.write(img)) {
        QMessageBox::information(this, tr("Export Completed"),
                tr("Profile exported to <b>%1</b>.").arg(fn));
    } else {
        QMessageBox::critical(this, tr("Export Failed"),
                tr("Could not export Profile: %1").arg(w.errorString()));
    }
}

void GraphicColumnWidget::slotExportToTiff() {
    QString fn = QFileDialog::getSaveFileName(this,
            tr("Export Profile To Tiff..."),
            QDir::currentPath(),
            tr("TIFF Files (*.tif *.tiff *.Tif *.TIF *.TIFF *.Tiff)"));
    if (fn.isEmpty()) {
        return;
    }

    QImageWriter w;
    w.setFileName(fn);
    w.setFormat("TIFF");

    QImage img(QSize((int)(_scene->width()), (int)(_scene->height())), QImage::Format_RGB32);
    QPainter painter(&img);
    painter.setRenderHint(QPainter::Antialiasing);
    _scene->render(&painter);
    painter.end();

    if (w.write(img)) {
        QMessageBox::information(this, tr("Export Completed"),
                tr("Profile exported to <b>%1</b>.").arg(fn));
    } else {
        QMessageBox::critical(this, tr("Export Failed"),
                tr("Could not export Profile: %1").arg(w.errorString()));
    }
}
