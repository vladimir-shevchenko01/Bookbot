# Книжный бот

## Описание

Книжный бот представляет собой телеграм-бот, который позволяет пользователям читать книгу прямо в чате и практиковаться с использованием инлайн-кнопок. Он имеет следующие основные функции:

- Загрузка страниц книги из хранилища и отправка их в чат в виде сообщений с кнопками.
- Сохранение последней прочитанной страницы, чтобы пользователь мог возобновить чтение с того же места.
- Возможность вернуться к началу книги.

Кроме основного функционала, бот также предлагает следующие дополнительные функции:

- Сохранение закладок - страниц книги, которые пользователь хочет сохранить.
- Редактирование списка закладок (удаление ненужных).

## Взаимодействие с ботом

1. Пользователь отправляет команду `/start` боту или находит его в поиске и запускает его.
2. Бот приветствует пользователя и сообщает, что пользователь может читать книгу прямо в чате с ботом. Бот также предлагает посмотреть список доступных команд, отправив команду `/help`.
3. Пользователь может выполнить одно из следующих действий:
   - Отправить команду `/help`, чтобы увидеть список доступных команд и получить информацию о сохранении страниц в закладки.
   - Отправить команду `/beginning`, чтобы получить первую страницу книги и инлайн-кнопки для навигации (назад, текущая страница, вперед).
   - Отправить команду `/continue`, чтобы получить страницу книги, на которой пользователь остановился во время последнего чтения. Если пользователь еще не начинал чтение, бот отправит первую страницу книги.
   - Отправить команду `/bookmarks`, чтобы получить список сохраненных закладок в виде инлайн-кнопок. Бот также предоставит возможность редактирования или удаления закладок.
   - Отправить любое другое сообщение, на которое бот будет реагировать, сообщая, что такая команда неизвестна.

### Взаимодействие с книгой

При взаимодействии с сообщением-книгой пользователь может выполнить следующие действия:

- Нажать на кнопку "Вперед", чтобы загрузить следующую страницу книги, если текущая страница не последняя. Номер текущей страницы увеличится на 1. Если текущая страница последняя, ничего не изменится.
- Нажать на кнопку с текущим номером страницы, чтобы сохранить эту страницу в закладки.
- Нажать на кнопку "Назад", чтобы загрузить предыдущую страницу книги, если текущая страница не первая. Номер текущей страницы уменьшится на 1. Если текущая страница первая, ничего не изменится.
- Пользователь отправляет в чат любое другое сообщение: Бот реагирует на такое сообщение отвечая, что такой команде он не обучен.