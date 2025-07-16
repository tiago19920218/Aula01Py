
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])
janela = QWidget()
janela.setWindowTitle("Minha Primeira Janela")
rotulo = QLabel("Aula de Python!!!", parent=janela)

janela.resize(500,400)

janela.show()

app.exec_()