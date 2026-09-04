---
title: Выполнение JavaScript
description: Запуск JavaScript в браузере модулем Execute JavaScript и проверка возвращаемого значения модулем Verify JavaScript Result; обоим нужен Test Configuration Parameter Browser.
level: 2
sidebar:
  order: 80
sources:
  - id: zZfamr0wZlc
    title: "Tosca Tutorial | Lesson 26 - Execute JavaScript | Verify JavaScript call | TBox HTML Modules |"
    url: https://www.youtube.com/watch?v=zZfamr0wZlc
    at: "00:07"
---

Два стандартных модуля в **Modules > Standard modules > TBox XEngines > HTML** позволяют TestCase выполнять JavaScript в браузере: **Execute JavaScript** запускает скрипт, а **Verify JavaScript Result** запускает скрипт и проверяет возвращённое значение. Через них доступно всё, что JavaScript умеет на странице: переход, действия с элементами, чтение состояния `document`.

## Предварительное условие: Test Configuration Parameter Browser

Оба модуля выбрасывают `InvalidOperationException`, а лог просит задать Test Configuration Parameter (параметр тестовой конфигурации) для браузера, если он не задан. Решение:

1. Выберите TestCase (лучше его папку, чтобы все TestCase его унаследовали) и откройте вкладку **Test Configuration**.
2. Добавьте параметр с именем `Browser` и задайте нужный браузер, например `Chrome`.

См. [Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/).

## Execute JavaScript

| ModuleAttribute | Значение |
|---|---|
| Title | Заголовок окна браузера; подходит регулярное выражение под любой заголовок |
| JavaScript | Выполняемый скрипт |

Пример: перейти на сайт, присвоив `window.location.href` URL демонстрационного магазина (saucedemo). Шаг перенаправляет открытое окно Chrome на эту страницу, и TestCase проходит.

## Verify JavaScript Result

| ModuleAttribute | Значение |
|---|---|
| Title | Заголовок окна, regex допустим |
| JavaScript | Скрипт, который **возвращает** значение |
| Result | Ожидаемое значение; ActionMode `Verify` |

Пример: проверить сессионную cookie после входа.

1. В инструментах разработчика браузера посмотрите cookies сайта: до входа их нет; после входа под стандартным пользователем появляется cookie `session-username` со значением `standard_user`.
2. Title `*` как regex, JavaScript `return document.cookie;`.
3. Result: cookie в виде `имя=значение`, `session-username=standard_user`, ActionMode `Verify`.
4. Выполните. В логе видна успешная верификация с ожидаемым и фактическим значениями.

:::note
Субтитры теряют пунктуацию, поэтому точная строка cookie восстановлена по демонстрационному сайту. Проверьте имя и значение в инструментах разработчика, прежде чем вводить их в атрибут Result.
:::

## См. также

- [Операции с окнами](/ToscaBase/ru/standard-modules/window-operations/)
- [UIA engine и desktop](/ToscaBase/ru/engines/uia-engine-and-desktop/) об обработке JavaScript-алертов
