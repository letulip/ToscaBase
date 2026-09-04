---
title: Обзор Commander
description: Экскурсия по Tosca Commander — стартовая страница и проект-пример First Steps, разделы workspace, устройство TestCase изнутри, Test Configuration Parameters и запуск TestCase в ScratchBook.
level: 1
sidebar:
  order: 60
sources:
  - id: U9X3juv6tz4
    title: "Tosca Tutorial | Lesson 4 - Tosca Commander Overview | Execute First Test Case | Test Results |"
    url: https://www.youtube.com/watch?v=U9X3juv6tz4
    at: "00:02"
  - id: c-VgJF2i1mU
    title: "Tricentis Tosca Tutorial Part-3 : Tosca Initial Project Setup, Tosca Workspace Overview & Creation"
    url: https://www.youtube.com/watch?v=c-VgJF2i1mU
    at: "05:30"
  - id: 6Z-XkFoVoxw
    title: "Tosca Tutorial | Lesson 5 - Create First Test Case | Tosca Commander | New Workspace |"
    url: https://www.youtube.com/watch?v=6Z-XkFoVoxw
    at: "09:21"
---

Tosca Commander — приложение, в котором проходит весь жизненный цикл тестирования: Module, TestCase, требования, дизайн тестов, выполнение и результаты — всё это разделы одного окна. Быстрее всего освоиться помогает проект-пример **First Steps**, поставляемый с Tosca. В нём есть готовые TestCase, которые можно открыть, изучить и запустить, прежде чем строить что-то своё.

## Стартовая страница и проект First Steps

После подключения лицензии Commander показывает стартовую страницу с недавними workspace и, по умолчанию, проектом **First Steps**. Щёлкните его, чтобы открыть. В разделе **TestCases** лежат примеры папок для ручных, автоматизированных и data-driven тестов и вспомогательных объектов, а также TestCase `Run me`, предназначенный для первого запуска.

## Разделы workspace

Каждый блок в окне Commander — раздел workspace. Основные:

| Раздел | Содержимое |
|---|---|
| **TestCases** | Папки, TestCase и их TestStep (шаги теста); место, где собирается автоматизация |
| **Modules** | Техническая информация о контролах приложения, полученная XScan. См. [Обзор Module](/ToscaBase/ru/modules/modules-overview/) |
| **Requirements** | Требования с весом риска, связанные с TestCase. См. [Требования и риски](/ToscaBase/ru/requirements-and-reporting/requirements-and-risk/) |
| **TestCase-Design** | TestSheet, атрибуты и экземпляры для data-driven дизайна. См. [Дизайн TestCase](/ToscaBase/ru/test-case-design/) |
| **Execution** | ExecutionList и их постоянные результаты. См. [ExecutionList](/ToscaBase/ru/execution/execution-lists/) |
| **Issues** | Дефекты, связанные с выполнениями |
| **Tutorial** | Встроенные учебные материалы; для этой базы знаний не нужны |

Чтобы увидеть иерархию всего проекта, нажмите **Project** на вкладке **Home**.

### Расположение разделов

Разделы можно показывать рядом. Перетащите вкладку раздела на одну из целей докинга (центр, верх, низ, лево, право), чтобы разделить окно; с **Modules** справа и **TestCases** слева можно перетаскивать Module прямо в TestCase. Закрытый раздел открывается заново через меню **Sections**, где перечислены все разделы (так его открывают в уроке об [отчётах](/ToscaBase/ru/requirements-and-reporting/reports/); в обзорных видео, на которые опирается эта страница, этот шаг не показан).

## Внутри раздела TestCases

Раздел — дерево: родительские папки, дочерние папки и TestCase внутри них (значок TestCase — кружок). Правый щелчок по папке показывает, что можно создать:

- **Create Folder** (`Ctrl+N`) и **Create Virtual Folder** (папка по запросу; см. [TQL и виртуальные папки](/ToscaBase/ru/requirements-and-reporting/tql-and-virtual-folders/))
- **Create TestCase**
- **Create Business TestCase** (см. [Повторения выполнения и бизнес-TestCase](/ToscaBase/ru/execution/execution-repetitions-and-business-test-cases/))
- **Create TestStep Library** (см. [Бизнес-параметры и библиотеки](/ToscaBase/ru/data-and-parameters/business-parameters-and-libraries/))
- **Create Recovery Scenario Collection** (см. [Сценарии восстановления и очистки](/ToscaBase/ru/test-cases/recovery-and-cleanup-scenarios/))
- **Create Test Configuration Parameter**

Сочетания клавиш показаны рядом с каждым пунктом меню; `Ctrl+T` открывает поиск для добавления TestStep из Module.

### Из чего состоит TestCase

Откройте автоматизированный TestCase из примеров. Его TestStep читаются как ручной сценарий: открыть приложение-пример, развернуть браузер, главное меню, данные автомобиля, данные страховки, данные продукта, вариант цены, отправить расчёт. **Expand all** / **Collapse all** показывают или скрывают TestStepValue под каждым шагом.

Каждый TestStepValue — один контрол приложения (текстовое поле, ссылка, кнопка). Панель **Properties** справа показывает идентифицирующие свойства, захваченные XScan, а колонка **Value** содержит данные для ввода или действие. Так и строится TestCase: Module даёт контролы, TestCase — значения и ActionMode. См. [Основы TestCase](/ToscaBase/ru/test-cases/test-case-basics/) и [ActionMode](/ToscaBase/ru/test-cases/action-modes/).

В деталях TestCase есть и **диаграмма потока управления (control flow diagram)** — графическое представление шагов по порядку.

### Test Configuration Parameters

TestCase из примера несёт **Test Configuration** с параметром `Browser`, значение которого — `Internet Explorer`, браузер, под который он был спроектирован. Измените значение на `Chrome`, `Edge` или `Firefox`, чтобы запустить в другом браузере, и верните значение по умолчанию после. Новые параметры добавляются правым щелчком по TestCase (или папке) и пунктом **Create Test Configuration Parameter**. Подробно — в [Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/).

## Запуск TestCase в ScratchBook

1. Выберите TestCase (или его папку) и в контекстном меню нажмите **Run in ScratchBook** либо зелёную кнопку воспроизведения на ленте **TestCases**.
2. Tosca проводит приложение через каждый шаг.
3. **ScratchBook (черновой прогон)** показывает каждый шаг с результатом (passed или failed), временем начала, длительностью и всем, что записано в log info.

:::caution
Результаты ScratchBook временные и нигде не сохраняются. Они нужны для пробных запусков во время построения TestCase. Для результатов, которые нужно хранить, включать в отчёты или сравнивать, поместите TestCase в **ExecutionList** в разделе **Execution** и запускайте оттуда; см. [ExecutionList](/ToscaBase/ru/execution/execution-lists/).
:::

## Далее

[Первый TestCase](/ToscaBase/ru/getting-started/first-test-case/) строит собственный TestCase: сканирование страницы входа, перетаскивание Module, ввод значений, запуск.
