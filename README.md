# Django + Stripe API
## Описание 
В данном проекте реализован простой сервер, который создает платежные формы для товаров с использованием Django и Stripe API.
Проверить работу приложения можете по данной [ссылке](https://django-stripe.herokuapp.com/). 
Существует несколько [тестовых карт](https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=checkout&integration=checkout#additional-testing-resources)
(4242 4242 4242 4242 - для проведения успешного платежа),
которые вы можете использовать, чтобы проверить работу приложения. Используйте их с любым CVC, почтой и сроком действия карты.

**GET** `/item/{id}` возвращает HTML страницу с информацией о выбранном товаре (Item) и кнопку Checkout, по нажатию которой происходит запрос на `/buy/{id}`.

**GET** `/buy/{id}` создает Checkout Session и перенаправляет на Checkout.

## Запуск приложения
1. Чтобы запустить приложение, убедитесь, что у вас установлены python и pip.
2. Выполните команду `pip install -r requirements.txt` для установки необходимых расширений.
3. Переименуйте `.env.example` в `.env`  и заполните **SECRET_KEY**, **STRIPE_API_KEY** и **DOMAIN**.
   - **SECRET_KEY** обычно задается автоматически при создании проекта. 
     В данном случае вы можете ввести любую последовательность символов (чем больше, тем лучше).
   - В **STRIPE_API_KEY** введите test secret key. Его можно найти в личном личном кабинете stripe, 
     переключив аккаунт в тестовый режим (Test mode). Dashboard > Developers > API keys.
   - **DOMAIN**=http://localhost:8000 (http://127.0.0.1:8000) - для работы приложения в локальной сети.


```
$ python manage.py createsuperuser  # создаем админа
...
$ python manage.py runserver        # запускаем программу
```
В личном кабинете админа `/admin` добавляем желаемое количество товаров (Item).

## Запуск приложения с Docker
Убедитесь, что у вас установлен [Docker](https://www.docker.com/).
Переименуйте `.env.example` в `.env`  и заполните **SECRET_KEY**, **STRIPE_API_KEY** и **DOMAIN**, как описано выше.

```
$ docker build .                                      # создаем контейнер
...
$ docker images                                       # определяем IMAGE ID для созданного контейнера
...
$ docker run --rm -d --publish 8000:8000 [IMAGE ID]   # запускаем программу через docker
...
$ docker exec -it [CONTAINER ID] bash -l              # для использования терминала внутри контейнера
$ python manage.py createsuperuser                    # создаем админа
...
Ctrl V to logout
```
Приложение будет доступно для тестирования на http://localhost:8000 (http://127.0.0.1:8000)
