# StoreProject

## Описание проекта

StoreProject - это веб-приложение для управления онлайн-магазином книг, построенное на Django. Этот проект включает функциональность для обработки заказов, управления товарами, а также интеграцию с Telegram для уведомлений.

### Функциональные возможности

- **Управление каталогом книг**: Администраторы могут добавлять, редактировать и удалять книги. Книги могут содержать заголовки, авторов, описания, обложки, цены и категории. Также доступна возможность поиска и фильтрации книг по различным критериям.
- **Обработка заказов**: Клиенты могут просматривать книги, добавлять их в корзину и оформлять заказы. Администраторы могут просматривать все заказы, изменять их статус (например, "в обработке", "отправлен", "доставлен") и отправлять уведомления клиентам о статусе заказа.
- **Управление пользователями**: Система поддерживает регистрацию и аутентификацию пользователей. Каждый пользователь может создавать и редактировать свой профиль, просматривать историю заказов. Администраторы имеют возможность управлять правами доступа пользователей.
- **Интеграция с Telegram**: Приложение отправляет уведомления администраторам о новых заказах и изменениях статуса заказов через Telegram. Это обеспечивает оперативное информирование и позволяет администраторам быстро реагировать на новые заказы.

### Дополнительные функции

- **Отзывы и рейтинги**: Пользователи могут оставлять отзывы и ставить рейтинги книгам, что помогает другим покупателям принимать решения о покупке.
- **Поддержка нескольких языков**: Приложение может быть локализовано на различные языки, что делает его доступным для пользователей из разных стран.
- **Оптимизация для мобильных устройств**: Приложение адаптировано для использования на мобильных устройствах, обеспечивая удобный доступ к магазину с любых устройств.
- **Административная панель**: Удобная административная панель позволяет управлять всеми аспектами магазина, включая книги, заказы, пользователей и настройки сайта.
- **Аналитика и отчеты**: Администраторы могут просматривать различные отчеты и аналитику, такие как продажи за определенный период, популярные книги, активность пользователей и т.д.

## Установка и запуск проекта

### Требования

- Python 3.6 или выше
- Windows (команды выполняются через CMD от имени Администратора)

### Шаги установки

1. Перейдите в директорию проекта:

   ```sh
   cd путь\к\проекту\Book-Haven-branch_desc
   ```

2. Создайте виртуальное окружение:

   ```sh
   python -m venv venv
   ```

3. Активируйте виртуальное окружение:

   ```sh
   .\venv\Scripts\activate
   ```

4. Установите зависимости:

   ```sh
   pip install -r requirements.txt
   ```

5. Создайте файл `.env`:

   ```sh
   echo. > .env
   ```

6. Откройте файл `.env` с помощью блокнота и добавьте следующие строки:

   ```
   SECRET_KEY='your_secret_key'
   TELEGRAM_TOKEN='your_telegram_token'
   TELEGRAM_CHAT_ID='your_telegram_chat_id'
   ```

7. Перейдите в директорию `OnlineStore`:

   ```sh
   cd OnlineStore
   ```

8. Обновите pip:

   ```sh
   python -m pip install --upgrade pip
   ```

9. Установите необходимые пакеты:

   ```sh
   pip install django
   pip install python-dotenv
   pip install django-taggit
   pip install python-telegram-bot
   python -m pip install Pillow
   pip install selenium
   pip install fuzzywuzzy[speedup]
   ```

10. Примените миграции базы данных:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

11. Загрузите начальные данные:

    ```sh
    python manage.py load_custom_data
    ```

12. Создайте суперпользователя:

    ```sh
    python manage.py createsuperuser
    ```

    Вас попросят ввести имя, почту и пароль для администратора.

13. Запустите сервер:
    ```sh
    python manage.py runserver
    ```

Теперь проект должен быть доступен по адресу `http://127.0.0.1:8000/`.

## Примеры использования

### Добавление новой книги

Чтобы добавить новую книгу в каталог, администратор должен войти в административную панель, выбрать раздел "Книги" и нажать кнопку "Добавить книгу". Далее необходимо заполнить все поля формы, такие как заголовок, автор, описание, цена и категория, а также загрузить изображение обложки. После сохранения книга станет доступной для пользователей в каталоге магазина.

### Оформление заказа

Пользователь может выбрать понравившиеся книги и добавить их в корзину. После этого он может перейти к оформлению заказа, где нужно указать контактную информацию и выбрать способ доставки. После подтверждения заказа пользователь получит уведомление о его статусе, а администратор будет уведомлен через Telegram о новом заказе.

### Управление пользователями

Администратор может просматривать список всех зарегистрированных пользователей, изменять их данные или удалять учетные записи. В административной панели также можно назначать права доступа, например, сделать пользователя администратором.

## Контакты

Если у вас есть вопросы или предложения, пожалуйста, свяжитесь с нами по email: k21_kazan.ys@server.odessa.ua, k21_fediaev.io@server.odessa.ua, k21_osypenko.sv@srtver.odessa.ua.

## Лицензия

Этот проект лицензирован под MIT License. Подробности смотрите в файле LICENSE.

# StoreProject

## Project Description

StoreProject is a web application for managing an online bookstore, built with Django. This project includes features for handling orders, managing products, and integrating with Telegram for notifications.

### Features

- **Book Catalog Management**: Administrators can add, edit, and delete books. Books can include titles, authors, descriptions, covers, prices, and categories. There is also a search and filter functionality for books.
- **Order Processing**: Customers can browse books, add them to the cart, and place orders. Administrators can view all orders, update their status (e.g., "processing," "shipped," "delivered"), and send notifications to customers about the order status.
- **User Management**: The system supports user registration and authentication. Each user can create and edit their profile, view their order history. Administrators can manage user access rights.
- **Telegram Integration**: The application sends notifications to administrators about new orders and order status changes via Telegram. This ensures prompt information and allows administrators to respond quickly to new orders.

### Additional Features

- **Reviews and Ratings**: Users can leave reviews and rate books, helping other customers make purchasing decisions.
- **Multilingual Support**: The application can be localized into various languages, making it accessible to users from different countries.
- **Mobile Optimization**: The application is optimized for use on mobile devices, ensuring a convenient shopping experience from any device.
- **Admin Panel**: A user-friendly admin panel allows managing all aspects of the store, including books, orders, users, and site settings.
- **Analytics and Reports**: Administrators can view various reports and analytics, such as sales over a specific period, popular books, user activity, etc.

## Installation and Running the Project

### Requirements

- Python 3.6 or higher
- Windows (commands must be run as Administrator)

### Installation Steps

1. Navigate to the project directory:

   ```sh
   cd path\to\project\Book-Haven-branch_desc
   ```

2. Create a virtual environment:

   ```sh
   python -m venv venv
   ```

3. Activate the virtual environment:

   ```sh
   .\venv\Scripts\activate
   ```

4. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

5. Create the `.env` file:

   ```sh
   echo. > .env
   ```

6. Open the `.env` file with a text editor and add the following lines:

   ```
   SECRET_KEY='your_secret_key'
   TELEGRAM_TOKEN='your_telegram_token'
   TELEGRAM_CHAT_ID='your_telegram_chat_id'
   ```

7. Navigate to the `OnlineStore` directory:

   ```sh
   cd OnlineStore
   ```

8. Upgrade pip:

   ```sh
   python -m pip install --upgrade pip
   ```

9. Install the required packages:

   ```sh
   pip install django
   pip install python-dotenv
   pip install django-taggit
   pip install python-telegram-bot
   python -m pip install Pillow
   pip install selenium
   pip install fuzzywuzzy[speedup]
   ```

10. Apply database migrations:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ``
    ```

`

11. Load initial data:

    ```sh
    python manage.py load_custom_data
    ```

12. Create a superuser:

    ```sh
    python manage.py createsuperuser
    ```

    You will be prompted to enter a username, email, and password for the admin account.

13. Run the server:
    ```sh
    python manage.py runserver
    ```

The project should now be accessible at `http://127.0.0.1:8000/`.

## Usage Examples

### Adding a New Book

To add a new book to the catalog, an administrator needs to log in to the admin panel, select the "Books" section, and click the "Add book" button. Then, all fields in the form must be filled in, such as title, author, description, price, and category, as well as uploading a cover image. After saving, the book will be available to users in the store catalog.

### Placing an Order

A user can choose the desired books and add them to the cart. Then, they can proceed to checkout, where they need to provide contact information and choose a delivery method. After confirming the order, the user will receive a notification about its status, and the administrator will be notified via Telegram of the new order.

### Managing Users

An administrator can view the list of all registered users, edit their information, or delete accounts. In the admin panel, it's also possible to assign access rights, for example, making a user an administrator.

## Contact

If you have any questions or suggestions, please contact us at: k21_kazan.ys@server.odessa.ua, k21_fediaiev.io@server.odessa.ua, k21_osypenko.sv@srtver.odessa.ua.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
