# Django-Stripe
___
Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:

1 Django Модель Item с полями (name, description, price)  
2 API с двумя методами:  
2.1 GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. 
2.2 2GET /{id}/, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. 

## Дополнительные задачи:
☑ Запуск используя Docker  
☑ Использование environment variables  
☑ Просмотр Django Моделей в Django Admin панели
___
## Запустить проект:
Клонировать репозиторий и перейти в него в командной строке:  
```
https://github.com/Flowmikro/Django-Stripe.git
```  
```
cd Django-Stripe
```  
Получить ключи Stripe  
Вставить в .env все переменные которые вам нужны  
____
Запустить НЕ используя Docker:
```angular2html
python3 -m venv venv 
```
```angular2html
.\venv\Scripts\activate
source venv/bin/activate mac|linux
```
Установить пакеты
```angular2html
pip install -r requirements.txt
```
Запустить сервер
```angular2html
python manage.py runserver
```
___
Запустить через Docker:
```
docker-compose up -d --build
```  
Перейти по ссылке: http://127.0.0.1:8000/
___
