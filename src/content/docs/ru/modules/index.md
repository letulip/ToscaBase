---
title: Module
description: Как Tosca описывает экраны в виде переиспользуемых Module — от сканирования в XScan и уникальной идентификации контролов до свойств, параметров, таблиц и гигиены workspace.
level: 1
sidebar:
  order: 0
---

Module (модуль) — это модель одного экрана или страницы в Tosca: контролы, нужные TestCase, вместе с техническими свойствами, по которым Tosca находит их во время выполнения. Всё остальное в Tosca строится на Module, поэтому этот раздел идёт сразу после [Начала работы](/ToscaBase/ru/getting-started/). Читайте документы по порядку: каждый опирается на предыдущий.

| Документ | О чём |
|---|---|
| [Обзор Module](/ToscaBase/ru/modules/modules-overview/) | Module и ModuleAttribute, классические Module и XModule, движки и TBox, стандартные и пользовательские Module |
| [XScan](/ToscaBase/ru/modules/xscan/) | Запуск сканирования, выбор контролов на экране, сообщения unique / not unique, сохранение и check-in |
| [Идентификация контролов](/ToscaBase/ru/modules/control-identification/) | Identify by properties, anchor, image и index — именно в этом порядке — и `ExplicitName` для выбора контрола из TestCase |
| [Пересканирование Module](/ToscaBase/ru/modules/rescan-modules/) | Повторное открытие Module в XScan, чтобы добавить свойства или контролы, и починка использующих его TestCase |
| [Дубликаты и слияние Module](/ToscaBase/ru/modules/duplicate-and-merge-modules/) | Поиск дубликатов и Module merge assistant |
| [Свойства и параметры Module](/ToscaBase/ru/modules/module-properties-and-parameters/) | Cardinality, business type, synchronization policy, а также configuration, identification, steering и transition parameters |
| [Табличные контролы](/ToscaBase/ru/modules/table-controls/) | Строки, столбцы и ячейки, селекторы, свойства таблицы, примеры steering, встроенные контролы, число строк и столбцов |
| [Сравнение таблицы с baseline](/ToscaBase/ru/modules/table-baseline-comparison/) | Снимок таблицы и проверка последующих выполнений по нему |

Смежное: реальные случаи, когда идентификация ломается, собраны в разделе [Устранение проблем](/ToscaBase/ru/troubleshooting/), а причины держать Module маленькими и уникальными — в [Гигиене Module](/ToscaBase/ru/best-practices/module-hygiene/). Module, поставляемые вместе с Tosca, описаны в [Стандартных Module](/ToscaBase/ru/standard-modules/).
