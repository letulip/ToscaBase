---
title: Основы TestCase
description: Что такое TestCase в Tosca, технические и бизнес-TestCase, как TestStep собираются из Module, папки TestStep, повторяющие бизнес-процесс, ввод значений и первый сквозной пример с WaitOn, Input и Verify.
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
---

TestCase (тест-кейс) — это набор инструкций, который проходит через приложение и проверяет результат. Он пишется по требованиям и может быть ручным или автоматизированным; в Tosca автоматизированный TestCase собирается из Module (модулей) — стандартных и пользовательских — плюс нужных им тестовых данных. Module хранят техническую информацию (как найти каждый контрол), TestCase — бизнес-информацию (последовательность действий), поэтому автоматизация ручного теста состоит из четырёх шагов: разметить структуру TestCase, добавить TestStep (шаги теста) из Module, ввести значения, затем настроить браузер и запустить. Эта страница — про сам объект; пошаговый разбор одного такого теста — [Первый TestCase](/ToscaBase/ru/getting-started/first-test-case/), а какой ActionMode (режим действия) ставить на каждое значение — тема документа [Режимы действия](/ToscaBase/ru/test-cases/action-modes/).

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
3. Добавьте TestStep из Module одним из двух способов: перетащите Module из секции **Modules** на TestCase (или на папку TestStep внутри него) либо щёлкните правой кнопкой по TestCase или папке, выберите **Search and add TestStep** (**Ctrl+T**) и найдите Module по имени в списке поиска. В обоих случаях каждый Module становится одним TestStep, а его TestStepValue — это контролы Module; один и тот же Module можно добавлять сколько угодно раз (один Module верхнего меню даёт шаги, которые открывают страницу логина, открывают корзину и выполняют выход).
4. Для каждого нужного контрола введите значение в колонке **Value** и выберите ActionMode. Нетронутые контролы игнорируются.
5. Переименуйте каждый TestStep по выполняемому действию (`Navigate to login page`, `Order blue jeans`); необязательно, но лог становится читаемым. Порядок шагов меняется перетаскиванием; **Expand all** в контекстном меню TestCase, папки или TestStep раскрывает все уровни сразу.

:::tip
Сгруппируйте TestCase по папкам до их создания. В общем репозитории сначала сделайте check-out (возьмите на редактирование) секцию **TestCases** (или папку); см. [Многопользовательские workspace](/ToscaBase/ru/administration/multi-user-workspaces/).
:::

## Папки TestStep

TestStep можно группировать в папки внутри TestCase (правой кнопкой по TestCase, **Create folder**), и дерево папок лучше разметить до того, как перетащен первый Module, — прямо по ручному тесту. В источнике каждый TestCase строится из `Precondition` (открыть URL, перейти на страницу логина, войти), `Process` и `Post condition` (выйти, закрыть браузер), а `Process` делится на подпапку для каждого этапа: `Order product`, `Start checkout`, `Checkout process`, `Verification of prices`, `Confirmation`, `Verification of success`. Пустой TestCase с такой структурой уже читается как ручной тест; затем TestStep добавляются папка за папкой, а отдельную папку можно запустить саму по себе в ScratchBook. Левая панель показывает дерево, правая (по двойному щелчку) — место редактирования TestStep и значений. Почему папки важны для сопровождения, см. в [Структуре TestCase](/ToscaBase/ru/best-practices/test-case-structure/); папка — ещё и единственное место, где задаётся [Repetition](/ToscaBase/ru/test-cases/repetitions/).

## Ввод значений

- Введите или выберите значение в колонке **Value**; как только значение введено, Tosca ставит ActionMode `Input` — то, что нужно большинству шагов. Текстовое поле принимает текст, выпадающий список предлагает варианты, захваченные XScan, чекбокс принимает `True`, кнопка или ссылка — `X` (клик). Пустое значение на кликабельном контроле под `Input` тоже кликает, но источник рекомендует `X`, чтобы намерение было видно в шаге.
- У каждого TestStepValue есть и **тип данных**: по умолчанию `String`, в списке также `Numeric`, `Date` и другие. Он важен для проверок, где два равных числа, сравниваемые как строки, могут не совпасть; см. [Verify](/ToscaBase/ru/test-cases/action-modes/#verify).
- Module, которые находят окно по заголовку, например `Close Browser`, принимают подстановочный шаблон (`Demo Web Shop*`) с ActionMode `Select`, потому что ничего не вводится.
- **F9** фильтрует TestCase до TestStepValue, у которых есть значение; повторное нажатие показывает все контролы. Удобно в Module со многими атрибутами, из которых используются несколько.
- Значения могут оставаться пустыми, пока раскладываются шаги; в источнике сначала добавляются все TestStep, а значения заполняются вторым проходом.

## Workstate

У TestCase три состояния: `Planned`, `In Work` и `Completed`. Состояние не декоративно — оно влияет на цифры покрытия требований. Когда какое значение ставить, объяснено в документе [Структура TestCase](/ToscaBase/ru/best-practices/test-case-structure/).

:::note
В источнике первое состояние названо «planning»; колонка Workstate в Commander показывает `Planned`. Считайте это одним и тем же значением.
:::

## ActionMode вкратце

Каждый TestStepValue несёт ActionMode, который говорит Tosca, что делать со значением: `Input` вводит данные или кликает, `Verify` сравнивает свойство со значением, `Buffer` сохраняет значение контрола под именем, `WaitOn` ждёт выполнения условия, `Select` и `Constraint` проходят по таблицам и сужают поиск, `Insert` создаёт объекты в не-UI структурах вроде XML. Синтаксис и примеры для каждого — в [Режимах действия](/ToscaBase/ru/test-cases/action-modes/).

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

- **Шаг 1.** Универсальный Module **TBox Automation Tools > Process Automation** запускает любую программу; для веб-приложения правильный выбор — специализированный `OpenUrl`.
- **Шаг 2.** `WaitOn` на значке Google обеспечивает синхронизацию: шаг не продолжается, пока страница не отрисует значок.
- **Шаг 3.** Статическое ожидание 5 с — так в источнике сделано для медленных результатов поиска; лучшая практика Tricentis — заменять статические ожидания на `WaitOn`, см. [Синхронизация вместо ожиданий](/ToscaBase/ru/best-practices/synchronisation-not-waits/).
- **Шаг 6.** `Close Browser` находит окно по заголовку; звёздочка в `Tricentis Tosca*` — подстановочный символ.
- **Браузер.** По умолчанию Tosca работает с Internet Explorer. Чтобы запускать в Chrome, добавьте на TestCase Test Configuration Parameter `Browser` со значением `Chrome`. См. [Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/).

TestCase готов к запуску из [ExecutionList](/ToscaBase/ru/execution/execution-lists/) или ScratchBook.

О переиспользовании TestStep между TestCase см. [Business Parameters и библиотеки TestStep](/ToscaBase/ru/data-and-parameters/business-parameters-and-libraries/).
