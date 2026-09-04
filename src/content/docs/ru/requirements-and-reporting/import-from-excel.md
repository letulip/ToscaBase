---
title: Импорт структуры папок из Excel
description: Постройте дерево папок TestCase или компонента в Excel и вставьте его в Tosca Commander через Create Folder Structure, соблюдая правило «столбец на уровень».
level: 3
sidebar:
  order: 40
sources:
  - id: ob-ktPgLPIA
    title: "Tosca Tutorial | Lesson 74 - Import Folder Structures from Microsoft Excel Sheet |"
    url: https://www.youtube.com/watch?v=ob-ktPgLPIA
    at: "00:09"
---

Если структура тестов уже существует в Microsoft Excel (тест-план, унаследованный реестр тест-кейсов, схема папок нового проекта), не нужно воссоздавать папки по одной в Tosca Commander. Скопируйте ячейки, и Commander создаст всё дерево одним действием. Это импорт только структуры: создаются папки, а не TestCase (тест-кейсы) или TestStep.

## Пример структуры

В уроке используется демо-приложение страхования автомобилей и рекомендуемая схема pre-processing / process / post-processing (см. [Структура тест-кейсов](/ToscaBase/ru/best-practices/test-case-structure/)):

```
Vehicle Insurance Offer
    Pre-processing
        Open Application
    Process
        Select Vehicle Data
        Enter Vehicle Data
        Enter Personal Data
        Enter Insurance Data
        Choose Product
        Premium Calculation
        Check Premiums
    Post-processing
        Close Application
```

На листе имя корня стоит в столбце A, `Pre-processing`, `Process` и `Post-processing` — в столбце B, их дочерние элементы — в столбце C, а более глубокий уровень — в столбце D.

## Правила для листа

- Объекты расположены **иерархически по столбцам слева направо**: родитель в крайнем левом столбце, каждый дочерний уровень на столбец правее.
- **Объекты одного уровня находятся в одном столбце.**
- **Одно значение в строке.** Строка никогда не содержит два имени.
- **Меньше 15 уровней.**

Если нарушить любое правило, структура импортируется не так, как задумано.

## Шаги импорта

1. В Excel выделите все строки структуры и нажмите **Ctrl+C**.
2. В Tosca Commander создайте или выберите целевую папку. Подойдёт любая (например, папка TestCases), но рекомендуемая цель — **component folder** (папка компонента), например `Import from Excel`.
3. Правой кнопкой по папке **> Create Folder Structure**. Commander строит дерево из скопированных ячеек.
4. Правой кнопкой **> Expand All**, чтобы проверить результат: все папки с листа существуют и вложены строго по столбцам.

:::note
Спикер упоминает горячие клавиши для этого действия и называет их Ctrl+N и Ctrl+S; субтитры в этом месте нечёткие, поэтому при сомнении используйте пункт контекстного меню.
:::

:::caution
Соседние папки могут оказаться не в том порядке, что на листе (например, `Process` перед `Pre-processing`). Переупорядочьте их вручную после импорта.
:::

## Когда это полезно

- Миграция реестра тестов, который до Tosca вёлся в Excel.
- Быстрое создание скелета папок нового проекта из тест-плана.
- Импорт согласованной с бизнесом структуры в стиле требований, которую затем наполняют тест-кейсами и привязывают к [требованиям](/ToscaBase/ru/requirements-and-reporting/requirements-and-risk/).
