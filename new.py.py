from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton)
from PyQt6.QtCore import Qt


app = QApplication([])
window = QWidget()


main_line = QVBoxLayout()

H1 = QHBoxLayout()
H2 = QHBoxLayout()
H3 = QHBoxLayout()

question = QLabel("рік")

btn_answer = QRadioButton("2023")
btn_wrong1 = QRadioButton("2022")
btn_wrong2= QRadioButton("205")
btn_wrong3 = QRadioButton("8023")

H1.addWidget(question, alignment=Qt.AlignmentFlag.AlignCenter)

H2.addWidget(btn_wrong2, alignment=Qt.AlignmentFlag.AlignCenter)
H2.addWidget(btn_wrong1, alignment=Qt.AlignmentFlag.AlignCenter)

H3.addWidget(btn_answer, alignment=Qt.AlignmentFlag.AlignCenter)
H3.addWidget(btn_wrong3, alignment=Qt.AlignmentFlag.AlignCenter)

window.resize(500,350)

main_line.addLayout(H1)
main_line.addLayout(H2)
main_line.addLayout(H3)

window.setLayout(main_line)
def show_win():
    msg=QMessageBox()
    msg.setText(("Правильно, грвня твоя"))
    msg.exec()

def show_lose():
    msg=QMessageBox()
    msg.setText(("Не правильно, з тебе косарь"))
    msg.exec()

btn_answer.clicked.connect(show_win)

btn_wrong1.clicked.connect(show_lose)
btn_wrong2.clicked.connect(show_lose)
btn_wrong3.clicked.connect(show_lose)




window.show()
app.exec()