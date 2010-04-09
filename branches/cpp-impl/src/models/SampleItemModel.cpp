/*
 * File:   SampleItemModel.cpp
 * Author: jolo
 *
 * Created on 11. Dezember 2009, 11:39
 */

#include "SampleItemModel.h"

#include <QMap>
#include <QFileDialog>
#include <QMessageBox>
#include <QFile>
#include <QTextStream>
#include <QDir>
#include <QFileInfo>

#include "MainWindow.h"
#include "StandardItemModel.h"
#include "ProfileLogger.h"
#include "Profile.h"
#include "Project.h"
#include "SampleItem.h"
#include "SampleEditorDialog.h"
#include "Sample.h"
#include "WorkWidget.h"

SampleItemModel::SampleItemModel(QObject* p)
: StandardItemModel(p),
_profile(0) {
    setSortRole(Qt::UserRole);
}

SampleItemModel::~SampleItemModel() {
}

void SampleItemModel::slotCurrentProfileChanged(Profile* p) {
    _profile = p;

    reload();
}

void SampleItemModel::reload() {
    clear();

    QStringList hh;
    hh << tr("Samples");
    setHorizontalHeaderLabels(hh);

    if (!_profile) {
        return;
    }

    for (QList<Sample*>::iterator it = _profile->getFirstSample();
            it != _profile->getLastSample();
            it++) {
        appendItem(*it);
    }

    emit reloaded();
}

SampleItem* SampleItemModel::appendItem(Sample* b) {
    SampleItem* itm = new SampleItem(b);
    appendRow(itm);
    return itm;
}

void SampleItemModel::slotCreate() {
    Sample* sample = _profile->createSample();

    SampleEditorDialog* dlg = new SampleEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(),
            sample);
    dlg->exec();

    reload();

    emit selectRequest(indexFromItem(findItemForSample(sample)));
}

void SampleItemModel::slotEdit(const QModelIndex& idx) {
    if (!idx.isValid()) {
        return;
    }

    SampleItem* itm = (SampleItem*) itemFromIndex(idx);
    Sample* sample = itm->getSample();

    SampleEditorDialog* dlg = new SampleEditorDialog((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(),
            sample);
    dlg->exec();

    reload();

    emit selectRequest(indexFromItem(findItemForSample(sample)));
}

SampleItem* SampleItemModel::findItemForSample(Sample* b) {
    if (!b) {
        return 0;
    }

    int max = rowCount();
    for (int r = 0; r < max; r++) {
        SampleItem* itm = (SampleItem*) item(r);
        if (itm->getSample()->getId() == b->getId()) {
            return itm;
        }
    }
    return 0;
}

void SampleItemModel::slotDelete(QModelIndexList lst) {
    for (QModelIndexList::iterator it = lst.begin(); it != lst.end(); it++) {
        SampleItem* itm = (SampleItem*) itemFromIndex(*it);
        _profile->deleteSample(itm->getSample());
    }
    reload();
}

void SampleItemModel::slotExportToLatex() {
    QFileInfo fi(QDir::currentPath(),
            tr("Samples_Profile_%1.tex").arg(_profile->getName()));

    QString fn = QFileDialog::getSaveFileName((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(),
            fi.absolutePath(),
            tr("LaTeX files (*.tex)"),
            fi.fileName());

    if (fn.isEmpty()) {
        return;
    }

    QStringList buf;
    buf << "%\\documentclass[a4paper]{scrartcl}"
            << "%\\usepackage{booktabs}"
            << "%\\begin{document}"
            << "\\begin{table}"
            << "\\centering"
            << "\\begin{tabular}{lll}"
            << "\\toprule"
            << QString("%1 & %2 & %3 \\\\")
            .arg(QObject::tr("Id"))
            .arg(QObject::tr("Name"))
            .arg(QObject::tr("Description"));

    for (QList<Sample*>::iterator it = _profile->getFirstSample();
            it != _profile->getLastSample();
            it++) {
        Sample* s = *it;
        buf << "\\midrule"
                << QString("%1 & %2 & %3\\\\")
                .arg(s->getId())
                .arg(s->getName())
                .arg(s->getDescription());
    }


    buf << "\\bottomrule"
            << "\\end{tabular}"
            << QString("\\caption{%1}").arg(tr("Samples in Profile \\emph{%1}.").arg(_profile->getName()))
            << "\\end{table}"
            << "%\\end{document}";

    QFile f(fn);

    if (!f.open(QFile::WriteOnly | QFile::Truncate)) {
        QMessageBox::critical((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(),
                tr("Could not write to file"),
                tr("Could not write to file '%1'.\nError: %2").arg(fn).arg(f.errorString()));
    }

    QTextStream strm(&f);

    strm << buf.join("\n");

    f.close();

    QMessageBox::information((static_cast<ProfileLogger*>(QApplication::instance()))->getMainWindow(),
            tr("Export completed"),
            tr("Export to file '%1' completed").arg(fn));
}
