---
title: Excel engine
description: Сравнение двух книг модулем Excel 1:1 File Compare и создание, заполнение, проверка и чтение листов Excel стандартными модулями TBox Excel - открытие, лист, диапазон, манипуляция, закрытие, число строк и столбцов.
level: 3
sidebar:
  order: 10
sources:
  - id: idPsLArM3zc
    title: "Tosca Tutorial | Lesson 19 - Compare Two Excel Files | TBox Automation Module | Excel Engine"
    url: https://www.youtube.com/watch?v=idPsLArM3zc
    at: "02:11"
  - id: hi0GA1Dg1Nc
    title: "Tosca Tutorial | Lesson 20 - Create, Open, Modify & Delete Excel Workbook | Excel Engine"
    url: https://www.youtube.com/watch?v=hi0GA1Dg1Nc
    at: "01:09"
  - id: 4V0ygehvBAk
    title: "Tosca Tutorial | Lesson 21 - Verify RowCount & ColumnCount of Excel WorkBook | Excel Engine"
    url: https://www.youtube.com/watch?v=4V0ygehvBAk
    at: "01:09"
---

Excel engine (движок Excel) поставляется как семейство стандартных модулей TBox, так что сканировать нечего и библиотеки ставить не нужно: найдите в Modules по запросу `TBox Excel` и получите модули для сравнения двух файлов, открытия или создания книги, добавления листов, определения диапазона ячеек, чтения, записи, буферизации и проверки ячеек, запуска макросов и закрытия или сохранения книги. Любой TestCase (тест-кейс) с книгой строится по одной схеме: открыть, определить диапазон, изменить диапазон, закрыть.

## Стандартные модули Excel

| Module | Роль |
|---|---|
| **TBox Excel 1:1 File Compare** | Сравнивает две книги лист за листом и сообщает о несовпадающих ячейках |
| **TBox Open Excel Workbook** | Открывает существующую книгу или создаёт новую |
| **TBox Create Excel Worksheet** | Добавляет лист в открытую книгу |
| **TBox Define Excel Range** | Именует блок ячеек; обязателен перед любой манипуляцией |
| **TBox Excel Range Manipulation** | Вводит, буферизует и проверяет ячейки и свойства определённого диапазона |
| **TBox Close Excel Workbook** | Закрывает книгу, при необходимости сохраняя под новым именем или в другом формате |
| **TBox Run Excel Macro** | Запускает макрос из книги |
| **TBox Clear Excel Range** | Очищает значения, ранее введённые в диапазон |
| **TBox Delete Excel Worksheet**, **TBox Update Excel Worksheet** | Удаляют или изменяют листы в многолистовых книгах |

:::caution
Во время выполнения TestCase книга не должна быть открыта в Excel, иначе шаг Open падает. Сначала закройте Excel, при необходимости сохранив файл.
:::

## Сравнение двух книг

`TBox Excel 1:1 File Compare` стоит рядом с модулями сравнения файлов, картинок и [PDF](/ToscaBase/ru/engines/pdf-engine/). Его атрибуты:

| Атрибут | Значение |
|---|---|
| Reference file | Полный путь к эталонной книге, включая `.xlsx` |
| Target file | Полный путь к сравниваемой книге |
| Reference password, Target password | Только для защищённых файлов |
| Include cells data, Include formats, Include objects | Булевы флаги, добавляющие в сравнение значения ячеек, форматирование и объекты; необязательны |
| Include sheets | Имена сравниваемых листов через точку с запятой. Лист, не указанный здесь, **не** сравнивается |
| Output path | Текстовый файл (например `results.txt`), куда пишутся расхождения. При совпадении файлов ничего не пишется |

Пример: в `users.xlsx` и `users1.xlsx` есть лист `Email` со списком адресов; в целевом файле одного адреса нет. Запуск в ScratchBook: шаг падает, в логе названы оба файла и расхождение: лист `Email`, ячейка `A49`, эталонное значение `test@gmail.com`, в целевом файле значения в `A49` нет. Те же строки записаны в выходной файл для отчётности. Время сравнения зависит от объёма данных.

## Создание и заполнение книги

TestCase `Create Excel` создаёт `emp.xlsx` с листом, содержащим заголовок, двух сотрудников с зарплатами и итог.

1. **TBox Delete File** удаляет прежнюю копию файла, чтобы прогон был повторяемым.
2. **TBox Open Excel Workbook**: `Workbook name` — имя, которое используют все последующие шаги (`EmployeeData`), `Path` — файл (`C:\training\emp.xlsx`), `Create new` — `True` для создания файла или `False` для открытия существующего. `Password` и `Read only` (`True`/`False`) необязательны.
3. **TBox Create Excel Worksheet**: тот же `Workbook name`, `Worksheet name` (`EMP`) и `Worksheet order`, который ставит лист `first`, `last` или на заданную позицию.
4. **TBox Define Excel Range**: `Range name` (`EmployeeData`), имена книги и листа, начальная ячейка (`A1`) и конечная (`B4`). Диапазон — это то, чем управляют последующие шаги, как выделение ячеек в Excel. Если записей может быть больше, задайте конечную ячейку с запасом, например строку 50 для 49 записей.
5. **TBox Excel Range Manipulation** с `Range name` `EmployeeData`. Его таблица данных повторяет диапазон: первая строка помечена как заголовок и получает `Full name` и `Salary`; следующие строки несут значения. У каждой ячейки свой ActionMode (режим действия), поэтому в одном шаге зарплаты вводятся и буферизуются (`Amount1`, `Amount2`), а ячейка `Total salary` проверяется математическим выражением, суммирующим два буфера.
6. **TBox Close Excel Workbook**: `Workbook name`, `Save` (`True`/`False`), `Path` (другой путь сохраняет копию в другом месте) и `Save as type`. Список типов включает все форматы, которые умеет писать Excel, в том числе книгу, PDF, TXT и CSV, так что TestCase может сразу экспортировать лист в PDF. Тот же модуль открывает и эти другие типы.

После прогона лог показывает введённые значения, буферизованные суммы и успешную проверку итога; файл `emp.xlsx` существует с листом `EMP` и теми же данными.

:::tip
Автор проверяет итог в том же шаге манипуляции, который заполняет лист, и отмечает, что рекомендуемая структура — отдельный проверочный TestCase.
:::

:::note
В видео итог вычисляется математической функцией над `{B[Amount1]}` и `{B[Amount2]}`; точный синтаксис выражения не произнесён. См. [Expressions](/ToscaBase/ru/expressions/) о математических выражениях Tosca.
:::

## Буферизация числа строк и столбцов

Для листа из четырёх строк и двух столбцов (`EmployeeData` из примера выше):

1. Создайте TestCase `Get row count and column count` и переиспользуйте шаги **Open Excel Workbook** (`Create new` = `False`), **Define Excel Range** (те же книга, лист и имя диапазона) и **Close Excel Workbook**.
2. Добавьте **TBox Excel Range Manipulation**, перетащите его выше шага Close и переименуйте в `Get row count`. Скопируйте, вставьте ниже и переименуйте копию в `Get column count`. В обоих укажите имя диапазона `EmployeeData`; автор забыл его во втором шаге, и прогон падал, пока поле не заполнили.
3. В `Get row count` откройте таблицу данных, нажмите стрелку в ячейке **Value** и выберите свойство `RowCount`. В качестве значения введите имя буфера `RC` и задайте ActionMode `Buffer`. `RowCount` — специальное свойство, возвращающее число строк таблицы; его можно и набрать вручную.
4. В `Get column count` сделайте то же с `ColumnCount`, буфером `CC` и ActionMode `Buffer`.

Лог сообщает, что диапазон `EmployeeData` успешно обновлён, `RC` установлен в `4`, `CC` в `2`. Проверьте буферы в следующем TestStep (шаге теста), чтобы превратить чтение в проверку; это работает и для существующих книг, и для созданных ранее в том же TestCase.

## См. также

- [Buffers](/ToscaBase/ru/data-and-parameters/buffers/) и [Операции с буферами](/ToscaBase/ru/standard-modules/buffer-operations/).
- [Операции с файлами и папками](/ToscaBase/ru/standard-modules/file-and-folder-operations/): TBox Delete File и другие модули сравнения файлов.
- [Табличные контролы](/ToscaBase/ru/modules/table-controls/): `RowCount` и `ColumnCount` для таблиц приложения.
