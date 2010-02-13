#include "PrimitiveDataset.h"

PrimitiveDataset::PrimitiveDataset(int id)
  :_id(id) {
}

PrimitiveDataset::~PrimitiveDataset() {}

QString PrimitiveDataset::makeToolTipText(const bool withDatasetName) const {
    QStringList ret;
    if (withDatasetName) {
        ret << tr("Dataset:");
    }

    ret << tr("ID: %1").arg(getId());

    return ret.join("\n");
}

QString PrimitiveDataset::toString(const bool withDatasetName) const {
    return makeToolTipText(withDatasetName);
}
