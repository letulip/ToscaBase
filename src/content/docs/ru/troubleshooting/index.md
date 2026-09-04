---
title: Устранение проблем
description: Препятствия автоматизации (одинаковые ID, динамические таблицы, скрытые элементы, drag and drop) и типичные проблемы реальных проектов — проблема, причина, решение.
level: 3
sidebar:
  order: 0
---

Раздел организован по симптомам. Первые три документа проходят по *Obstacle Course* (полосе препятствий) Tricentis — публичной странице задач по автоматизации, воспроизводящих то, что ломается в реальных приложениях; каждое препятствие описано как **Проблема / Причина / Решение**. Четвёртый документ отвечает на вопросы, которые возникают в проектах, но не имеют выделенного Module. Последний — полный сквозной разбор, связывающий техники воедино.

| Документ | Что решает |
|---|---|
| [Препятствия: идентификация контролов](/ToscaBase/ru/troubleshooting/obstacles-identification/) | *Selected item is not unique*, «близнецы», ID, меняющиеся между кликами, мультиселект (cardinality, `ExplicitName`), автодополнение (`SENDKEYS`, `ResultCount`), скрытые элементы, контролы вне viewport (`ScrollingBehavior`). |
| [Препятствия: таблицы](/ToscaBase/ru/troubleshooting/obstacles-tables/) | Таблицы из `div` (идентификация по якорю), «плавающие» строки (`Constraint`), `RowCount`, `$last` / `$lastContentRow`, поиск по ячейкам через `Exists`, адресация ячеек по заголовкам строк и столбцов, выпадающие списки в ячейках с `{XB[...]}`. |
| [Препятствия: ввод и клики](/ToscaBase/ru/troubleshooting/obstacles-input-and-clicks/) | `{DRAG}` / `{DROP}`, клики до смены подписи (`While`), экранирование значений, `{CLICK}` с `OffsetHorizontal`, Module *Click On Screen*. |
| [Типичные проблемы и решения](/ToscaBase/ru/troubleshooting/common-problems-and-fixes/) | Переключение вкладок браузера через `TBox Send Keys`, подсчёт всех ссылок на странице, скачивание файла через `curl` и его проверка. |
| [Разбор: сквозной живой проект](/ToscaBase/ru/troubleshooting/worked-example-live-project/) | Завершение примера Vehicle Insurance: условные папки шаблона, выбор из данных, `WaitOn`, отчётность из ExecutionList. |

Читайте документы о препятствиях после [Идентификации контролов](/ToscaBase/ru/modules/control-identification/), [Табличных контролов](/ToscaBase/ru/modules/table-controls/) и [ActionModes](/ToscaBase/ru/test-cases/action-modes/): они опираются на эти основы и показывают их под нагрузкой.
