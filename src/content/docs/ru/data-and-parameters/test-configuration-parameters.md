---
title: Test Configuration Parameters
description: Test Configuration Parameters (TCP) хранят данные окружения и настройки вне TestStep; где их задавать, синтаксис {CP[имя]}, системные параметры и Configurations уровня проекта.
level: 2
sidebar:
  order: 20
sources:
  - id: k_paxCad6Kw
    title: "Tricentis Tosca Tutorial Part-7: Tosca Parameters,Tosca Configuration Parameter"
    url: https://www.youtube.com/watch?v=k_paxCad6Kw
    at: "01:50"
  - id: H5M6Y_Su4OQ
    title: "Tosca Tutorial | Lesson 156 - Test Configuration Parameters | Project Configurations |"
    url: https://www.youtube.com/watch?v=H5M6Y_Su4OQ
    at: "00:09"
---

**Test Configuration Parameter (параметр тестовой конфигурации, TCP)** — именованное значение, заданное на объекте Tosca, а не внутри TestStep. Шаги ссылаются на него через `{CP[имя]}`, поэтому смена значения в одном месте меняет все шаги, которые его используют. TCP — правильное место для данных, одинаковых во всём наборе, но разных между окружениями или прогонами: URL приложения, учётные данные, браузер, таймауты, пути отчётов. Жёстко прописанные значения означают правку TestCase при каждой смене данных; при тысяче шагов с одним URL это тысяча правок.

## Где живут TCP

У каждого объекта, который может нести TCP, в деталях есть вкладка **Test Configuration**: корень проекта, component folders, папки TestCase, сами TestCase, ExecutionList, папка TestCase-Design и раздел **Configurations**. Правила:

- TCP, заданный на папке, **наследуется** всеми подпапками и TestCase под ней. Общие значения задавайте как можно выше (корень или компонент), а ниже переопределяйте только при необходимости.
- Во время выполнения TCP **только для чтения**; задавайте их до запуска.
- Часть параметров **системные**, определённые Tosca (при создании они появляются в выпадающем списке), остальные — **пользовательские**, названные вами.

## Создание и использование TCP

1. Выберите TestCase (или папку, ExecutionList) и откройте вкладку **Test Configuration**.
2. Кликните правой кнопкой по объекту в верхней части вкладки и выберите **Create Test Configuration Parameter**.
3. В выпадающем списке параметров выберите системный (например `Browser`, после чего появится список значений: Chrome, Firefox, Edge, Internet Explorer и другие) или введите своё имя: `Username`, `Password`, `URL`, `MyTCP`.
4. Введите значение. **Тип данных** можно сменить; для учётных данных выберите `Password`, чтобы значение было скрыто.
5. В TestStep замените литерал на `{CP[имя]}`. При наборе `{CP[` всплывает список параметров, видимых этому TestCase.

Удалить значение из списка нельзя; используйте **Reset to default value** на параметре — это убирает его.

Кроме удобства сопровождения автор отмечает два побочных эффекта: шаги становятся **абстрактными** (читатель видит `{CP[Password]}`, а не секрет), а набор проще запускать в другом окружении. В демо имя пользователя, пароль и URL TestCase логина заменены на TCP, чтобы один и тот же кейс можно было прогнать для семи демо-пользователей без создания семи TestCase.

TCP сочетаются с другими видами параметров:

- `TBox Set Buffer` со значением `{CP[MyTCP]}` копирует конфигурационное значение в [буфер](/ToscaBase/ru/data-and-parameters/buffers/); лог ScratchBook показывает подставленное значение.
- [Business Parameter](/ToscaBase/ru/data-and-parameters/business-parameters-and-libraries/) переиспользуемого TestStepBlock можно заполнить через `{CP[SearchText]}` вместо литерала.
- Некоторые стандартные модули и Test Data Services вообще не запускаются без определённых TCP: `Browser` для [Execute JavaScript](/ToscaBase/ru/standard-modules/execute-javascript/), `TestDataEndpoint` и `TestDataRepository` для [Test Data Services](/ToscaBase/ru/data-and-parameters/test-data-services/).

## Системные параметры, которые стоит знать

Полный список — в документации Tricentis; ниже те, что выделяет видео, сгруппированные по engine.

| Engine | Параметр (как назван в видео) | Что задаёт |
|---|---|---|
| XBrowser | `Browser` | В каком браузере выполняется веб-TestCase; самый важный параметр для веб-тестов |
| XBrowser | Версия браузера | Версия этого браузера |
| XBrowser | Accessibility analysis, accessibility fast mode | Запускать ли анализ доступности и в быстром ли режиме |
| TBox | Avoid execution recorder | Включает или выключает запись выполнения для TestCase |
| TBox (recovery engine) | On dialog failure, on exception failure, on verification failure | Что Tosca делает после каждого типа сбоя |
| TBox | Page sync | Синхронизация с незавершёнными Ajax-запросами |
| TBox | Scrolling behaviour | Вертикальная или горизонтальная прокрутка |
| TBox | `SynchronizationTimeout` | Сколько Tosca ждёт контрол; имеет значение по умолчанию, которое можно переопределить |
| TBox | `TargetDateFormat`, target time format | Формат даты и времени в TestCase, см. [Выражения дат](/ToscaBase/ru/expressions/date-expressions/) |
| TBox (recovery engine) | TestStep retries, TestCase retries | Сколько раз повторяется шаг или TestCase |
| Mobile | APM server, browser, device model, device name, live view, simulator | Настройки mobile engine, разбираются в уроках по мобильному тестированию |

:::note
В транскрипте большинство параметров названы на слух («page sync», «avoid execution recorder»); только выделенные кодом встречаются в написанном виде в других местах этой базы знаний. Точные идентификаторы смотрите в выпадающем списке или документации Tricentis.
:::

## Configurations уровня проекта

Раздел **Configurations** проекта хранит переиспользуемые наборы TCP. В нём есть предустановленные (API, mobile, Test Data Service), и можно создать свою Configuration, папку конфигураций, структуру или виртуальную папку. Пример: `Project A` с `Browser` = Chrome и `SynchronizationTimeout` = 3000, `Project B` с `Browser` = Firefox и `SynchronizationTimeout` = 6000 — те же параметры с разными значениями для двух команд.

- **Применить** Configuration — перетащить её на TestCase, папку или ExecutionList. Объект наследует весь набор.
- **Заблокировать** Configuration — открыть её **Properties** и установить **Predefined** в `true`. Предопределённую Configuration нельзя изменить или удалить, только наследовать. TestCase, который её наследует, всё же может переопределить значение локально (скажем, Chrome на Edge), и это переопределение действует только в этом TestCase; оригинал не меняется. Так проектные настройки остаются под контролем администратора.

## Configuration Parameters уровня модуля — другой механизм

Модули тоже несут **Configuration Parameters** (`ExplicitName`, `ConstraintIndex` и другие), задаваемые на ModuleAttribute: они настраивают, как Tosca управляет контролом, и через `{CP[...]}` не читаются; см. [Свойства и параметры модуля](/ToscaBase/ru/modules/module-properties-and-parameters/) и, для `ExplicitName`, [Идентификацию контролов](/ToscaBase/ru/modules/control-identification/). Единственный случай, когда такой параметр управляется из TestCase через буфер (`ConstraintIndex` для двух одинаковых вкладок браузера), — рецепт в [Типичных проблемах и решениях](/ToscaBase/ru/troubleshooting/common-problems-and-fixes/#одинаковые-вкладки-браузера).

## Смежное

- [Буферы](/ToscaBase/ru/data-and-parameters/buffers/): рантайм-двойник TCP
- [Business Parameters и библиотеки](/ToscaBase/ru/data-and-parameters/business-parameters-and-libraries/)
- [Кроссбраузерное выполнение](/ToscaBase/ru/execution/cross-browser-execution/): TCP `Browser` на ExecutionList
