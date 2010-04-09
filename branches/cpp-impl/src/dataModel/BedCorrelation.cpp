#include "BedCorrelation.h"

#include <QStringList>

#include "Bed.h"
#include "Profile.h"

BedCorrelation::BedCorrelation(int id,
			       Bed* left,
			       Bed* right)
  : Dataset(id),
    _left(left),
    _right(right) {
  updateName();
}

BedCorrelation::~BedCorrelation() {}

void BedCorrelation::setLeftBed(Bed* b) {
  _left = b;
  updateName();
}

void BedCorrelation::setRightBed(Bed* b) {
  _right = b;
  updateName();
}

void BedCorrelation::updateName() {
  QStringList buf;

  if (!_left) {
    buf << tr("Left Bed Not Set");
  } else {
    buf << tr("Profile '%1' Bed '%2'").arg(_left->getProfile()->getName()).arg(_left->getName());
  }

  if (!_right) {
    buf << tr("Right Bed Not Set");
  } else {
    buf << tr("Profile '%1' Bed '%2'").arg(_right->getProfile()->getName()).arg(_right->getName());
  }

  setName(buf.join(" - "));
}
