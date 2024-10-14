# coding: utf-8

# MODULES
import numpy as np
from PyQt5.QtWidgets import QLineEdit
from PyQt5 import QtCore, QtGui


# STATICS
def is_float(some_string):
    try:
        float(some_string)
    except ValueError:
        return False
    else:
        return True


class QLineEditNumber(QLineEdit):
    def __init__(self, parent=None):
        super(QLineEditNumber, self).__init__(parent)
        self.inFocus = False
        self.installEventFilter(self)

    def value(self):
        if is_float(self.text().replace(",", ".")):
            return float(self.text().replace(",", "."))
        else:
            print(f"QLineEditNumber: Cannot convert '{self.text()}' to float")
            return np.NAN

    def setValue(self, some_flot):
        if is_float(some_flot):
            self.setText(str(some_flot))
        else:
            print(f"QLineEditNumber: '{some_flot}' not a float")

    def eventFilter(self, source, event):
        if source is self:
            if event.type() == QtCore.QEvent.FocusIn:
                self.inFocus = True
            if event.type() == QtCore.QEvent.FocusOut:
                self.inFocus = False
            elif self.inFocus and event.type() == QtCore.QEvent.Wheel:
                if self.cursorPosition() > 0 and self.text()[self.cursorPosition() - 1] not in [",", "."]:
                    current_cursor_position = self.cursorPosition()
                    if "." in self.text():
                        point_position = self.text().find(".")
                    else:
                        point_position = self.text().find(",")
                    if point_position == -1:
                        current_point_position = len(self.text())
                        self.setText(f"{self.value() + (-1 if event.angleDelta().y() < 0 else 1) * 10 ** (len(self.text()) - self.cursorPosition()):.{0}f}")
                        self.setCursorPosition(current_cursor_position + (len(self.text()) - current_point_position))
                    elif self.cursorPosition() <= point_position:
                        current_point_position = point_position
                        self.setText(f"{self.value() + (-1 if event.angleDelta().y() < 0 else 1) * 10 ** (point_position - self.cursorPosition()):.{len(self.text()) - point_position - 1}f}")
                        if "." in self.text():
                            point_position = self.text().find(".")
                        else:
                            point_position = self.text().find(",")
                        self.setCursorPosition(current_cursor_position + (point_position - current_point_position))
                    else:
                        current_point_position = len(self.text())
                        self.setText(f"{self.value() + (-1 if event.angleDelta().y() < 0 else 1) / 10 ** (self.cursorPosition() - point_position - 1):.{len(self.text()) - point_position - 1}f}")
                        self.setCursorPosition(current_cursor_position + (len(self.text()) - current_point_position))
        return QtGui.QWidget.eventFilter(self, source, event)
