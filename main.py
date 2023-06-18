




import socket
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QLineEdit, QPushButton
class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("p2p chat")
        self.message_history = QTextEdit()
        self.message_input = QLineEdit()
        self.send_button = QPushButton("send")
        self.send_button.clicked.connect(self.send_message)
        layout = QVBoxLayout()
        layout.addWidget(self.message_history)
        layout.addWidget(self.message_input)
        layout.addWidget(self.send_button)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.host = 'localhost'  # Enter your IP address or hostname
        self.port = 9999  # Choose a port number
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        print("connected.")
        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.start()
    def receive_messages(self):
        while True:
            try:
                data = self.sock.recv(1024).decode('utf-8')
                self.message_history.append(data)
            except OSError:
                break
    def send_message(self):
        message = self.message_input.text()
        self.sock.send(message.encode('utf-8'))
        self.message_input.clear()
def run_chat_app():
    app = QApplication([])
    window = ChatWindow()
    window.show()
    app.exec_()
if __name__ == '__main__':
    run_chat_app()






