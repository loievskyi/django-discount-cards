# django-discount-cards

[Тестовое задание](https://github.com/loievskyi/django-discount-cards/blob/master/python_test.txt)

## Установка

Использовался Python3.9.5 и Django версии 3.2.5.
Перед началом рекомендуется установить и запустить виртуальное окружение.
Далее нужно перейти из терминала (или консоли) в папку проекта.
После уствновить необходимые пакеты:


```bash
python -m pip install -r requirements.txt
```

Далее:
```bash
python manage.py migrate
python manage.py compilemessages
```

Для запуска сервера:

```bash
python manage.py runserver
```

## Скрины

### Список карт с полями

![alt text](https://github.com/loievskyi/django-discount-cards/blob/master/screens/discount-cards-list.png)

Список карт доступен по адресу /discount-cards/list/

### Просмотр профиля карты с историей покупок по ней

![alt text](https://github.com/loievskyi/django-discount-cards/blob/master/screens/discount-cards-detail.png)

Профиль доступен по адресу /discount-cards/\<id\>/ (или по нажатию на кнопку "Детали" в списке)

### Изменение статуса карты

![alt text](https://github.com/loievskyi/django-discount-cards/blob/master/screens/discount-cards-edit.png)

Изменение статуса карты доступно по адресу /discount-cards/edit/\<id\>/ (или по нажатию на кнопку "Редактировать" в списке)

### Удаление карты (DRF)

![alt text](https://github.com/loievskyi/django-discount-cards/blob/master/screens/discount-cards-delete-confirm.png)

Изменение статуса карты доступно отправкой delete запроса по адресу /api/v1/discount-cards/\<id\>/ (или по нажатию на кнопку "Удалить" в списке)

![alt text](https://github.com/loievskyi/django-discount-cards/blob/master/screens/discount-cards-delete.png)

### Поиск и фильтрация (DRF)

![alt text](https://github.com/loievskyi/django-discount-cards/blob/master/screens/api-discount-cards-search-filters.png)

Поиск доступен по полям "seria", "number", "status", "end_date".
Фильтрация доступна по всем полям.

![alt text](https://github.com/loievskyi/django-discount-cards/blob/master/screens/api-discount-cards-search-result.png)

### API Список дисконтных карт (DRF)

![alt text](https://github.com/loievskyi/django-discount-cards/blob/master/screens/api-discount-cards-list.png)

Список дисконтных карт (/api/v1/discount-cards/)

### API Детали дисконтной карт (DRF)

![alt text](https://github.com/loievskyi/django-discount-cards/blob/master/screens/api-discount-cards-detail.png)

Список дисконтных карт (/api/v1/discount-cards/\<id\>/)
