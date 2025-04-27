import sys
import os
import PySide6
import numpy as np
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QLabel, QLayout, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QWidget

def calculate_determinant() -> int:
    matrix = np.random.rand(25, 25)
    det = np.linalg.det(matrix)
    return det


class SecondWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Numpy Window")

        layout = QVBoxLayout()
        label = QLabel(str(calculate_determinant()))
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.setMinimumSize(QSize(200, 100))
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Demo App")

        self.second_window = SecondWindow()  # Create an instance of the second window
        button = QPushButton("Press here")
        button.clicked.connect(self.open_second_window)

        layout_button = QHBoxLayout()
        layout_button.addWidget(button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(self.makeHLabels("Python interpret path:", sys.executable))
        main_layout.addLayout(self.makeHLabels("Python version:", sys.version))
        main_layout.addLayout(self.makeHLabels("PySide6 module path:", os.path.abspath(PySide6.__file__)))
        main_layout.addLayout(self.makeHLabels("Numpy module path:", os.path.abspath(np.__file__)))
        main_layout.addLayout(self.makeHLabels("Numpy version:", np.__version__))
        main_layout.addLayout(layout_button)

        main_layout.setSpacing(10)
        main_layout.setContentsMargins(10, 10, 10, 10)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)


    def makeHLabels(self, title: str, value: str) -> QLayout:
        layout = QHBoxLayout()

        title_label = QLabel(title)
        layout.addWidget(title_label)
        layout.setAlignment(title_label, Qt.AlignLeft)

        value_label = QLabel(value)
        value_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        layout.addWidget(value_label)
        layout.setAlignment(value_label, Qt.AlignRight)

        return layout

    def open_second_window(self) -> None:
        self.second_window.show()



def run() -> None:
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
