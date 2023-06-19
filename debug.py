



import socket
import threading
def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024).decode('utf-8')
            print(data)
        except OSError:
            break
def send_message(sock):
    while True:
        message = input()
        sock.send(message.encode('utf-8'))

def start_chat(port):
    host = 'localhost'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print("connected")
    receive_thread = threading.Thread(target=receive_messages, args=(sock,))
    receive_thread.start()
    send_thread = threading.Thread(target=send_message, args=(sock,))
    send_thread.start()
    
if __name__ == '__main__':
    port1 = 9999
    port2 = 8888
    thread1 = threading.Thread(target=start_chat, args=(port1,))
    thread2 = threading.Thread(target=start_chat, args=(port2,))
    thread1.start()
    thread2.start()




