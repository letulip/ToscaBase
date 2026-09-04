---
title: Стандартные модули
description: Модули TBox Automation Modules, входящие в поставку Tosca, для файлов, папок, буферов, процессов, скриншотов, окон и JavaScript.
level: 2
sidebar:
  order: 0
sources:
  - id: 0Hc_M7ksots
    title: "TRICENTIS Tosca 16.0 - Lesson 05 | Model-Based Test Automation | Standard Modules of Tosca |"
    url: https://www.youtube.com/watch?v=0Hc_M7ksots
    at: "03:02"
---

Tosca поставляется с библиотекой готовых модулей — **Standard modules (стандартные модули)**, они же TBox Automation Modules. Они покрывают общие операции, нужные TestCase вокруг тестируемого приложения, и добавляются через **Add TestStep** без сканирования. Раздел описывает каждую группу: что делает модуль, его ModuleAttributes и подводные камни.

| Документ | Содержание |
|---|---|
| [Операции с файлами и папками](/ToscaBase/ru/standard-modules/file-and-folder-operations/) | Создание, копирование, сравнение и удаление файлов и папок; проверка существования папки |
| [Операции с буферами](/ToscaBase/ru/standard-modules/buffer-operations/) | Set Buffer, Partial Buffer, Name to Buffer, Delete Buffer |
| [Запуск и закрытие программ](/ToscaBase/ru/standard-modules/start-and-close-programs/) | TBox Start Program с аргументами, закрытие программ через taskkill, Start/Stop Timer |
| [TBox Evaluation Tool](/ToscaBase/ru/standard-modules/evaluation-tool/) | TBox Evaluation Tool: сравнение динамических выражений, условие If, математика по оператору |
| [Скриншоты при сбое](/ToscaBase/ru/standard-modules/screenshots-on-failure/) | TBox Take Screenshot и настройка проекта для автоматических скриншотов |
| [Операции с окнами](/ToscaBase/ru/standard-modules/window-operations/) | TBox Window Operation, закрытие попапов, TBox Scroll Window Operation |
| [Диалоги рабочего стола](/ToscaBase/ru/standard-modules/desktop-dialogs/) | TBox Save As для диалога Windows Save As и его окна подтверждения |
| [Выполнение JavaScript](/ToscaBase/ru/standard-modules/execute-javascript/) | Execute JavaScript и Verify JavaScript Result в TBox XEngines > HTML |

Читайте по порядку: файловые и буферные операции нужны почти каждому TestCase, модули процессов и окон вступают в игру для настольных приложений, а Module для JavaScript — запасной вариант для веб-сценариев, которые HTML engine не выражает напрямую.

## Откуда они берутся

Стандартные модули поставляются как subset (подмножество) `Standard.tsu` в папке установки Tosca. При создании workspace (рабочего пространства) пункт **Use workspace template** указывает на этот файл, и в новом workspace в разделе Modules появляется папка **Standard modules** (см. [Настройка workspace и проекта](/ToscaBase/ru/getting-started/workspace-and-project-setup/)). Что в ней есть, как показано в уроке 5:

| Папка | Примеры |
|---|---|
| TBox Automation Tools | Basic window operations (отправка клавиш, операции с окном, прокрутка окна), file operations (сравнение файлов) |
| TBox XEngines > HTML | `OpenUrl`, `Close Browser` |
| Excel | Открыть и закрыть книгу, создать и удалить лист ([Excel engine](/ToscaBase/ru/engines/excel-engine/)) |
| PDF | Сравнение PDF-файлов ([PDF engine](/ToscaBase/ru/engines/pdf-engine/)) |
| SAP | Модули для приложений SAP |

Каждый из них — готовая функция, которую иначе пришлось бы писать скриптом: открыть URL, закрыть браузер, сравнить файлы, обработать попап. Их можно перетаскивать в любое число TestCase.
