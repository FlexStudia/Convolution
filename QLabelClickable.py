# coding: utf-8

# PACKAGES
from PyQt5.QtWidgets import QLabel, QApplication
from PyQt5.QtCore import pyqtSignal, QTimer

class QLabelClickable(QLabel):
		clicked = pyqtSignal(str)
		def __init__(self, parent=None):
			super(QLabelClickable, self).__init__(parent)
		def mousePressEvent(self, event):
			self.ultimo = "Clic"
		def mouseReleaseEvent(self, event):
			QTimer.singleShot(QApplication.instance().doubleClickInterval()/6,
							  self.performSingleClickAction)
		def performSingleClickAction(self):
			if self.ultimo == "Clic":
				self.clicked.emit(self.ultimo)
