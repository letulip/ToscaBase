---
title: "Препятствия: таблицы"
description: Псевдотаблицы из div, «плавающие» строки, перетаскивание строк в другую таблицу по порядку, подсчёт строк, значение последней строки, поиск по ячейкам, заголовки строк и столбцов, выпадающие списки внутри ячеек.
level: 3
sidebar:
  order: 20
sources:
  - id: k6AQZELm3H4
    title: "Tosca Tutorial | Lesson 109 - Not a Table | Dynamically changing Table Element | Obstacle 3"
    url: https://www.youtube.com/watch?v=k6AQZELm3H4
    at: "02:16"
  - id: dWayq96UL1M
    title: "Tosca Tutorial | Lesson 111 - Complex Table Interactions | Dynamic Rows | Obstacle 5"
    url: https://www.youtube.com/watch?v=dWayq96UL1M
    at: "02:14"
  - id: vjxpW60gvXs
    title: "Tosca Tutorial | Lesson 115 - Drag and Drop Table Rows | Repetition | Obstacle 9 |"
    url: https://www.youtube.com/watch?v=vjxpW60gvXs
    at: "01:13"
  - id: GeBgfUdwM-E
    title: "Tosca Tutorial | Lesson 124 - Count Number of Rows | Dynamic Web Table | RowCount | Obstacle 18"
    url: https://www.youtube.com/watch?v=GeBgfUdwM-E
    at: "02:15"
  - id: 2cSYF98wQb8
    title: "Tosca Tutorial | Lesson 125 - Get Last Table Row Value | LastContentRow | Obstacle 19"
    url: https://www.youtube.com/watch?v=2cSYF98wQb8
    at: "02:18"
  - id: WMatBr3w8UI
    title: "Tosca Tutorial | Lesson 127 - Search Table Cell Value | Constraint Action Mode | Obstacle 21"
    url: https://www.youtube.com/watch?v=WMatBr3w8UI
    at: "02:16"
  - id: ULBjqXHmDjs
    title: "Tosca Tutorial | Lesson 128 - Meeting Scheduler Table | Buffer Action Mode | Obstacle 22"
    url: https://www.youtube.com/watch?v=ULBjqXHmDjs
    at: "03:20"
  - id: UQpoXy-e3no
    title: "Tosca Tutorial | Lesson 129 - Dropdown Table | Dynamic XBuffer | Embedded Controls | Obstacle 23"
    url: https://www.youtube.com/watch?v=UQpoXy-e3no
    at: "03:16"
  - id: 4gM7fyyRJpE
    title: "TRICENTIS Tosca 16.0 - Lesson 45 | OBSTACLE#3 | Dynamically changing Table Elements – Not a Table |"
    url: https://www.youtube.com/watch?v=4gM7fyyRJpE
    at: "01:14"
  - id: vPB8nzD54Hs
    title: "TRICENTIS Tosca 16.0 - Lesson 47 | OBSTACLE#5 | Complex Table Interactions | Dynamic Rows |"
    url: https://www.youtube.com/watch?v=vPB8nzD54Hs
    at: "01:15"
  - id: 6sOxIsT81YI
    title: "TRICENTIS Tosca 16.0 - Lesson 37 | Drag & Drop Operations | Web Table | Repetition |"
    url: https://www.youtube.com/watch?v=6sOxIsT81YI
    at: "01:19"
  - id: IasTOBRqL2Y
    title: "TRICENTIS Tosca 16.0 - Lesson 51 | OBSTACLE #9 | Drag & Drop Dynamic WebTable Rows | Repetition |"
    url: https://www.youtube.com/watch?v=IasTOBRqL2Y
    at: "01:15"
  - id: 3m45f0Yu9G8
    title: "TRICENTIS Tosca 16.0 - Lesson 60 | OBSTACLE #18 | Dynamic Web Table | Count Number of Rows| RowCount"
    url: https://www.youtube.com/watch?v=3m45f0Yu9G8
    at: "01:15"
  - id: fWUEjwHsCls
    title: "TRICENTIS Tosca 16.0 - Lesson 61 | OBSTACLE #19 | Get Last Table Row Value | LastContentRow"
    url: https://www.youtube.com/watch?v=fWUEjwHsCls
    at: "01:14"
  - id: iYsG4hbu7sw
    title: "TRICENTIS Tosca 16.0 - Lesson 63 | OBSTACLE #21 | Search Table Cell Value | Constraint Action Mode"
    url: https://www.youtube.com/watch?v=iYsG4hbu7sw
    at: "01:13"
  - id: iOh_KgFyhWU
    title: "TRICENTIS Tosca 16.0 - Lesson 64 | OBSTACLE #22 | Table Search | Dynamic Table | Buffer Action Mode"
    url: https://www.youtube.com/watch?v=iOh_KgFyhWU
    at: "01:12"
  - id: NKe6fY6ffWE
    title: "TRICENTIS Tosca 16.0 - Lesson 68 | OBSTACLE #26 | Dropdown Table |Dynamic XBuffer |Embedded Controls"
    url: https://www.youtube.com/watch?v=NKe6fY6ffWE
    at: "01:13"
---

Большинство реальных проблем управления живёт в веб-таблицах: строки меняют позицию между загрузками страницы, число строк неизвестно, «таблица» оказывается набором `div`, или контрол находится внутри ячейки, а XScan поместил его вне строки. Набор инструментов невелик: ActionMode `Constraint` (ограничение) для выбора строки, `Buffer` для чтения ячейки, свойства `RowCount`, `ColumnCount` и `ResultCount`, селекторы строк вроде `$last`, `{XB[...]}`, встроенные контролы и свойство папки `Repetition` (повторение). Базовые понятия — в [Табличных контролах](/ToscaBase/ru/modules/table-controls/) и [ActionModes](/ToscaBase/ru/test-cases/action-modes/). Сравнение всей таблицы с сохранённым снимком (препятствие 34 серии Tosca 16) описано в [Сравнении таблицы с baseline](/ToscaBase/ru/modules/table-baseline-comparison/).

Рутина для каждого препятствия: отсканировать Module в папку *Obstacles*, создать TestCase с именем препятствия, перетащить в него Module, поставить workstate *Completed*, запустить в ScratchBook. Серия Tosca 16 (уроки 45–68; *Drop-down table* там — препятствие 26) решает каждое так же; дополнительные детали отмечены по месту.

## Не таблица (препятствие 3)

**Проблема.** Клик по *Generate order ID* добавляет номер заказа в блок, похожий на таблицу, в случайную строку. Номер нужно забуферизовать и ввести в текстовое поле.

**Причина.** XScan не показывает ни строк, ни ячеек: «таблица» — вложенные `div`, а у `div` с номером заказа нет ничего отличительного, кроме динамического `InnerText`.

**Решение.**

1. Поднимайте уровень **filtered items**, пока не появится `div` с номером заказа.
2. Снимите `InnerText`, переключитесь на *Identify by anchor* (по якорю) и перетащите `div` со статической подписью *Order ID* в слот anchor: подпись остаётся рядом с номером, где бы ни оказалась строка ([Идентификация контролов](/ToscaBase/ru/modules/control-identification/)).
3. Понизьте уровень фильтра, добавьте ссылку *Generate order ID* и текстовое поле, переименуйте атрибут номера в `Order ID`.
4. TestCase: ссылка → `X`; `Order ID` → свойство `InnerText`, ActionMode `Buffer`, значение `orderId`; текстовое поле → `{B[orderId]}`.

## Сложные взаимодействия с таблицей (препятствие 5)

**Проблема.** Нажать кнопку *Edit* в строке *John Doe*. Каждое обновление перемешивает строки, и в двух строках имя *John*.

**Причина.** Индекс строки ничего не значит, а XScan помещает отсканированную кнопку *Edit* вне строки.

**Решение.**

1. Отсканируйте таблицу и одну кнопку *Edit* (на *not unique* не обращайте внимания) и сделайте её [встроенным контролом](/ToscaBase/ru/modules/table-controls/#встроенные-контролы-внутри-таблицы) строки.
2. TestCase: в строке ячейка *First name* = `John` и ячейка *Last name* = `Doe`, обе с ActionMode `Constraint` (одного мало — *John* встречается дважды); *Edit* → `X`. Два Constraint отфильтровывают ровно одну строку независимо от позиции; клик попадает в кнопку этой строки.

## Список дел (To-do list, препятствие 9)

**Проблема.** Две таблицы — *To-do tasks* и *Completed tasks*. Перетащить каждую строку первой таблицы во вторую в порядке столбца *ID* (от 1 до 6).

**Причина.** Одиночное перетаскивание — это `{DRAG}` плюс `{DROP}`, как в разделе [Перетаскивание картинки](/ToscaBase/ru/troubleshooting/obstacles-input-and-clicks/#перетаскивание-картинки-drag-and-drop-image-препятствие-8); сложность в том, чтобы повторить его шесть раз, каждый раз для другой строки, без шести копий TestStep.

**Решение.**

1. Module: обе таблицы.
2. TestCase: в *To-do tasks* выберите столбец *ID*, значение ячейки `1`; строка → `{DRAG}` (ActionMode `Input`); таблица *Completed tasks* → `{DROP}` (тоже `Input`), без строки и столбца, чтобы строка попала в таблицу целиком. Запустите один раз и убедитесь, что одна строка переносится.
3. Перенесите TestStep в папку `Repetition` и задайте папке свойство [Repetition](/ToscaBase/ru/test-cases/repetitions/) равным `6`.
4. Замените `1` на `{REPETITION}` — номер текущего прохода (1, 2, ...): на каждом проходе адресуется строка, чей ID равен этому номеру, и строки переносятся по порядку; в логе каждый проход показан отдельно. В роли *ID* подойдёт любой уникальный столбец с номерами от 1 до *n*.

:::note
Субтитры искажают имя; правильно — `{REPETITION}`. Ни один урок не говорит, какой ActionMode у ячейки *ID*; естественный вариант — `Constraint` (препятствие 5). `{DROP}` с ActionMode `Verify` по умолчанию падает с ошибкой *could not find table* (урок 37).
:::

## Много строк (препятствие 18)

**Проблема.** Посчитать строки таблицы, ввести число в *Row count*, нажать кнопку. После каждого клика размер таблицы меняется.

**Причина.** Число строк известно только во время выполнения; статическое число не подходит.

**Решение.** У табличного контрола есть свойство `RowCount` (и `ColumnCount`). Module: таблица, текстовое поле, кнопка. Таблица → свойство `RowCount`, ActionMode `Buffer`, значение `rows`; текстовое поле → `{B[rows]}`; кнопка → `X`.

## Последняя строка (препятствие 19)

**Проблема.** Проверить, что в последней строке есть значение заказа, и скопировать его в текстовое поле; ни значение, ни число строк не постоянны.

**Причина.** Индекс «последней строки» меняется.

**Решение.** В атрибуте строки выберите селектор из выпадающего списка вместо номера: `$last` выбирает последнюю строку (`$lastContentRow` здесь делает то же и требует у строки ActionMode `Select`). Ячейка *Value* → ActionMode `Buffer`, значение `b_val`; текстовое поле → `{B[b_val]}`. В списке также есть `$1`, `$n`, строка заголовка и первая пустая строка, так что позиция нигде не зашита.

## Поиск по таблице (препятствие 21)

**Проблема.** Динамическая таблица; узнать, содержит ли какая-либо ячейка значение `15`, и ввести `true` или `false` в текстовое поле.

**Причина.** Значение может оказаться в любой строке и любом столбце — или отсутствовать.

**Решение.**

1. Module: таблица и текстовое поле.
2. TestCase: в строке задайте ячейке `15` с ActionMode `Constraint`; Tosca отфильтрует строки до той, где эта ячейка есть, в любом столбце.
3. Строка → свойство `Exists`, ActionMode `Buffer`, значение `b_exists`: `True`, если строка по Constraint найдена, иначе `False`.
4. Текстовое поле → `{B[b_exists]}`.

Constraint плюс `Exists` — самый быстрый поиск по всей таблице.

## Планировщик встреч (препятствие 22)

**Проблема.** Расписание: время в заголовках строк, дни недели в заголовках столбцов. Прочитать статус (*open* / *closed*) для четверга, 11–13, и ввести его в текстовое поле.

**Причина.** Никакой; строка и столбец заданы, новое здесь только адресация ячейки по заголовкам.

**Решение.**

1. Module: расписание и поле результата.
2. Атрибут строки: введите текст заголовка строки (`11 - 13`, как на странице), ActionMode `Select`; Tosca выберет строку по этому тексту, пока он уникален.
3. Ячейка: выберите столбец `Thursday` из заголовков, ActionMode `Buffer`, значение `b_status`.
4. Текстовое поле → `{B[b_status]}` с `Input` (урок 128 использует `{SENDKEYS "{B[b_status]}"}`; работают оба варианта).

:::note
Динамическое время пришлось бы сначала буферизовать или наложить на него Constraint; автор упоминает это, но не показывает.
:::

## Таблица с выпадающими списками (препятствие 23)

**Проблема.** В каждой строке задание вроде *Select the word that starts with letter M* и выпадающий список; *Generate* меняет буквы. Для каждой строки выбрать единственное подходящее слово, затем *Submit*.

**Причина.** Буква неизвестна до выполнения, и XScan помещает отсканированный `select` вне строки.

**Решение.**

1. Нажмите *Generate* до сканирования, чтобы выпадающие списки существовали. Module: *Generate*, *Submit*, таблица и один выпадающий список (не уникален — нормально); перетащите `select` внутрь ячейки — он станет [встроенным контролом](/ToscaBase/ru/modules/table-controls/#встроенные-контролы-внутри-таблицы), присутствующим в каждой строке.
2. TestCase:
   - *Generate* → `X`.
   - Строка `$2` (строка 1 — заголовок). Первая ячейка → ActionMode `Verify`, значение: постоянный текст плюс `{XB[letter]}`, который сразу верифицирует фиксированную часть и сохраняет меняющуюся букву в `letter` ([Buffers](/ToscaBase/ru/data-and-parameters/buffers/)).
   - Вторая ячейка → ActionMode `Select` (по умолчанию `Verify`). Вложенный список → `{B[letter]}*`: слово, начинающееся с этой буквы.
   - Скопируйте блок строки для строк `$3`–`$6`, меняя только номер строки; каждая строка перезаписывает тот же буфер.
   - *Submit* → `X`.
