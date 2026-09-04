---
title: Тест-кейсы
description: Сборка TestCase из Module - TestStep и ActionMode, условия и циклы, повторения, сценарии восстановления и очистки, рекордер и исследовательское тестирование.
level: 1
sidebar:
  order: 0
---

TestCase (тест-кейс) - это место, где Module (модули) превращаются в исполняемый тест: каждый TestStep (шаг теста) управляет контролами одного Module, а ActionMode (режим действия) на каждом значении определяет, вводит ли Tosca значение, проверяет, буферизует или ждёт его. Раздел начинается с самого объекта TestCase и справочника по ActionMode, затем описывает всё, что меняет прямой ход выполнения сверху вниз (условия, циклы, повторения, восстановление), и заканчивается двумя способами записи вместо ручной сборки.

| Документ | О чём |
|---|---|
| [Основы TestCase](/ToscaBase/ru/test-cases/test-case-basics/) | Технические и бизнес-TestCase, создание TestCase, TestStep из Module, Workstate, первый сквозной пример |
| [Режимы действия](/ToscaBase/ru/test-cases/action-modes/) | Справочник по `Input`, `Insert`, `Verify`, `Buffer`, `WaitOn`, `Select` и `Constraint` со сводной таблицей и примерами на формах и таблицах |
| [Управление потоком](/ToscaBase/ru/test-cases/control-flow/) | Операторы `If`, циклы `While` и `Do`, свойство Maximum repetitions |
| [Повторения](/ToscaBase/ru/test-cases/repetitions/) | Повторение TestStep папки фиксированное число раз через колонку или свойство Repetition |
| [Сценарии восстановления и очистки](/ToscaBase/ru/test-cases/recovery-and-cleanup-scenarios/) | Включение recovery engine, Recovery Scenario Collection, Retry level, Cleanup Scenario |
| [Рекордер](/ToscaBase/ru/test-cases/recorder/) | Генерация Module и TestCase записью действий, режим верификации, что дорабатывать после записи |
| [Исследовательское тестирование](/ToscaBase/ru/test-cases/exploratory-testing/) | Explorative session, запись документа сценария со скриншотами, экспорт в PDF |

Читайте по порядку: первые два документа - предпосылка для всего остального на сайте. Переиспользование TestStep между TestCase (библиотеки, Business Parameter) описано в разделе [Данные и параметры](/ToscaBase/ru/data-and-parameters/), а правила поддерживаемого TestCase - в [Лучших практиках](/ToscaBase/ru/best-practices/).
