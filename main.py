from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from rsa import generate_keys, encrypt, decrypt
import sys


class RSAMainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.e, self.d, self.n = generate_keys()

        self.setWindowTitle('RSA Encryption/Decryption')
        self.setGeometry(100, 100, 400, 400)

        self.layout = QVBoxLayout()

        self.label = QLabel('Введите сообщение:')
        self.layout.addWidget(self.label)

        self.input_text = QTextEdit(self)
        self.layout.addWidget(self.input_text)

        self.encrypt_button = QPushButton('Зашифровать', self)
        self.encrypt_button.clicked.connect(self.encrypt_message)
        self.encrypt_button.clicked.connect(self.decrypt_message)
        self.layout.addWidget(self.encrypt_button)

        self.decrypted_label = QLabel('Зашифрованное сообщение:')
        self.layout.addWidget(self.decrypted_label)

        self.encrypted_text = QTextEdit(self)
        self.encrypted_text.setReadOnly(True)
        self.layout.addWidget(self.encrypted_text)

        self.plain_label = QLabel('Расшифрованное сообщение:')
        self.layout.addWidget(self.plain_label)

        self.decrypted_text = QTextEdit(self)
        self.decrypted_text.setReadOnly(True)
        self.layout.addWidget(self.decrypted_text)

        self.setLayout(self.layout)

    def encrypt_message(self):
        message = self.input_text.toPlainText()
        encrypted = encrypt(message, self.e, self.n)
        self.encrypted_text.setPlainText(" ".join(map(str, encrypted)))

    def decrypt_message(self):
        encrypted_message = list(map(int, self.encrypted_text.toPlainText().split()))
        decrypted = decrypt(encrypted_message, self.d, self.n)
        self.decrypted_text.setPlainText(decrypted)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RSAMainWindow()
    window.show()
    sys.exit(app.exec_())
