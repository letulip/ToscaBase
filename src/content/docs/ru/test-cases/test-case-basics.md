---
title: Основы TestCase
description: Что такое TestCase в Tosca, технические и бизнес-TestCase, как TestStep собираются из Module, и первый сквозной пример с WaitOn, Input и Verify.
level: 1
sidebar:
  order: 10
sources:
  - id: TMfn5am9x-c
    title: "Tricentis Tosca Tutorial Part-5 : Tosca Test Case, Tosca Test Case Design and Best Practices"
    url: https://www.youtube.com/watch?v=TMfn5am9x-c
    at: "01:15"
---

TestCase (тест-кейс) - это набор инструкций, который проходит через приложение и проверяет результат. Он пишется по требованиям к ПО и может быть ручным или автоматизированным; в Tosca автоматизированный TestCase собирается из Module (модулей) - стандартных и пользовательских - плюс тестовых данных, которые этим Module нужны. Эта страница про сам объект: два вида TestCase, как TestStep (шаги теста) получаются из Module, и полный первый пример. Какой ActionMode (режим действия) ставить на каждое значение - тема документа [Режимы действия](/ToscaBase/ru/test-cases/action-modes/).

## Технические и бизнес-TestCase

| Вид | Что содержит | Исполняемый |
|---|---|---|
| Technical TestCase (технический) | Всю техническую информацию для управления контролами: TestStep, TestStepValue, ActionMode | Да |
| Business TestCase (бизнес) | Логическую группу технических TestCase, представляющую одну функциональность и спроектированную по требованиям | Нет, служит для мониторинга покрытия |

Всё ниже относится к техническим TestCase. Бизнес-TestCase описаны вместе с ExecutionList в документе [Повторения выполнения и бизнес-TestCase](/ToscaBase/ru/execution/execution-repetitions-and-business-test-cases/).

## Создание TestCase

1. В секции **TestCases** щёлкните правой кнопкой по папке и выберите значок создания TestCase (синяя круговая стрелка) или нажмите **Ctrl+N**, затем **Ctrl+T**.

:::note
Аккорд **Ctrl+N**, **Ctrl+T** (две клавиши подряд) создаёт TestCase; одиночный **Ctrl+T** внутри TestCase открывает поиск для добавления TestStep из Module.
:::
2. Дайте TestCase осмысленное имя. Новый TestCase пуст: в нём пока нет TestStep.
3. Перетащите Module из секции **Modules** на TestCase. Каждый перетащенный Module становится одним TestStep, а его TestStepValue - это контролы Module.
4. Для каждого нужного контрола введите значение в колонке **Value** и выберите ActionMode. Нетронутые контролы игнорируются.
5. Переименуйте каждый TestStep по выполняемому действию (например `Open Google`, `Search Tricentis Tosca`). Это необязательно, но делает лог читаемым.

:::tip
Папки необязательны, но рекомендуются: логически сгруппируйте TestCase до их создания. В общем репозитории перед созданием чего-либо нужно сделать check-out секции **TestCases** (или папки). См. [Многопользовательские workspace](/ToscaBase/ru/administration/multi-user-workspaces/).
:::

## Workstate

У TestCase три состояния: `Planned`, `In Work` и `Completed`. Состояние не декоративно - оно влияет на цифры покрытия требований. Когда какое значение ставить, объяснено в документе [Структура TestCase](/ToscaBase/ru/best-practices/test-case-structure/).

:::note
В источнике первое состояние названо «planning»; колонка Workstate в Commander показывает `Planned`. Считайте это одним и тем же значением.
:::

## ActionMode вкратце

Каждый TestStepValue несёт ActionMode, который говорит Tosca, что делать со значением:

- `Input` вводит данные или выполняет клик.
- `Insert` создаёт объекты в не-UI структурах (например, XML).
- `Verify` сравнивает свойство контрола со значением; в значении записано условие.
- `Buffer` сохраняет значение контрола в именованный буфер.
- `WaitOn` приостанавливает выполнение, пока условие в значении не выполнится (синхронизация).
- `Select` проходит по уровням иерархии до дочерних элементов, обычно строк и ячеек таблиц.
- `Constraint` ограничивает поиск элементами с определённым значением, в основном в колонках таблиц.

Полный справочник с синтаксисом и примерами - [Режимы действия](/ToscaBase/ru/test-cases/action-modes/).

## Рабочий пример: поиск в Google

Сценарий: открыть Google в Chrome, найти *Tricentis Tosca*, открыть первый результат, проверить, что появился сайт Tricentis, закрыть браузер. Три пользовательских Module уже созданы (экран поиска Google, экран результатов, портал Tricentis), в каждом только нужные контролы; как они сканировались, см. в [XScan](/ToscaBase/ru/modules/xscan/).

| # | TestStep | Module | Значения и ActionMode |
|---|---|---|---|
| 1 | Open Google | `OpenUrl` (стандартный Module, **TBox XEngines > HTML**) | URL `www.google.com`, `Input` |
| 2 | Search Tricentis Tosca | Экран поиска Google | значок Google: `Exists` = `True`, `WaitOn`; поле поиска: `Tricentis Tosca`, `Input`; кнопка поиска: клик, `Input` |
| 3 | Pause | `TBox Wait` (стандартный Module) | `5000` (миллисекунды) |
| 4 | Open first result | Экран результатов | ссылка первого результата: клик, `Input` |
| 5 | Verify Tosca official portal | Портал Tricentis | логотип: `Exists` = `True`, `Verify` |
| 6 | Close browser | `Close Browser` (стандартный Module) | заголовок `Tricentis Tosca*` |

Замечания по шагам:

- **Шаг 1.** Универсальный Module **TBox Automation Tools > Process Automation** запускает любую программу, но для веб-приложения правильный выбор - специализированный `OpenUrl`; в источнике сначала перетаскивают универсальный, потом заменяют.
- **Шаг 2.** `WaitOn` на значке Google обеспечивает синхронизацию: шаг не продолжается, пока страница не отрисует значок.
- **Шаг 3.** Автор добавляет статическое ожидание 5 с, потому что результаты поиска могут грузиться медленно при плохой сети. Так сделано в источнике, но лучшая практика Tricentis - заменять статические ожидания на `WaitOn`; см. [Синхронизация вместо ожиданий](/ToscaBase/ru/best-practices/synchronisation-not-waits/).
- **Шаг 6.** `Close Browser` находит окно по заголовку. Звёздочка - подстановочный символ: `Tricentis Tosca*` соответствует любому заголовку, начинающемуся с этого текста.
- **Браузер.** По умолчанию Tosca работает с Internet Explorer. Чтобы запускать в Chrome, добавьте на TestCase Test Configuration Parameter `Browser` со значением `Chrome`. См. [Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/).

TestCase готов к запуску из [ExecutionList](/ToscaBase/ru/execution/execution-lists/) или ScratchBook.

## Куда дальше

- [Режимы действия](/ToscaBase/ru/test-cases/action-modes/) - каждый ActionMode подробно.
- [Структура TestCase](/ToscaBase/ru/best-practices/test-case-structure/) - папки, точки проверки и Workstate.
- [Business Parameter и библиотеки](/ToscaBase/ru/data-and-parameters/business-parameters-and-libraries/) - переиспользование TestStep между TestCase.
