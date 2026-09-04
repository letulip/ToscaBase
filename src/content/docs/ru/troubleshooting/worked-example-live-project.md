---
title: "Разбор: сквозной живой проект"
description: Завершение примера Vehicle Insurance end-to-end — условные папки шаблона, выбор тарифа из данных, WaitOn для подтверждения и отчётность из ExecutionList.
level: 3
sidebar:
  order: 50
sources:
  - id: Z_0TLCYKrBU
    title: "Tosca Tutorial | Live Project | Automate End-to-End Scenarios"
    url: https://www.youtube.com/watch?v=Z_0TLCYKrBU
    at: "00:04"
---

Этот разбор доводит демо-приложение *Vehicle Insurance* до конца сквозного сценария. Он начинается с рабочего пространства, уже построенного по лучшим практикам предыдущих сессий, и завершает последние три страницы: выбор тарифа, отправку котировки и подтверждение результата. Суть не в самих страницах, а в том, как части складываются вместе: Modules (модули), шаблон TestCase, TestSheet с атрибутами и условиями, экземпляры шаблона, ScratchBook и ExecutionList (список выполнения). У каждой техники есть свой документ; подробности — по ссылкам.

## Исходная точка

В компонентной папке *Vehicle Insurance* уже есть:

- Modules для каждой страницы (см. [Обзор Modules](/ToscaBase/ru/modules/modules-overview/)).
- TestCase design (TestSheet) с данными по автомобилю и продукту ([TestSheets и атрибуты](/ToscaBase/ru/test-case-design/test-sheets-and-attributes/)).
- Шаблон с шагами pre-processing и post-processing ([Шаблоны и инстанцирование](/ToscaBase/ru/test-case-design/templates-and-instantiation/)).
- Четыре экземпляра: один straight-through, два валидных с разными данными, один невалидный; в одном уже стоят точки верификации.
- Требования, привязанные к кейсам ([Требования и риски](/ToscaBase/ru/requirements-and-reporting/requirements-and-risk/)).

Запуск экземпляров показывает, насколько далеко идёт покрытие: ввод данных до таблицы тарифов, проверка показанных цен и выбор варианта. Осталось: проверить сгенерированный PDF (отложено), нажать *Next*, заполнить страницу *Send Quote*, нажать *Send* и проверить сообщение об успехе.

## Шаг 1: отсканировать недостающие контролы

1. Откройте Module *Select price option*, где пока только таблица тарифов, и **пересканируйте** его ([Пересканирование Modules](/ToscaBase/ru/modules/rescan-modules/)). Добавьте только ссылку *Download quote* и кнопку *Next*.
2. Отсканируйте новый Module для страницы *Send Quote* в базовом виде: поля ввода и кнопку *Send*.
3. Заполните страницу вручную, нажмите *Send*, дождитесь диалога подтверждения и отсканируйте его кнопку *OK* в отдельный Module. XScan даст ему то же имя, что и предыдущему; переименуйте в *Confirmation message*.

:::tip
Добавляйте только те контролы, которые реально использует автоматизация. Сканирование целых страниц стоит производительности и размера рабочего пространства и противоречит рекомендуемой практике ([Гигиена Modules](/ToscaBase/ru/best-practices/module-hygiene/)).
:::

## Шаг 2: тариф из данных и условные папки

Вариант для клика (Silver, Gold, Platinum, Ultimate) должен приходить из тестовых данных, а не из жёстко заданного шага.

1. В TestSheet добавьте атрибут `Price option` с четырьмя экземплярами. Заполните точки данных случайно / ортогонально, чтобы никакие два экземпляра TestCase не делили одни данные ([Экземпляры и комбинаторика](/ToscaBase/ru/test-case-design/instances-and-combinatorics/)).
2. В шаблоне создайте папку *Select price option Silver* с Module тарифов и кликом по записи Silver.
3. Поставьте **условие** на папку: `Price option` равно `Silver` **и** тип тестовых данных валидный (невалидный кейс до этой страницы не доходит). Убедитесь, что условия объединены через AND, а не OR.
4. Скопируйте папку три раза для Gold, Platinum и Ultimate; переименуйте, измените условие и замените клик.

:::caution
Когда копируете папку и перенаправляете клик, отключите или удалите исходный шаг клика. У скопированного шага по-прежнему ActionMode `Input`, и нетронутая копия всё ещё будет ожидать значение для старой записи.
:::

5. В каждую папку тарифа добавьте второй TestStep *Click next* на кнопку *Next* с тем же Module. Держите его отдельным TestStep, не сливая с шагом выбора.
6. **Check template** (без ошибок), затем **reinstantiate** экземпляры. Каждый экземпляр теперь содержит ровно одну папку тарифа: straight-through — Silver, валидные — Gold и Platinum, невалидный — ни одной.

Это ключевой паттерн: шаблон содержит все ветки, условия на папках выбирают ветку для экземпляра, а инстанцирование порождает уникальный TestCase на каждую строку данных.

## Шаг 3: отправить котировку

1. В TestSheet добавьте атрибут `Send quote` с вложенными `Email`, `Phone`, `Username`, `Password`, `Confirm password`, `Comments` и задайте им экземпляры (общий email для демо допустим; в реальных проектах будут разные пользователи). `Phone` и `Comments` на странице необязательны и остаются пустыми.
2. В шаблоне создайте папку *Send quote* с Module *Send Quote*. Каждое поле берёт значение из атрибута TestSheet; никаких статических значений в шаблоне ([Структура тест-кейса](/ToscaBase/ru/best-practices/test-case-structure/)).
3. Обусловьте папку валидными данными, как раньше.
4. Нажмите *Send*.

## Шаг 4: дождаться подтверждения, а не спать

1. Добавьте Module *Confirmation message* с кнопкой *OK*: свойство `Exists`, значение `True`, ActionMode `WaitOn`. Tosca ждёт появления диалога, сколько бы времени это ни заняло.
2. Добавьте тот же Module ещё раз как *Click OK* с `X` на кнопке.

`WaitOn` заменяет статическое ожидание; см. [Синхронизация вместо ожиданий](/ToscaBase/ru/best-practices/synchronisation-not-waits/) и [ActionModes](/ToscaBase/ru/test-cases/action-modes/).

## Шаг 5: проверить, переинстанцировать, запустить

1. Снова **Check template**, **reinstantiate**. Экземпляры получают папку *Send quote* со своими значениями.
2. Запустите один экземпляр в ScratchBook: выбирается вариант, нажимается *Next*, заполняется форма, ожидание ловит подтверждение, нажимается *OK*.
3. Синхронизируйте ExecutionList с изменёнными TestCase и запустите оттуда. Результат тот же, что в ScratchBook; разница в том, что ExecutionList хранит его с датой, временем и длительностью ([Списки выполнения](/ToscaBase/ru/execution/execution-lists/), [Результаты и логи](/ToscaBase/ru/execution/execution-results-and-logs/)).
4. Для отчётности руководству используйте **print view** ExecutionList и экспорт в Excel или PDF. Добавляйте или убирайте столбцы в ExecutionList — экспорт следует за ними; немного форматирования в Excel делает отчёт презентабельным ([Отчёты](/ToscaBase/ru/requirements-and-reporting/reports/)).

## Что осталось за кадром и куда это вставить

- **Проверка PDF** скачанной котировки показана отдельно и вставляется после *Download quote*: [PDF-движок](/ToscaBase/ru/engines/pdf-engine/).
- **Проверка email** на демо невозможна (письмо не отправляется). На реальной системе проверяйте через UI или добавьте API-шаги, если письмо уходит через API: [API TestCases](/ToscaBase/ru/api-testing/api-test-cases/).
- **Test events** для запуска на нескольких агентах требуют многопользовательского рабочего пространства: [Распределённое выполнение](/ToscaBase/ru/execution/distributed-execution-dex/).

## Практики, на которые опирается проект

- Одна **компонентная папка** на проект с Modules, TestCases, TestCase design, требованиями и ExecutionLists; несколько компонентных папок для нескольких проектов ([Структура тест-кейса](/ToscaBase/ru/best-practices/test-case-structure/)).
- **Соглашения об именовании** для Modules, TestCases и TestSteps ([Соглашения об именовании](/ToscaBase/ru/best-practices/naming-conventions/)).
- **Никаких констант** в TestCase: параметризуйте через TestSheet или Test Configuration Parameters ([Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/)).
- **Условия** на папках шаблона, чтобы каждый экземпляр был отдельным сценарием, а не тем же сценарием с другими подписями.
