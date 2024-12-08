import socket

HOST = '127.0.0.1'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Сервер працює на {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()  # Приймаємо підключення від клієнта
        with conn:
            print(f"Підключено клієнта: {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Отримано від {addr}: {data.decode()}")
                conn.sendall(data)  # Відправляємо отримані дані назад
