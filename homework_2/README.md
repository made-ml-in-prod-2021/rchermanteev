# Домашнее задание 2.

### Pull контейнера с docker hub:

    docker pull rchermanteev/2020_made_ml_in_production

### Запуск контейнера:

    docker run -p 5000:5000 rchermanteev/2020_made_ml_in_production
    
### Сборка контейнера(если не пользоваться docker hub):

    docker build -t rchermanteev/2020_made_ml_in_production .

### Установка зависимостей: 

    pip install -r requirements.txt
    
### Запуск скрипта с отправкой запросов на получение предсказаний:

    python make_request.py

### Чек лист:
      
    0) создал ветку homework2

    1) написал REST сервис, используя FastApi. Реализовал endpoint /predict (3)
    
    2) Написал тесты для /predict  (3) 
    
    3) Написал скрипт, который будет делать запросы к сервису (2)
    
    4) Сделал валидацию входных данных (3 - доп баллы)
    
    5) Добавил докерфайл, описал работу с ним в README (4)
    
    6) Пока оптимизировал только путём выбора легковесной основы и устранением ненужных пакетов (1 - доп баллы)
    
    7) опубликовал образ в https://hub.docker.com/ (2)
    
    8) Описал в README работу с docker hub-ом (1)
    
    5) этот чек-лист считать самооценкой (1 - доп балл)
    
    6) создал пулл-реквест и поставил label -- hw2
    
    Всего: 20