from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from random import randint

app = QApplication([])
window = QWidget()

line = QVBoxLayout()

text = QLabel("Випадкове число")
number = QLabel("?")
button = QPushButton("Згенерувати")


line.addWidget(text)
line.addWidget(number)
line.addWidget(button)

window.setLayout(line)

def generate_rand ():
    r = randint(0,100) 
    number.setText(str(r))

button.clicked.connect(generate_rand)




window.show()
app.exec()