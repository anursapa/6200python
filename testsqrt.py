import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

window = QtGui.QWidget()
window.setGeometry(0, 0, 500, 300)
window.setWindowTitle("PyQT test!")

window.show()
sys.exit()
