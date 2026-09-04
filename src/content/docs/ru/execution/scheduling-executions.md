---
title: Планирование выполнения
description: Прогоны без участия человека и без CI-сервера: запуск скрипта TCShell через bat-файл из Планировщика заданий Windows.
level: 2
sidebar:
  order: 80
sources:
  - id: EWJxuLJyJWU
    title: "Tosca Tutorial| Lesson 141 - Common RealTime Tosca Problems & Fixes | Schedule Automated Executions|"
    url: https://www.youtube.com/watch?v=EWJxuLJyJWU
    at: "00:12"
---

Автоматизированные тесты, которые кто-то каждый день запускает руками, обесценивают автоматизацию. В каждом проекте должно быть **выполнение без присмотра (unattended execution)**: расписание, по которому ExecutionList запускаются без человека за столом. Обычный ответ — CI/CD-инструмент ([Jenkins](/ToscaBase/ru/execution/ci-integration-jenkins/)), но когда CI недоступен, скрипт TCShell по любому расписанию может запускать **Планировщик заданий Windows (Task Scheduler)**.

Строительные блоки те же, что и для интеграции с Jenkins: скрипт `.tcs`, говорящий Commander, что делать, и файл `.bat`, вызывающий TCShell с этим скриптом. Планировщик лишь заменяет триггер.

## Скрипт TCShell

TCShell — инструмент командной строки Tosca для управления Commander без его открытия; его команды описаны в [Инструменты командной строки](/ToscaBase/ru/administration/command-line-tools/). Скрипт из демо (`script.tcs`) делает четыре вещи:

1. `jumptonode` к запускаемому ExecutionList по его пути в разделе Execution (папка Execution > папка ExecutionList > `Swag Labs` > `Run login`).
2. Задача, которая **очищает лог**.
3. Задача, которая **запускает** ExecutionList.
4. Задача, которая **сохраняет** результаты.

## Bat-файл

Bat-файл (`execute.bat` в демо) содержит две команды:

1. `cd` в домашнюю папку Commander.
2. Команду TCShell с путём к файлу workspace, учётными данными (пустыми для локального workspace) и путём к скрипту в качестве параметра, например `C:\training\tcshell_script.tcs`.

Создайте его в Блокноте и сохраните с расширением `.bat`.

## Создание запланированной задачи

1. Откройте **Task Scheduler**, перейдите в **Task Scheduler Library** и нажмите **Create Task** на панели **Actions**.
2. **General**: введите имя (`Tosca executions`) и описание; отметьте **Run with highest privileges**.
3. **Triggers > New**: оставьте **On a schedule**; выберите **One time** для первой проверки (в демо время ставится на две минуты вперёд) или **Daily**/**Weekly** для реальной работы. Расширенные настройки позволяют случайную задержку, повтор задачи каждый час в течение периода и срок истечения.
4. **Actions > New**: действие **Start a program**, укажите файл `.bat`.
5. Подтвердите. Задача появится в библиотеке со статусом **Ready**, временем последнего триггера и **временем следующего запуска**. Правый клик > **Run** запускает её сразу, не дожидаясь.

В назначенное время сама откроется командная строка, выполнит команды bat-файла, прогонит ExecutionList и завершит задачу.

:::caution
В момент срабатывания задачи workspace в Commander должен быть **закрыт**. TCShell входит в workspace, а в локально открытый workspace второй раз войти нельзя; прогон просто ждёт. В демо это и происходит: первый триггер зависает, пока workspace не закрыт, и триггер приходится редактировать, чтобы он сработал снова.
:::

## См. также

- [Интеграция с Jenkins](/ToscaBase/ru/execution/ci-integration-jenkins/) использует тот же скрипт и bat-файл за CI-сборкой.
- [Распределённое выполнение](/ToscaBase/ru/execution/distributed-execution-dex/): запуск TestEvent на удалённых агентах вместо локальной машины.
