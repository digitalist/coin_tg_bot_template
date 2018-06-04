
# Waves Proof of Concept Telegram bot


### архитектурно:

асинхронный бот с диспетчером/мапером приходящих команд в callable объекты (похоже на паттерн Команда с Фабрикой)
достаточно легко реализуемые возможности: троттлинг пользователей, кэширование пользователей, сессий, списка токенов


использует telepot либу.

### Legend:

    +: done
    -: todo
    ~: легко сделать

+ async (для поддержки толпы пользователей одновременно)
+ поддержка livereload для разработки  (через aoiklivereload)
+ поддержка и waves и assets (любые токены) - (из имеющихся на балансе у бота, судя по тз?)
+ /tokens для списка id возможных токенов. дефолтный токен - waves
~ выдача token через тикеры вроде "/want 20 btc" (сейчас либо waves - по дефолту, либо по id токена)
+  для разработчиков: поддержка autoreload при изменении кода
-  поддержка сессии на пользователя (с таймаутом) - "чатовые транзакции" для вещей типа "подтвердить перевод, отменить при таймауте без подтверждения" - реализуется через telepot
-  поддержка инлайна (напр. баланс, типы токенов на балансе у бота) https://core.telegram.org/bots/inline


### реализованные команды

в порядке применения:
/reg ADDRESS - регистрирует адрес для user_id
/tokens - выдает список id токенов (пока грубо без тикеров и т.д.) 
/want AMOUNT - прислать waves если у бота есть AMOUNT
/want AMOUNT token - прислать AMOUNT токена, если у бота хватает
/help

- все команды лежат в src.commands

- для использования бота надо определить следующие переменные в env (пока так, чтобы не укладывать в репозиторий): `telegram_token` и `waves_private_key` - они попадают в объект конфига и уже оттуда используются в коде 

- не вся обработка ошибок/проверки реализованы полностью, поскольку главным я счел архитектурное решение.
- пока не успел прикрутить webhooks, но с использованием telepot это довольно тривиальная задача

- не вынес в конфиг chain и тест-ноду, использует node1 тестнета