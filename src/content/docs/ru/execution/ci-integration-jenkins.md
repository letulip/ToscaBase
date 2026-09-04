---
title: Интеграция с Jenkins
description: Запуск задач Tosca Commander из freestyle-задания Jenkins через выполнение bat-файла Windows, который вызывает TCShell со скриптом .tcs.
level: 2
sidebar:
  order: 90
sources:
  - id: GFVCsjV-8_w
    title: "Tosca Tutorial | Lesson 89 - Run Tosca Commander Tasks from Jenkins | CI/CD | DevOps |"
    url: https://www.youtube.com/watch?v=GFVCsjV-8_w
    at: "00:03"
---

TCShell позволяет выполнить ExecutionList из командной строки, не открывая Commander (см. [Инструменты командной строки](/ToscaBase/ru/administration/command-line-tools/)). Но набирать эту команду — всё ещё ручной шаг. Обёрнутая в задание **Jenkins**, она превращается в кнопку, расписание или триггер на изменение кода, что и нужно CI/CD-конвейеру. Этот документ описывает путь через TCShell; более новая альтернатива для [распределённого выполнения](/ToscaBase/ru/execution/distributed-execution-dex/) — [Tosca Execution Client](/ToscaBase/ru/execution/tosca-execution-client/).

## Предварительное условие: bat-файл

Jenkins не может выполнить скрипт `.tcs` напрямую, поэтому нужен bat-файл Windows, вызывающий TCShell. Демонстрационный `execute.bat` содержит те же две команды, что используются из командной строки:

1. `cd` в домашнюю папку Commander.
2. Команда TCShell, вызывающая `script.tcs`.

Скрипт `.tcs` хранит задачи Commander (перейти к ExecutionList, запустить, сохранить), поэтому bat-файл никогда не меняется: чтобы сделать что-то другое, меняйте скрипт. Создайте bat-файл в Блокноте и сохраните как `.bat`.

## Создание задания Jenkins

В демо используется локальный экземпляр Jenkins; на серверном шаги те же, возможно с дополнительной настройкой.

1. **New Item**, выберите **Freestyle project** (Pipeline тоже подходит), назовите, например `Tosca_Execute_CI`, и нажмите **OK**.
2. Пропустите необязательные разделы (description, discard old builds, source code management, build triggers), если они не нужны. В build triggers задаются периодическое расписание или опрос SCM.
3. В разделе **Build** нажмите **Add build step > Execute Windows batch command**.
4. Введите две строки: `cd` в каталог с bat-файлом, затем `execute.bat`.
5. **Save**.

Нажмите **Build Now**. **Console Output** показывает то же, что и командная строка: TCShell входит в workspace, выполняет задачи скрипта, и сборка заканчивается **SUCCESS**.

:::caution
Закройте workspace в Commander перед сборкой. Сам Commander может оставаться открытым, но если в workspace выполнен вход, TCShell войти не сможет, и сборка поведёт себя странно.
:::

## Где это применимо

Всё, что скрипт умеет в Commander, умеет и задание: запускать тесты или любую другую задачу TCShell. Планирование задания из Jenkins — CI-эквивалент [планирования через Планировщик заданий Windows](/ToscaBase/ru/execution/scheduling-executions/).
