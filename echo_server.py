import socket

HOST = '127.0.0.1'  # Локальний хост
PORT = 12345  # Порт для з'єднання

# Створюємо серверний сокет
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))  # Прив'язуємо сокет до адреси
    server_socket.listen()  # Чекаємо на клієнтські підключення
    print(f"Сервер запущено на {HOST}:{PORT}")

    conn, addr = server_socket.accept()  # Приймаємо підключення
    with conn:
        print(f"Підключено клієнта: {addr}")
        while True:
            data = conn.recv(1024)  # Отримуємо дані
            if not data:
                break
            print(f"Отримано: {data.decode()}")
            conn.sendall(data)  # Відправляємо дані назад
