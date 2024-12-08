import socket

HOST = '127.0.0.1'  # Адреса сервера
PORT = 12345        # Порт сервера

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))  # Підключаємося до сервера
    while True:
        message = input("Введіть повідомлення для сервера (або 'exit' для виходу): ")
        if message.lower() == 'exit':
            break
        client_socket.sendall(message.encode())  # Відправляємо дані
        data = client_socket.recv(1024)  # Отримуємо відповідь
        print(f"Відповідь сервера: {data.decode()}")
