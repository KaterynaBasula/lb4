import socket

HOST = '127.0.0.1'
PORT = 12345
FILENAME = 'received_file.txt'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Сервер чекає на файл на {HOST}:{PORT}")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Підключено клієнта: {addr}")
        with open(FILENAME, 'wb') as file:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                file.write(data)  # Записуємо отримані дані у файл
        print(f"Файл збережено як {FILENAME}")
