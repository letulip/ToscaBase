---
title: Модули Test Data Service
description: Стандартные модули, управляющие Test Data Services из TestCase (Create and Provide New Item, Find and Provide Item, Update Item, Move Item to Type, Delete Item, Expert Module), поток create-find-update, чтение элементов через {TDS[тип.атрибут]} и массовая генерация данных случайными значениями и Repetitions.
level: 2
sidebar:
  order: 50
sources:
  - id: Eli2iucdQ_s
    title: "Tosca Tutorial | Lesson 154 - Test Data Management with Tosca | Test Data Services | TDS Modules |"
    url: https://www.youtube.com/watch?v=Eli2iucdQ_s
    at: "22:27"
---

Test Data Services задуманы для управления из TestCase, чтобы данные существовали до запуска кейсов, которым они нужны. Поиск `test data` в **Add TestStep** выводит стандартные модули TDS из Standard subset. Эта страница проходит по ним в порядке, в котором их использует реальный поток. Концепция, веб-интерфейс и два обязательных Test Configuration Parameter (`TestDataEndpoint`, `TestDataRepository`) — в [Test Data Services](/ToscaBase/ru/data-and-parameters/test-data-services/); без этих параметров каждый модуль ниже падает.

## Модули

| Модуль | Назначение |
|---|---|
| **Create and Provide New Item** | Создаёт элемент в типе (создавая тип, если его нет) и *предоставляет* его последующим шагам |
| **Find and Provide Item** | Выбирает существующий элемент по фильтру или запросу и предоставляет его |
| **Update Item** | Меняет атрибуты предоставленного элемента |
| **Update Type** | Меняет тип |
| **Move Item to Type** | Переносит предоставленный элемент из одного типа в другой |
| **Delete Item** | Удаляет предоставленный элемент (только его) |
| **Import Items**, **Export Items** | Импорт и экспорт файлов, как в веб-интерфейсе |
| **Expert Module** | Один модуль с папкой *Test Data Task*, покрывающий всё выше плюс задачи, доступные только здесь |

Общие ModuleAttributes: **existing or new TDS type** (после первого успешного прогона выпадающий список показывает известные типы), необязательное **alias name**, **data structure**, куда добавляется по паре атрибут-значение на столбец, а для операций поиска — **position** (первый, случайный; по умолчанию 1), **TDQL query** и **sort**.

:::caution
Модули образуют **поток**: каждый шаг передаёт предоставленный элемент в памяти следующему. `Update Item`, `Move Item to Type` и `Delete Item` падают с ошибкой *no available test data was found*, если до них ничего не предоставлено или фильтр поиска ничего не нашёл. Запускайте шаги вместе, а не по отдельности.
:::

## Шаг 1: создать элемент

Добавьте **Create and Provide New Item**, задайте тип (`Vehicle`), затем добавьте атрибуты и значения в data structure: `Make` = `BMW`, `Engine`, `DOM` = `01/01/2014`, `Seats` = `4`, `FuelType`, `Price`, `Mileage` = `1000` — по полям формы автомобиля. Добавьте и пользовательский атрибут **`Status`** = `new`: это поле отслеживает, использован ли уже элемент.

Запустите в ScratchBook. В логе ничего особенного; проверяйте, обновив тип на странице сервера, где появляется новая строка. Смена типа на `Automo` и марки на `Audi` с повторным запуском добавляет строку уже в тот тип, так что один модуль и создаёт типы, и наполняет существующие.

## Шаг 2: найти элемент

**Find and Provide Item** с типом `Vehicle`. В data structure введите `Status` = `new`; как только значение введено, ActionMode автоматически переключается на `Constraint`, потому что атрибут — фильтр, а не ввод. Предоставляются только элементы со статусом `new`.

Чтобы увидеть найденное, добавьте следом `TBox Set Buffer` с буфером `status` и значением `{TDS[vehicle.status]}`; лог покажет буфер со значением `new`. Выражение `{TDS[тип.атрибут]}` — способ, которым шаги потребляют элемент: `{TDS[vehicle.engine]}`, `{TDS[vehicle.dom]}` и так далее идут прямо в значения `Input` формы. См. [Буферы](/ToscaBase/ru/data-and-parameters/buffers/).

Альтернатива — фильтр **TDQL query**, читающийся как SQL: `vehicle[make=="BMW"]` выбирает элемент BMW. TestCase проходит без видимого вывода, что показывает совпадение запроса.

:::note
В транскрипте запрос произнесён как «vehicle, квадратная скобка, make равно равно BMW»; нужны ли кавычки вокруг значения, на слух не понять. Попробуйте оба варианта.
:::

## Шаг 3: обновить состояние

**Update Item** с alias `Vehicle` и `Status` = `used` в data structure меняет предоставленный элемент. После совместного запуска create, find и update на странице сервера элемент показан со статусом `used`. Это цикл отслеживания: найти данные `new`, использовать их в приложении, пометить `used`, чтобы следующий прогон их не взял.

## Шаг 4: перенести элемент в следующий процесс

Когда данные должны идти дальше в другое приложение (скажем, расчёт цены в бэкенде), держите по типу на процесс и переносите элемент: **Move Item to Type** принимает исходный тип (`Vehicle`) и целевой (`PriceOption`, существующий или новый). Ему нужен предоставленный элемент, поэтому сначала запустите **Find and Provide Item**; если тот шаг всё ещё фильтрует по `new` после того, как элемент стал `used`, ничего не найдётся и перенос упадёт. Запуск всего потока с создания проходит, и на странице сервера появляется новый тип `PriceOption` с перенесённым элементом.

## Шаг 5: удалить использованные данные

**Delete Item** с alias `Vehicle` удаляет текущий предоставленный элемент, а не весь тип. Поменяйте фильтр предыдущего поиска на `Status` = `used`, и пара «найти, затем удалить» вычищает использованные данные.

## Expert Module

**Expert Module** содержит папку *Test Data Task* с create, find, update, delete и дополнительно **assign read-only**, **delete type**, **delete all** (не рекомендуется: удаляет всё), **lock item / unlock item**, **lock type / unlock type**. Принимает те же входы (тип, position, data structure или query, sort). Используйте его, если предпочитаете один модуль для всех задач или нужны дополнительные.

## Данные TDS в реальном TestCase

В видео шаблон TestCase-Design копируется в обычный TestCase (`Verify mobile automation insurance - TDS`), и внутри папки pre-processing добавляется папка `Prepare test data` с **Create and Provide New Item** и **Find and Provide Item** (`Status` = `new`). TestStepValue, которые раньше приходили из TestSheet, заменяются на `{TDS[vehicle.engine]}`, `{TDS[vehicle.mileage]}` и так далее. С двумя TCP, скопированными на папку, запуск pre-processing, навигации и блока *enter vehicle data* заполняет форму из TDS. Откуда данные берутся изначально (база, бизнес-аналитики, команда ручного тестирования), не важно; TDS ими управляет.

## Массовые данные через случайные значения и Repetitions

1. В **Create and Provide New Item** замените фиксированные значения случайными выражениями ([Случайные значения](/ToscaBase/ru/expressions/random-values/)): трёхзначное случайное число для двигателя, одна цифра для мест, четыре для цены, три для пробега. Значения, которые должны совпадать с выпадающим списком (`Make`), остаются фиксированными.
2. Откройте **Properties** папки `Prepare test data` и установите **Repetition** в `10` ([Repetitions](/ToscaBase/ru/test-cases/repetitions/)).

Один прогон создаёт в типе десять элементов с разными данными. Как генерировать данные — ваш выбор; TDS — место, где ими управляют.

## Смежное

- [Test Data Services](/ToscaBase/ru/data-and-parameters/test-data-services/): концепция, веб-интерфейс, предпосылки
- [Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/)
- [Операции с буферами](/ToscaBase/ru/standard-modules/buffer-operations/)
