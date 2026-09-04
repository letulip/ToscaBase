---
title: Tosca Execution Client
description: Запуск DEX TestEvent из командной строки или CI/CD-конвейера скриптом Tosca Execution Client (PowerShell/shell) и вызов его из Jenkins.
level: 2
sidebar:
  order: 110
sources:
  - id: e5hbUh6SM08
    title: "Tosca Tutorial | Lesson 153 - Tosca Execution Client | Script Based CI/CD Integration | Powershell |"
    url: https://www.youtube.com/watch?v=e5hbUh6SM08
    at: "00:03"
---

**Tosca Execution Client (клиент выполнения)** — инструмент командной строки, появившийся в Tosca 15.2, который запускает **TestEvent** на Tosca Server из любой CI/CD-системы (Jenkins, GitLab, всё, что умеет выполнять скрипт). Ему требуется [распределённое выполнение с AOS](/ToscaBase/ru/execution/distributed-execution-dex/); события, конфигурации и агенты настраиваются там, клиент лишь запускает их и собирает результаты. По сравнению с путём через [TCShell и Jenkins](/ToscaBase/ru/execution/ci-integration-jenkins/) ему не нужен Commander на машине сборки, и он работает на Windows и Linux.

## Загрузка и предварительные условия

- Источник: репозиторий GitHub `tricentis/tosca-execution-client` (поиск «Tosca execution client»). Скачайте ветку `main` как ZIP и распакуйте в папку вроде `C:\execution\tosca-execution-client`. Внутри README и клиент: скрипт **PowerShell** для Windows и **shell**-скрипт для Linux.
- Поддерживается с Tosca **15.2** и выше.
- В Windows политика выполнения PowerShell по умолчанию блокирует скрипты (`Undefined`). В PowerShell выполните `Set-ExecutionPolicy Bypass -Scope LocalMachine` и подтвердите предупреждение безопасности. У Linux своя настройка, описанная в README.

## Параметры

Обязательные:

| Параметр | Значение |
|---|---|
| Tosca server URL | Например `http://localhost:80` или IP сервера с портом |
| Project name | **Имя корня проекта**, содержащего TestEvent |
| Events | JSON-массив имён TestEvent для запуска, либо |
| Events config file path | Путь к JSON-файлу с конфигурацией событий |

Необязательные: CA-сертификат, client ID и client secret (только для HTTPS), таймаут клиента, окружение выполнения, ID выполнения, интервал опроса, таймаут запроса, число повторов и задержка между ними, имя и папка файла результатов (по умолчанию рядом со скриптом), отключение логирования, путь к папке логов.

## Запуск из PowerShell

1. `cd` в папку клиента; запуск скрипта из другого места завершается ошибкой «not executable».
2. Выполните команду из README со своими значениями: имя скрипта PowerShell, URL сервера, события (в демо `sample` — TestEvent с DEX-конфигурацией и ExecutionList входа) и имя проекта (`multi-user`).

Вывод показывает, как событие **ставится в очередь**, стартует и завершается; тест выполняется на агенте (в демо вход на той же машине), а TestEvent отображается выполненным в Commander и DEX-мониторе. В папке клиента появляются два результата: папка `logs` для отладки и **XML результатов** с именем набора, числом тестов, сбоями и временем. Формат в стиле JUnit, так что любой плагин отчётов CI сможет его отрисовать.

## Запуск из Jenkins

1. Установите плагин **PowerShell**, если шага сборки нет: **Manage Jenkins > Plugins > Available plugins**, найдите `PowerShell`, установите.
2. **New Item > Freestyle project**, назовите (`execution client`), **OK**.
3. **Build > Add build step > PowerShell**, введите две строки: `cd` в папку клиента, затем ту же команду выполнения, что выше. **Save**.
4. **Build Now**. **Console Output** показывает тот же лог очереди/старта/завершения, тест выполняется на агенте, сборка заканчивается **SUCCESS**, результаты записаны в XML-файл.

Добавьте XML- или другой плагин отчётов для читаемого отчёта внутри сборки. Подключив задание к конвейеру команды, вы получите автоматический запуск TestEvent на каждое изменение кода.
