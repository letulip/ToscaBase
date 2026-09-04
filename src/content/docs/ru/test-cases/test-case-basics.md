---
title: Основы TestCase
description: Что такое TestCase в Tosca, технические и бизнес-TestCase, TestStep из Module, папки TestStep, ввод значений, настройка браузера и запуск, а также первый сквозной пример.
level: 1
sidebar:
  order: 10
sources:
  - id: TMfn5am9x-c
    title: "Tricentis Tosca Tutorial Part-5 : Tosca Test Case, Tosca Test Case Design and Best Practices"
    url: https://www.youtube.com/watch?v=TMfn5am9x-c
    at: "01:15"
  - id: R5IzSJwGgSc
    title: "TRICENTIS Tosca 16.0 - Lesson 08 | Test Case Automation | Create TestCase Structure |"
    url: https://www.youtube.com/watch?v=R5IzSJwGgSc
    at: "02:04"
  - id: nEcKRePDKa0
    title: "TRICENTIS Tosca 16.0 - Lesson 09 | Test Case Automation | Create Test Steps using Modules |"
    url: https://www.youtube.com/watch?v=nEcKRePDKa0
    at: "01:01"
  - id: ZZ6lWHHHnCg
    title: "TRICENTIS Tosca 16.0 - Lesson 10 | Test Case Automation | Populate TestStep Values for Test Cases |"
    url: https://www.youtube.com/watch?v=ZZ6lWHHHnCg
    at: "04:05"
  - id: SLWKhb4igB0
    title: "TRICENTIS Tosca 16.0 - Lesson 11 | Test Case Automation | Run your First Automated Tests | TCP |"
    url: https://www.youtube.com/watch?v=SLWKhb4igB0
    at: "05:55"
---

TestCase (тест-кейс) — это набор инструкций, который проходит через приложение и проверяет результат. Написанный по требованиям автоматизированный TestCase в Tosca собирается из Module (модулей) — стандартных и пользовательских — плюс нужных им тестовых данных. Module хранят техническую информацию (как найти каждый контрол), TestCase — бизнес-информацию (последовательность действий), поэтому автоматизация ручного теста состоит из четырёх шагов: разметить структуру TestCase, добавить TestStep (шаги теста) из Module, ввести значения, затем настроить браузер и запустить. Эта страница — про сам объект; пошаговый разбор — [Первый TestCase](/ToscaBase/ru/getting-started/first-test-case/), режимы действия — в [ActionMode](/ToscaBase/ru/test-cases/action-modes/).

## Технические и бизнес-TestCase

| Вид | Что содержит | Исполняемый |
|---|---|---|
| Technical TestCase (технический) | Всю техническую информацию для управления контролами: TestStep, TestStepValue, ActionMode | Да |
| Business TestCase (бизнес) | Группу технических TestCase, представляющую одну функциональность и спроектированную по требованиям | Нет; служит для мониторинга покрытия |

Ниже — только технические TestCase; бизнес-TestCase описаны в документе [Повторения выполнения и бизнес-TestCase](/ToscaBase/ru/execution/execution-repetitions-and-business-test-cases/).

## Создание TestCase

1. В секции **TestCases** щёлкните правой кнопкой по папке и выберите значок создания TestCase или нажмите **Ctrl+N**, затем **Ctrl+T**.

:::note
**Ctrl+N**, затем **Ctrl+T** создаёт TestCase; одиночный **Ctrl+T** внутри TestCase открывает поиск для добавления TestStep из Module.
:::
2. Дайте TestCase осмысленное имя. Он пуст, пока не добавлены TestStep.
3. Добавьте TestStep из Module: перетащите Module из секции **Modules** на TestCase (или на папку TestStep внутри него) либо щёлкните правой кнопкой по TestCase или папке, выберите **Search and add TestStep** (**Ctrl+T**) и найдите Module по имени. Каждый Module становится одним TestStep, а его TestStepValue — это контролы Module; один и тот же Module можно добавлять сколько угодно раз.
4. Для каждого нужного контрола введите значение в колонке **Value** и выберите ActionMode. Нетронутые контролы игнорируются.
5. Переименуйте каждый TestStep по выполняемому действию (`Navigate to login page`, `Order blue jeans`) — ради читаемого лога. Порядок шагов меняется перетаскиванием; **Expand all** (контекстное меню) раскрывает все уровни сразу.

:::tip
Сначала продумайте папки. В общем репозитории перед созданием сделайте check-out (возьмите на редактирование) секцию **TestCases** (или папку); см. [Многопользовательские workspace](/ToscaBase/ru/administration/multi-user-workspaces/).
:::

## Папки TestStep

TestStep группируются в папки (правой кнопкой по TestCase, **Create folder**); разметьте дерево по ручному тесту до того, как перетащен первый Module. В источнике каждый TestCase строится из `Precondition` (открыть URL, перейти на страницу логина, войти), `Process` и `Post condition` (выйти, закрыть браузер), а `Process` делится на подпапку для каждого этапа (`Order product`, `Start checkout`, `Checkout process`, `Verification of prices`, `Confirmation`, `Verification of success`). Такой каркас уже читается как ручной тест; TestStep добавляются папка за папкой, а папку можно запустить отдельно. Почему папки важны для сопровождения, см. в [Структуре TestCase](/ToscaBase/ru/best-practices/test-case-structure/); папка — ещё и единственное место, где задаётся [Repetition](/ToscaBase/ru/test-cases/repetitions/).

## Ввод значений

- Введите или выберите значение в колонке **Value**; как только значение введено, Tosca ставит ActionMode `Input` — то, что нужно большинству шагов. Текстовое поле принимает текст, выпадающий список предлагает варианты, захваченные XScan, чекбокс принимает `True`, кнопка или ссылка — `X` (клик).
- У каждого TestStepValue есть и **тип данных**: по умолчанию `String`, в списке также `Numeric`, `Date` и другие. Он важен для проверок, где два равных числа, сравниваемые как строки, могут не совпасть; см. [Verify](/ToscaBase/ru/test-cases/action-modes/#verify).
- Module, которые находят окно по заголовку, например `Close Browser`, принимают подстановочный шаблон (`Demo Web Shop*`) с ActionMode `Select`.
- **F9** фильтрует TestCase до TestStepValue, у которых есть значение; повторное нажатие показывает все контролы.
- Значения могут оставаться пустыми, пока раскладываются шаги; в источнике они заполняются вторым проходом.

## Настройка и запуск

Без указаний Tosca работает с Internet Explorer, поэтому веб-TestCase нужен Test Configuration Parameter `Browser`: выделите TestCase, откройте вкладку **Test Configuration**, щёлкните запись правой кнопкой, **Create Test Configuration Parameter**, выберите `Browser` и имя браузера (`Chrome`). Параметр можно поставить и на папку или ExecutionList; см. [Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/). Затем правый щелчок по TestCase — **Run in ScratchBook**: открывается браузер и выполняется каждый шаг; зелёный — значит, пройден. Результаты ScratchBook временные, поэтому это место для пробных прогонов; для сохраняемых результатов нужен [ExecutionList](/ToscaBase/ru/execution/execution-lists/). Для отладки выделите несколько TestStep через `Shift` или одну папку TestStep и запустите только их; подробности — в [Первом TestCase](/ToscaBase/ru/getting-started/first-test-case/#6-запуск-в-scratchbook).

## Workstate

У TestCase три состояния: `Planned`, `In Work` и `Completed`. Состояние не декоративно — оно влияет на цифры покрытия требований. Когда какое ставить — в документе [Структура TestCase](/ToscaBase/ru/best-practices/test-case-structure/).

:::note
В источнике первое состояние названо «planning»; колонка Workstate в Commander показывает `Planned`. Считайте это одним и тем же значением.
:::

## ActionMode вкратце

ActionMode говорит Tosca, что делать со значением: `Input` вводит данные или кликает, `Verify` сравнивает свойство со значением, `Buffer` сохраняет значение контрола под именем, `WaitOn` ждёт выполнения условия, `Select` и `Constraint` проходят по таблицам и сужают поиск, `Insert` создаёт объекты в не-UI структурах вроде XML. Подробности — в [ActionMode](/ToscaBase/ru/test-cases/action-modes/).

## Рабочий пример: поиск в Google

Сценарий: открыть Google в Chrome, найти *Tricentis Tosca*, открыть первый результат, проверить, что появился сайт Tricentis, закрыть браузер. Три пользовательских Module (экран поиска Google, экран результатов, портал Tricentis) содержат только нужные контролы; см. [XScan](/ToscaBase/ru/modules/xscan/).

| # | TestStep | Module | Значения и ActionMode |
|---|---|---|---|
| 1 | Open Google | `OpenUrl` (стандартный Module, **TBox XEngines > HTML**) | URL `www.google.com`, `Input` |
| 2 | Search Tricentis Tosca | Экран поиска Google | значок Google: `Exists` = `True`, `WaitOn`; поле поиска: `Tricentis Tosca`, `Input`; кнопка поиска: клик, `Input` |
| 3 | Pause | `TBox Wait` (стандартный Module) | `5000` (миллисекунды) |
| 4 | Open first result | Экран результатов | ссылка первого результата: клик, `Input` |
| 5 | Verify Tosca official portal | Портал Tricentis | логотип: `Exists` = `True`, `Verify` |
| 6 | Close browser | `Close Browser` (стандартный Module) | заголовок `Tricentis Tosca*` (подстановочный символ) |

Замечания:

- **Шаг 1.** Универсальный Module **TBox Automation Tools > Process Automation** запускает любую программу; для веб-приложения используйте `OpenUrl`.
- **Шаг 2.** `WaitOn` на значке Google обеспечивает синхронизацию: шаг ждёт, пока страница не отрисует значок.
- **Шаг 3.** Статическое ожидание 5 с — обходной приём автора для медленных результатов; лучшая практика заменяет его на `WaitOn`, см. [Синхронизация вместо ожиданий](/ToscaBase/ru/best-practices/synchronisation-not-waits/).

Переиспользование TestStep между TestCase: [Business Parameters и библиотеки TestStep](/ToscaBase/ru/data-and-parameters/business-parameters-and-libraries/).
