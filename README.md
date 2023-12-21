# Django-Stripe
___
Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:

1 Django Модель Item с полями (name, description, price)  
2 API с двумя методами:  
2.1 GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса  
2.2 2GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)

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
Запустить через Docker:
```
docker-compose up -d --build
```  
Перейти по ссылке: http://127.0.0.1:8000/