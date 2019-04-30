# Поиск победителя конкурса в Инстаграм

Модуль создает список пользователей Инстаграм для определения победителя в конкурсе,
которые удовлетворяют следующим условиям: подписаться, поставить лайк и отметить друга.

## Как установить

Для использования модуля необходимо зарегистрироваться на сайте [Инстаграм](https://www.instagram.com/ "https://www.instagram.com/") и получить логин и пароль для подключения.
После скачивания в этой же папке создаем .env файл, который должен содержать строки:

`LOGIN=Ваш логин`
`PASSWORD=Ваш пароль`


Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
`pip install -r requirements.txt`

Для запуска скрипта в качестве аргумента надо указать Имя пользователя разместившего пост и ссылку на этот пост:

`main.py beautybar.rus https://www.instagram.com/p/BtON034lPhu/`


## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/modules/ "https://dvmn.org/modules/").