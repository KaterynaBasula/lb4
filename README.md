Використання Socket API для мережевих додатків 


[easy] Розробити echo-сервер з використанням python socket API, який приймає з'єднання від клієнта та повертає клієнту отримані дані.

Розробимо код з використанням python socket API, який приймає з'єднання від клієнта та повертає клієнту отримані дані, див. рис. 1.

![1](https://github.com/user-attachments/assets/2584f992-b4ad-46ad-af95-7b120952f016)
Рисунок 1 - Еcho-сервер

На рис. 1 можна побачити, що сервер був успішно запущенний. 
Echo-сервер є програмою, що використовує TCP-сокет для приймання даних від клієнта та їхнього зворотного відправлення. Спочатку сервер створює сокет за допомогою бібліотеки socket, використовуючи IPv4 (AF_INET) і тип з'єднання SOCK_STREAM, який призначений для TCP. Він налаштовує адресу та порт, на яких працюватиме сервер: у даному випадку 127.0.0.1 (локальний хост) і порт 12345. Після цього викликається метод bind(), який прив'язує серверний сокет до вказаних параметрів, і listen(), що переводить сокет у режим очікування з'єднань від клієнтів. Коли клієнт підключається до сервера, викликається метод accept(), який створює новий канал для обміну даними з клієнтом і повертає адресу клієнта. Далі сервер у циклі читає дані від клієнта через метод recv(), який отримує блок даних розміром до 1024 байти. Якщо отримані дані є непорожніми, сервер відправляє їх назад клієнту за допомогою sendall(). Цей процес триває до тих пір, поки клієнт не завершить з'єднання.

[easy] Розробити echo-клієнт з використанням python socket API, який встановлює з'єднання з сервером, надсилає строкові дані та отримує відповідь. 

Тепер розробимо код з використанням python socket API, який встановлює з'єднання з сервером, надсилає строкові дані та отримує відповідь, див. рис. 2.

![2](https://github.com/user-attachments/assets/18cf2b9a-f4a1-4843-811c-491351ddfcfd)
Рисунок 2 - Еcho-клієнт

На рис. 2 можна побачити, щопісля запуску echo-клієнт було написано повідомлення та отримано відповідь.
Echo-клієнт також використовує TCP-сокет, але на відміну від сервера, він ініціює з'єднання з використанням методу connect(), передаючи IP-адресу та порт сервера. Після встановлення з'єднання клієнт вводить текстове повідомлення, яке кодується у формат байтів методом encode() і відправляється на сервер через метод sendall(). Сервер отримує дані та надсилає їх назад, а клієнт отримує відповідь за допомогою recv() і декодує її для виведення на екран. Цикл триває до тих пір, поки користувач не введе команду для завершення, наприклад, "exit".

[medium] Модифікувати TCP-сервер з п.1, щоб він працював постійно та обробляв запити від багатьох клієнтів послідовно. Для тестування сервера. запустити декілька разів клієнт з пункту 1-а. 

Модифікуємо TCP-сервер з п.1, див. рис. 3.

![3](https://github.com/user-attachments/assets/715cac79-b9f6-452a-a7fd-20c8d8dc2787)
Рисунок 3 - Модифікація TCP-сервера

На рис. 3 можна побачити, що TCP-сервер був успішно запущений. Тепер запустимо Еcho-клієнт, див. рис. 4.

![4](https://github.com/user-attachments/assets/de09636d-45d1-43db-8573-595d7f60e52a)
Рисунок 4 - Запуск Еcho-клієнт

На рис. 4 можна побачити, що все успішно працює. 
Модифікований TCP-сервер для обробки багатьох клієнтів використовує нескінченний цикл while True для приймання нових підключень. На кожному підключенні він створює канал зв'язку з клієнтом і обробляє його запит. При цьому сервер працює послідовно: він чекає, поки один клієнт завершить роботу, після чого переходить до обслуговування наступного. Для кожного клієнта дані отримуються і відправляються назад аналогічно базовому echo-серверу, але цей процес повторюється для необмеженої кількості клієнтів у межах одного запуску сервера.

[medium/hard]  Розробити TCP-сервер з використанням python socket API, який приймає текстовий файл від клієнта та зберігає його локально на стороні сервера.

Розробимо код  з використанням python socket API, який приймає текстовий файл від клієнта та зберігає його локально на стороні сервера, див. рис. 5.

![5](https://github.com/user-attachments/assets/4c27114d-52a6-460f-8b22-b286c82b35ad)
Рисунок 5 - TCP-сервер 

На рис. 5 можна побачити, що сервер був успішно запущений.
TCP-сервер для приймання файлів працює подібно до базового сервера, але замість обміну текстовими даними він отримує файл від клієнта і зберігає його локально на сервері. Після приймання з'єднання сервер відкриває файл у бінарному режимі wb для запису. Дані передаються блоками по 1024 байти і зберігаються у файлі за допомогою методу write(). Цикл триває до тих пір, поки клієнт не завершить передачу файлу, тобто коли сервер не отримає порожній блок даних.

[medium]  Розробити TCP-клієнт, який відправляє будь-який текстовый файл на сервер. 

Створюємо текстовий файл з якимось повідомленням, див. рис. 6.

![6](https://github.com/user-attachments/assets/9ecbe0d0-6e21-473e-82dc-95cb584f2b13)
Рисунок 6 - Вміст текстового файлу

Запускаємо file_server.py nf file_client.ry та отримуємо те ж повідомлення у новому тектовому файлі, див. рис. 7

![7](https://github.com/user-attachments/assets/d5a722c1-38aa-453b-b46e-687e57a55e0a)
Рисунок 7 - Отримане повідомлення

На рис. 7 можна побачити, що повідомлення було успішно отримано.

Висновок

Таким чином, базовий echo-сервер і echo-клієнт демонструють основи обміну текстовими даними через TCP-сокет. Модифікований сервер дозволяє обробляти декілька клієнтів послідовно, а сервер і клієнт для передачі файлів розширюють функціонал, забезпечуючи можливість обміну файлами між клієнтом і сервером. Ці програми є основою для більш складних мережевих додатків та дозволяють ознайомитися з принципами роботи TCP-з'єднань у Python.





