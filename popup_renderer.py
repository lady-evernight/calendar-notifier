from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
import sys

app = QApplication(sys.argv)
window=QWidget()
window.setFixedSize(360, 220)
window.setStyleSheet("background-color: #fce4ec;")
window.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

label=QLabel("Test", window)
label.move(50, 100)

background=QLabel(window)
pixmap=QPixmap("assets/bg.png")
background.setPixmap(pixmap)
background.setScaledContents(True)
background.setFixedSize(360, 220)

screen=app.primaryScreen().geometry()
x=(screen.width() - window.width()) // 2
y=90

window.move(x, y)
window.show()
sys.exit(app.exec())