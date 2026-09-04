---
title: Первый TestCase
description: Построение и запуск полного TestCase входа в систему с нуля — структура папок, сканирование страницы в Module, перетаскивание Module в TestCase, значения и ActionMode, параметр Browser, открытие и закрытие браузера, запуск в ScratchBook.
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
---

Первый TestCase — вход в систему: открыть демонстрационный интернет-магазин (демо-сайт Sauce Labs «Swag Labs» со страницей входа и списком товаров), ввести имя пользователя и пароль, нажать **Login** и закрыть браузер. При всей простоте он проходит полный рабочий цикл Tosca: сканирование страницы в Module, сборку TestCase из Module, добавление стандартных Module, открывающих и закрывающих браузер, задание браузера через Test Configuration Parameter и запуск в ScratchBook. Предпосылки: workspace, созданный из стандартного шаблона ([Workspace и настройка проекта](/ToscaBase/ru/getting-started/workspace-and-project-setup/)), Chrome с расширением Tosca ([Установка](/ToscaBase/ru/getting-started/installation/#расширение-браузера-для-xscan)) и открытая в Chrome демо-страница.

## 1. Структура папок в TestCases

В разделе **TestCases** создайте папку для сценария (`Ctrl+N` или лента), например `Sauce Demo Test`. Внутри создайте:

- папку `Prerequisites` — она будет открывать приложение;
- TestCase `Login Test`;
- позже папку `Post condition` — она будет закрывать приложение.

Как вкладывать папки и TestCase — дело ваше; суть в том, что папку можно выполнить как единое целое, и предусловия, тест и очистка выполняются вместе по порядку.

## 2. Сканирование страницы входа в Module

В TestCase нет технической информации; она живёт в **Module** — аналоге page object в Tosca.

1. В разделе **Modules** создайте папку (например, `Sauce Demo`).
2. Правый щелчок по ней — **Scan**. Выпадающий список показывает несколько типов сканирования (application, API, mobile, PDF и другие). Выберите **Application**.
3. Агент XScan перечисляет открытые окна. Выберите окно Chrome с демо-страницей и нажмите **Scan**.
4. XScan просит щёлкать контролы в приложении, чтобы добавить их. Щёлкните поле **username**, поле **password** и кнопку **Login**. Они появляются в окне XScan с галочками.
5. Нажмите **Save** и закройте XScan. Раздел **Advanced**, где меняют идентифицирующие свойства, когда контрол не уникален, здесь не нужен; см. [Идентификация контролов](/ToscaBase/ru/modules/control-identification/).
6. Переименуйте новый Module во что-то понятное любому, например `Login Page`.

Развернув Module, вы увидите три ModuleAttribute с их **ActionMode**, **диапазоном значений** и, на панели Properties, идентифицирующими свойствами, которые будет использовать Tosca. Если каждый контрол уникален на странице, менять нечего. Подробно — [XScan](/ToscaBase/ru/modules/xscan/).

## 3. Перетаскивание Module в TestCase

Закрепите **Modules** рядом с **TestCases** (перетащите вкладку раздела на правую цель докинга; см. [Обзор Commander](/ToscaBase/ru/getting-started/commander-overview/#расположение-разделов)). Перетащите `Login Page` на `Login Test`. Другой способ, которым в уроках по Tosca 16 добавляют большинство шагов, — правый щелчок по TestCase (или папке), пункт *search and add step* либо `Ctrl+T`, затем выбор Module в поиске. В обоих случаях Tosca создаёт TestStep с одним TestStepValue на каждый ModuleAttribute; переименуйте его по бизнес-действию, которое он выполняет. Заполните его:

| TestStepValue | Тип данных | ActionMode | Значение |
|---|---|---|---|
| Username | String | `Input` | имя стандартного пользователя демо-сайта (показано на странице входа) |
| Password | Password | `Input` | соответствующий пароль; после ввода он маскируется |
| Login | String | `Input` | `X` |

Ввод или вставка значения автоматически переключает ActionMode на `Input`; тип данных по умолчанию — String (есть также Numeric, Date и другие). Текстовое поле принимает `Input` со значением; кнопка или ссылка — не текстовое поле, поэтому её значение `X` велит Tosca нажать её, при том что ActionMode остаётся `Input`. `X` — внутренний клик без перемещения указателя, и это рекомендуемый способ нажатия. Пустое значение с `Input` тоже нажимает, но урок по Tosca 16 рекомендует `X`, чтобы намерение было видно в шаге. Флажок принимает `True`, чтобы его отметить. В видео вместо этого выбирают **Click** из выпадающего списка значений, что подставляет `{CLICK}` — физический клик мышью; он работает, но медленнее и менее надёжен, см. [Синхронизация вместо ожиданий](/ToscaBase/ru/best-practices/synchronisation-not-waits/). Все ActionMode описаны в [ActionMode](/ToscaBase/ru/test-cases/action-modes/).

:::tip
Когда в TestCase много шагов, `F9` переключает раздел TestCases между показом только тех TestStepValue, у которых есть значение, и показом всех. **Expand all** работает на уровне TestStep, TestCase и папки.
:::

## 4. Браузер как Test Configuration Parameter

Tosca должна знать, какой браузер использовать. Правый щелчок по родительской папке `Sauce Demo Test` — **Create Test Configuration Parameter**. Введите или выберите `Browser` (предопределённый тип параметра со значениями-браузерами), задайте значение `Chrome`, тип данных оставьте string. Поскольку параметр стоит на родительской папке, он действует на всё внутри. Подробнее — [Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/).

## 5. Открытие приложения (Prerequisites)

Браузер выбран, но ничто его пока не открывает. В `Prerequisites` добавьте TestStep из стандартных Module, пришедших с шаблоном: **TBox XEngines > HTML > Open Url** в разделе Modules либо `Ctrl+T` в папке и поиск. Переименуйте шаг в `Open Application` и вставьте URL демо-сайта в значение **Url**. Необязательные значения `ActiveTab` и аргументы браузера можно оставить пустыми.

## 6. Запуск в ScratchBook

Правый щелчок по **родительской папке** (а не только по TestCase, потому что сначала должны выполниться предусловия) — **Run in ScratchBook**. Запускается Chrome, открывается URL, вводятся учётные данные и нажимается Login. ScratchBook показывает `Open Url` и `Login Page` с их TestStepValue и результатом каждого шага.

:::caution
Успешный прогон в ScratchBook не доказывает, что вход выполнен. В источнике первый прогон прошёл все шаги, хотя страница показывала «username and password do not match»: TestCase только вводил значения и щёлкал, ничто не проверяло результат. Добавьте проверку (например, заголовок страницы товаров с ActionMode `Verify`), прежде чем доверять тесту; см. [Структура TestCase](/ToscaBase/ru/best-practices/test-case-structure/).
:::

## 7. Закрытие браузера (Post condition)

Создайте папку `Post condition` и перетащите в неё **TBox Automation Tools > Basic window operations > TBox Window Operation**, переименовав в `Close Application`:

| TestStepValue | ActionMode | Значение |
|---|---|---|
| Caption | `Select` | `Swag*` — заголовок окна начинается со «Swag Labs», подстановочный знак покрывает остальное |
| Operation | `Input` | `Close` (в списке также Maximize, Minimize, Normal и другие) |

Запустите родительскую папку снова: теперь видны три шага (Open Url, Login Page, TBox Window Operation), и в конце браузер закрывается. Module описан в [Операциях с окнами](/ToscaBase/ru/standard-modules/window-operations/).

## 8. Установка Workstate

У каждого TestCase есть **Workstate (состояние работы)**: `Planned`, `In Work`, `Completed`. Ставьте `In Work`, пока строите, и `Completed`, когда закончили; значок меняется вместе с состоянием, а в общем workspace это показывает коллегам, что готово. Работая в одиночку, можно не обращать внимания. См. [Структура TestCase](/ToscaBase/ru/best-practices/test-case-structure/#устанавливайте-workstate).

## Что вы освоили

Сканировать страницу в Module, строить TestCase из Module, задавать значения и ActionMode, параметризовать браузер, обрамлять тест предусловиями и очисткой и запускать его. Каждая следующая тема расширяет этот каркас. Продолжайте с [Основ TestCase](/ToscaBase/ru/test-cases/test-case-basics/), где разобран и длинный сквозной сценарий демо-магазина (папки precondition, process, postcondition) из уроков по Tosca 16.
