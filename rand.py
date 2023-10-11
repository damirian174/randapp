from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QPushButton, QWidget, QGridLayout, \
    QLabel, QSpinBox
from PyQt5.QtGui import QIcon
import sys
import random
import string
import os
from PyQt5.QtWinExtras import QtWin


class Mainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RandomApp")
        icon_path = os.path.join(os.path.dirname(sys.executable), 'icon.ico')
        self.setWindowIcon(QIcon(icon_path))
       # self.iconbitMap(icon_path)
        self.setWindowIcon(QIcon('icon.ico'))
        self.resize(350, 250)
        self.spinbox = QSpinBox(self)
        self.spinbox.setGeometry(10, 10, 100, 30)
        self.spinbox.valueChanged.connect(self.handle_value_changed)

        self.btn = QPushButton('Generate', self)
        self.btn.clicked.connect(self.rand)
        self.btn.setStyleSheet("QPushButton {"
                               "border: none;"
                               "border-radius: 25px;"
                               "background-color: blue;"
                               "color: white;"
                               "padding: 10px;"
                               "}"
                               "QPushButton:hover {"
                               "background-color: grey;"
                               "}"
                               "QPushButton:pressed {"
                               "background-color: white;"
                               "}")
        self.btnquit = QPushButton('Cancel', self)
        self.btnquit.clicked.connect(self.close)
        self.btnquit.setStyleSheet("QPushButton {"
                                   "border: none;"
                                   "border-radius: 25px;"
                                   "background-color: red;"
                                   "color: white;"
                                   "padding: 10px;"
                                   "}"
                                   "QPushButton:hover {"
                                   "background-color: grey;"
                                   "}"
                                   "QPushButton:pressed {"
                                   "background-color: white;"
                                   "}")

        self.btnsave = QPushButton(self)
        self.btnsave.setIcon(QIcon('save.png'))
        self.btnsave.setIconSize(self.btnsave.size())
        self.btnsave.clicked.connect(self.save)
        self.btnsave.setFixedWidth(40)
        self.btnsave.setFixedHeight(35)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QGridLayout(central_widget)
        b = QLabel('Добро пожаловать в приложение генератор паролей', self)
        c = QLabel('                        Ваш случайный пароль', self)
        e = QLabel('Укажите сложность пароля', self)
        self.d = QLabel('    ', self)

        layout.addWidget(b, 0, 0)
        layout.addWidget(c, 1, 0)
        layout.addWidget(self.d, 2, 0)
        layout.addWidget(e, 3, 0)
        layout.addWidget(self.btn, 4, 0)
        layout.addWidget(self.btnquit, 5, 0)
        layout.addWidget(self.btnsave, 4, 1)
        layout.addWidget(self.spinbox, 3, 1)

        self.show()

    def handle_value_changed(self, value):
        print(value)

    def rand(self):
        password_length = self.spinbox.value()
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(password_length))
        self.d.setText(f'                                       {password}')

    def save(self):
        if self.d.text().strip() == '':
            QMessageBox.critical(self, "Ошибка", "Случайный пароль не сгенерировано!")
            return

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "Текстовые файлы (*.txt);;Все файлы (*)",
                                              options=options)

        if file:
            if not file.endswith('.txt'):
                file += '.txt'
            with open(file, 'w') as f:
                f.write(self.d.text().strip())

if __name__ == '__main__':
    try:
        myappid = 'mycompany.myproduct.subproduct.version'
        QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
    except ImportError:
        pass
    app = QApplication(sys.argv)
   # app.setWindowIcon(QIcon('icon.ico'))
    dlgMain = Mainwindow()
    dlgMain.show()
    sys.exit(app.exec_())
