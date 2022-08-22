import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtWidgets import QPushButton, QWidget, QGridLayout

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Python Menus & Toolbars")
        self.resize(400, 200)
        self.centralWidget = QLabel("Hello, World")
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.centralWidget)
    


def main():
    # Create an instance of QApplication
    gui = QApplication(sys.argv)
    # Show GUI
    view = Window()
    view.show()
    # Execute main loop
    sys.exit(gui.exec_())

if __name__ == '__main__':
    main()