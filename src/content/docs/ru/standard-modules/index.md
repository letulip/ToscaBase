---
title: Стандартные модули
description: Модули TBox Automation Modules, входящие в поставку Tosca, для файлов, папок, буферов, процессов, скриншотов, окон и JavaScript.
sidebar:
  order: 0
---

Tosca поставляется с библиотекой готовых модулей — **Standard modules (стандартные модули)**, они же TBox Automation Modules. Они покрывают общие операции, нужные TestCase вокруг тестируемого приложения, и добавляются через **Add TestStep** без сканирования. Раздел описывает каждую группу: что делает модуль, его ModuleAttributes и подводные камни.

| Документ | Содержание |
|---|---|
| [Операции с файлами и папками](/ToscaBase/ru/standard-modules/file-and-folder-operations/) | Создание, копирование, сравнение и удаление файлов и папок; проверка существования папки |
| [Операции с буферами](/ToscaBase/ru/standard-modules/buffer-operations/) | Set Buffer, Partial Buffer, Name to Buffer, Delete Buffer |
| [Запуск и закрытие программ](/ToscaBase/ru/standard-modules/start-and-close-programs/) | TBox Start Program с аргументами, закрытие программ через taskkill, Start/Stop Timer |
| [Evaluation tool](/ToscaBase/ru/standard-modules/evaluation-tool/) | TBox Evaluation Tool: сравнение динамических выражений, условие If, математика по оператору |
| [Скриншоты при сбое](/ToscaBase/ru/standard-modules/screenshots-on-failure/) | TBox Take Screenshot и настройка проекта для автоматических скриншотов |
| [Операции с окнами](/ToscaBase/ru/standard-modules/window-operations/) | TBox Window Operation, закрытие попапов, TBox Scroll Window Operation |
| [Диалоги рабочего стола](/ToscaBase/ru/standard-modules/desktop-dialogs/) | TBox Save As для диалога Windows Save As и его окна подтверждения |
| [Выполнение JavaScript](/ToscaBase/ru/standard-modules/execute-javascript/) | Execute JavaScript и Verify JavaScript Result в TBox XEngines > HTML |

Читайте по порядку: файловые и буферные операции нужны почти каждому TestCase, модули процессов и окон вступают в игру для настольных приложений, а JavaScript-модули — запасной вариант для веб-сценариев, которые HTML engine не выражает напрямую.
