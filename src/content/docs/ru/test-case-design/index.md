---
title: Дизайн тест-кейсов
description: Моделирование тестовых данных в TestSheet с атрибутами, экземплярами и классами и генерация TestCase из шаблонов.
level: 2
sidebar:
  order: 0
---

Раздел **TestCase-Design (дизайн тест-кейсов)** — место, где Tosca отделяет тестовые данные от TestCase. Сценарий описывается как TestSheet (тестовый лист) из атрибутов и их значений; значения помечаются как валидные, невалидные, straight-through или граничные, а Tosca комбинирует их в экземпляры TestCase. TestCase, преобразованный в шаблон, читает данные из листа, и инстанцирование создаёт по одному конкретному TestCase на экземпляр. Раздел описывает весь этот путь.

| Документ | Содержание |
|---|---|
| [Обзор TestCase-Design](/ToscaBase/ru/test-case-design/test-case-design-overview/) | Зачем отделять данные от TestCase, классы эквивалентности и граничные значения, объекты раздела, порядок работы |
| [TestSheet и атрибуты](/ToscaBase/ru/test-case-design/test-sheets-and-attributes/) | Папки и TestSheet, атрибуты и податрибуты, четыре рекомендуемых атрибута, свойство Business Relevant |
| [Экземпляры и комбинаторика](/ToscaBase/ru/test-case-design/instances-and-combinatorics/) | Экземпляры как значения и как TestCase, свойства Character и Position, методы all combinations / orthogonal / pairwise / linear expansion |
| [Шаблоны и инстанцирование](/ToscaBase/ru/test-case-design/templates-and-instantiation/) | Convert to Template, schema path, Check Template, привязка значений, Instantiate, условные TestStep, Reinstantiate |
| [Классы дизайна](/ToscaBase/ru/test-case-design/design-classes/) | Классы для общих атрибутов, ссылки на классы, разрешение ссылки |
| [Разбор: от начала до конца](/ToscaBase/ru/test-case-design/worked-example-end-to-end/) | Полная последовательность на примере Vehicle Insurance: от пустого листа до ExecutionList |

Читайте по порядку. Обзор даёт словарь, следующие два документа строят лист, документ о шаблонах превращает его в TestCase, классы убирают дублирование между листами, а разбор связывает всё вместе. См. также [Структура TestCase](/ToscaBase/ru/best-practices/test-case-structure/) — правило «без констант», на которое опираются шаблоны, и [Требования и риски](/ToscaBase/ru/requirements-and-reporting/requirements-and-risk/) — привязка сгенерированных TestCase к требованиям.
