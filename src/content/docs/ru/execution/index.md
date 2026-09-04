---
title: Выполнение
description: Запуск TestCase через ExecutionList, чтение и архивирование результатов, ручные и записанные прогоны, планирование, интеграция с CI и распределённое выполнение на DEX-агентах.
level: 2
sidebar:
  order: 0
---

Раздел **Execution** workspace — место, где запускаются готовые TestCase и где живут их результаты. Этот раздел начинается с базовой единицы, ExecutionList (списка выполнения), затем переходит к работе с результатами, вариантам прогона (ручной, повторный, записанный, задокументированный, мультибраузерный) и, наконец, к выносу прогона за пределы Commander: по расписанию, из CI-сервера или на DEX-агенты.

| Документ | О чём |
|---|---|
| [ExecutionList](/ToscaBase/ru/execution/execution-lists/) | ScratchBook и ExecutionList, создание и запуск списков, синхронизация с TestCase |
| [Результаты и логи](/ToscaBase/ru/execution/execution-results-and-logs/) | Опции представления ActualLog, трендовые диаграммы, очистка и архив, копирование в Excel, LogViewer |
| [Ручное выполнение](/ToscaBase/ru/execution/manual-execution/) | Run as manual TestCase с окном чек-листа, установка результата вручную |
| [Repetitions и бизнес-TestCase](/ToscaBase/ru/execution/execution-repetitions-and-business-test-cases/) | Repetitions у execution entry, business TestCase и business ExecutionList |
| [Запись выполнения](/ToscaBase/ru/execution/recording-executions/) | Настройка Execution Recorder (MP4), параметр AvoidExecutionRecorder |
| [DokuSnapper](/ToscaBase/ru/execution/dokusnapper/) | Сгенерированный документ с логом и скриншотом на каждый TestStep |
| [Кросс-браузерное выполнение](/ToscaBase/ru/execution/cross-browser-execution/) | Параметр Browser из Buffer, ошибка «No feasible executor found» |
| [Планирование выполнения](/ToscaBase/ru/execution/scheduling-executions/) | Скрипт TCShell, bat-файл, Планировщик заданий Windows |
| [Интеграция с Jenkins](/ToscaBase/ru/execution/ci-integration-jenkins/) | Freestyle-задание, запускающее bat-файл с TCShell |
| [Распределённое выполнение (DEX)](/ToscaBase/ru/execution/distributed-execution-dex/) | Workspace AOS, DEX-агент, Configurations, TestEvent |
| [Tosca Execution Client](/ToscaBase/ru/execution/tosca-execution-client/) | Запуск TestEvent из PowerShell, shell или Jenkins |

Прочитайте первые два раньше остальных; каждый следующий документ предполагает, что вы умеете создать список и прочитать его лог. Recovery и Cleanup Scenarios (сценарии восстановления и очистки), реагирующие на сбои во время прогона, описаны в [Тест-кейсах](/ToscaBase/ru/test-cases/recovery-and-cleanup-scenarios/).
