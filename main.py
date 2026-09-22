from PySide6.QtWidgets import
import sys

class display_window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Display Application")
        self.resize()

        # project will showcase self made animation...

app = QApplication(sys.argv)

app.setStyleSheet(style_sheet)

window = MainWindow()
window.show()

sys.exit(app.exec())
