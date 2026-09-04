---
title: Первый TestCase
description: Построение и запуск TestCase входа в систему с нуля — структура папок, сканирование Module, значения и ActionMode, параметр Browser, открытие и закрытие браузера, запуск целиком или по частям в ScratchBook.
level: 1
sidebar:
  order: 70
sources:
  - id: 6Z-XkFoVoxw
    title: "Tosca Tutorial | Lesson 5 - Create First Test Case | Tosca Commander | New Workspace |"
    url: https://www.youtube.com/watch?v=6Z-XkFoVoxw
    at: "02:11"
  - id: U9X3juv6tz4
    title: "Tosca Tutorial | Lesson 4 - Tosca Commander Overview | Execute First Test Case | Test Results |"
    url: https://www.youtube.com/watch?v=U9X3juv6tz4
    at: "08:14"
  - id: nEcKRePDKa0
    title: "TRICENTIS Tosca 16.0 - Lesson 09 | Test Case Automation | Create Test Steps using Modules |"
    url: https://www.youtube.com/watch?v=nEcKRePDKa0
    at: "09:17"
  - id: ZZ6lWHHHnCg
    title: "TRICENTIS Tosca 16.0 - Lesson 10 | Test Case Automation | Populate TestStep Values for Test Cases |"
    url: https://www.youtube.com/watch?v=ZZ6lWHHHnCg
    at: "04:05"
  - id: SLWKhb4igB0
    title: "TRICENTIS Tosca 16.0 - Lesson 11 | Test Case Automation | Run your First Automated Tests | TCP |"
    url: https://www.youtube.com/watch?v=SLWKhb4igB0
    at: "04:47"
---

Первый TestCase — вход в систему: открыть демонстрационный интернет-магазин (демо-сайт Sauce Labs «Swag Labs» со страницей входа и списком товаров), ввести имя пользователя и пароль, нажать **Login** и закрыть браузер. Предпосылки: workspace, созданный из стандартного шаблона ([Workspace и настройка проекта](/ToscaBase/ru/getting-started/workspace-and-project-setup/)), Chrome с расширением Tosca ([Установка](/ToscaBase/ru/getting-started/installation/#расширение-браузера-для-xscan)) и открытая в Chrome демо-страница.

## 1. Структура папок в TestCases

В разделе **TestCases** создайте папку для сценария (`Ctrl+N` или лента), например `Sauce Demo Test`. Внутри создайте:

- папку `Prerequisites` — она будет открывать приложение;
- TestCase `Login Test`;
- позже папку `Post condition` — она будет закрывать приложение.

Папку можно выполнить как единое целое, поэтому предусловия, тест и очистка выполняются вместе по порядку.

## 2. Сканирование страницы входа в Module

В TestCase нет технической информации; она живёт в **Module** — аналоге page object в Tosca.

1. В разделе **Modules** создайте папку (например, `Sauce Demo`).
2. Правый щелчок по ней — **Scan > Application**.
3. Агент XScan перечисляет открытые окна. Выберите окно Chrome с демо-страницей и нажмите **Scan**.
4. Щёлкните в приложении поле **username**, поле **password** и кнопку **Login**; они появляются в XScan с галочками.
5. Нажмите **Save** и закройте XScan. Раздел **Advanced** (идентифицирующие свойства для неуникальных контролов) здесь не нужен; см. [Идентификация контролов](/ToscaBase/ru/modules/control-identification/).
6. Переименуйте новый Module во что-то понятное любому, например `Login Page`.

Развернув Module, вы увидите три ModuleAttribute с их **ActionMode**, **диапазоном значений** и идентифицирующими свойствами; пока каждый контрол уникален на странице, менять нечего. Подробно — [XScan](/ToscaBase/ru/modules/xscan/).

## 3. Перетаскивание Module в TestCase

Закрепите **Modules** рядом с **TestCases** ([Обзор Commander](/ToscaBase/ru/getting-started/commander-overview/#расположение-разделов)) и перетащите `Login Page` на `Login Test` либо щёлкните TestCase правой кнопкой и используйте *search and add step* (`Ctrl+T`), как это делают в уроках по Tosca 16. В обоих случаях Tosca создаёт TestStep с одним TestStepValue на каждый ModuleAttribute; переименуйте его по бизнес-действию. Заполните его:

| TestStepValue | Тип данных | ActionMode | Значение |
|---|---|---|---|
| Username | String | `Input` | имя стандартного пользователя демо-сайта (показано на странице входа) |
| Password | Password | `Input` | соответствующий пароль; после ввода он маскируется |
| Login | String | `Input` | `X` |

Ввод или вставка значения автоматически переключает ActionMode на `Input`; тип данных по умолчанию — String. Кнопка или ссылка принимает `X` — внутренний клик без перемещения указателя и рекомендуемый способ нажатия (пустое значение с `Input` тоже нажимает, но `X` делает намерение видимым). Флажок принимает `True`. В более старом видео выбирают **Click** из выпадающего списка значений (`{CLICK}` — более медленный физический клик мышью; см. [Синхронизация вместо ожиданий](/ToscaBase/ru/best-practices/synchronisation-not-waits/)). Все ActionMode описаны в [ActionMode](/ToscaBase/ru/test-cases/action-modes/).

:::tip
Когда в TestCase много шагов, `F9` переключает раздел TestCases между показом только тех TestStepValue, у которых есть значение, и показом всех.
:::

## 4. Браузер как Test Configuration Parameter

Tosca должна знать, какой браузер использовать. Правый щелчок по родительской папке `Sauce Demo Test` — **Create Test Configuration Parameter**. Введите или выберите `Browser` (предопределённый тип параметра со значениями-браузерами), задайте значение `Chrome`, тип данных оставьте string. Поскольку параметр стоит на родительской папке, он действует на всё внутри. В уроке 11 его ставят на сам TestCase (вкладка **Test Configuration**, правый щелчок по записи, **Create Test Configuration Parameter**, `Browser` = `Chrome`); параметр может нести и ExecutionList, и тогда его значение перекрывает значение TestCase. Подробнее — [Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/).

## 5. Открытие приложения (Prerequisites)

Браузер выбран, но ничто его пока не открывает. В `Prerequisites` добавьте TestStep из стандартных Module: **TBox XEngines > HTML > Open Url** в разделе Modules либо `Ctrl+T` в папке и поиск. Переименуйте шаг в `Open Application` и вставьте URL демо-сайта в значение **Url**. Необязательные значения `ActiveTab` и аргументы браузера можно оставить пустыми.

## 6. Запуск в ScratchBook

Правый щелчок по **родительской папке** (а не только по TestCase, потому что сначала должны выполниться предусловия) — **Run in ScratchBook**. Запускается Chrome, открывается URL, вводятся учётные данные и нажимается Login. ScratchBook показывает `Open Url` и `Login Page` с их TestStepValue и результатом каждого шага: всё зелёное — значит, каждый шаг пройден. Прогоны в ScratchBook — пробные: результаты временные и не сохраняются, в отличие от [ExecutionList](/ToscaBase/ru/execution/execution-lists/). Той же командой запускают сквозной TestCase демо-магазина из уроков по Tosca 16 — от входа до оформления заказа и выхода ([Основы TestCase](/ToscaBase/ru/test-cases/test-case-basics/)).

:::caution
Успешный прогон в ScratchBook не доказывает, что вход выполнен: в источнике первый прогон прошёл, хотя страница показывала «username and password do not match», потому что ничто не проверяло результат. Добавьте проверку (например, заголовок страницы товаров с ActionMode `Verify`); см. [Структура TestCase](/ToscaBase/ru/best-practices/test-case-structure/).
:::

### Запуск части TestCase

Для отладки запускайте только фрагмент:

- Выделите несколько TestStep (`Shift`+щелчок), правый щелчок — **Run in ScratchBook**: выполнятся только они, например один вход.
- Щёлкните правой кнопкой папку TestStep, например `Checkout process`, и запустите её отдельно.
- Откройте **ScratchBook** с ленты, закрепите его справа, перетащите в него TestStep и выберите **Run** в контекстном меню. ScratchBook хранит свои записи, поэтому очищайте их перед следующим прогоном.

Частичный прогон предполагает, что приложение уже в нужном состоянии; в источнике один прогон упал лишь потому, что были открыты две вкладки магазина, — закройте лишние вкладки заранее.

## 7. Закрытие браузера (Post condition)

Создайте папку `Post condition` и перетащите в неё **TBox Automation Tools > Basic window operations > TBox Window Operation**, переименовав в `Close Application`:

| TestStepValue | ActionMode | Значение |
|---|---|---|
| Caption | `Select` | `Swag*` (заголовок начинается со «Swag Labs»; подстановочный знак для остального) |
| Operation | `Input` | `Close` (в списке также Maximize, Minimize, Normal и другие) |

Запустите родительскую папку снова: видны три шага, и в конце браузер закрывается. Module описан в [Операциях с окнами](/ToscaBase/ru/standard-modules/window-operations/).

## 8. Установка Workstate

У каждого TestCase есть **Workstate (состояние работы)**: `Planned`, `In Work`, `Completed`. Ставьте `In Work`, пока строите, и `Completed`, когда закончили; в общем workspace это показывает коллегам, что готово. См. [Структура TestCase](/ToscaBase/ru/best-practices/test-case-structure/#устанавливайте-workstate).

## Что вы освоили

Сканировать страницу в Module, строить TestCase из Module, задавать значения и ActionMode, параметризовать браузер, обрамлять тест предусловиями и очисткой, запускать его целиком или по частям. Каждая следующая тема расширяет этот каркас; продолжайте с [Основ TestCase](/ToscaBase/ru/test-cases/test-case-basics/).
