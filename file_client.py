import socket

HOST = '127.0.0.1'
PORT = 12345
FILENAME = 'example.txt'  # Текстовий файл для відправки

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print(f"Підключено до сервера {HOST}:{PORT}")

    with open(FILENAME, 'rb') as file:
        for data in file:
            client_socket.sendall(data)  # Відправляємо файл блоками
    print("Файл успішно відправлено!")
