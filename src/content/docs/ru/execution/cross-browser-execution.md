---
title: Кросс-браузерное выполнение
description: Запуск одного TestCase в нескольких браузерах через Test Configuration Parameter Browser, берущий значение из Buffer, и исправление ошибки «No feasible executor found», вызванной TestStep без Module.
level: 2
sidebar:
  order: 70
sources:
  - id: 8tXcwf0qLx8
    title: "Tosca Tutorial | Lesson 144 - Common Problems & Fixes | Cross Browser Testing | Multiple Browsers |"
    url: https://www.youtube.com/watch?v=8tXcwf0qLx8
    at: "00:12"
  - id: h8u3f4AU4_I
    title: "Tosca Tutorial | Lesson 143 - Common Problems & Fixes | No Feasible Executor Found | Execution |"
    url: https://www.youtube.com/watch?v=h8u3f4AU4_I
    at: "00:12"
---

В каком браузере выполняется веб-TestCase, решает Test Configuration Parameter `Browser`, одно значение на прогон. Это отвечает на «сегодня в Chrome, завтра в Firefox», но не на «прогнать этот TestCase в Chrome *и* Edge в одном выполнении», а это и частое требование проекта, и популярный вопрос на собеседовании. Приём в том, чтобы сделать параметр динамическим. Вторая половина документа посвящена ошибке выполнения, которая выглядит как проблема браузера или агента, но ею не является.

## Один браузер на прогон

На TestCase или ExecutionList откройте **Test Configuration** и добавьте Test Configuration Parameter `Browser`; выберите браузер из списка (Chrome, Firefox, Edge...). Меняйте значение перед каждым прогоном, чтобы переключить браузер. Механизм параметров описан в [Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/).

## Несколько браузеров в одном TestCase

Вместо константы дайте `Browser` **ссылку на Buffer (буфер)**, а затем задавайте этот Buffer внутри TestCase перед каждой частью, которая должна выполняться в другом браузере.

1. Разбейте TestCase на папки, по одной на прогон в браузере. В демо папка `Login process` (Open URL, Close Browser) копируется, получаются `Login process 1` и `Login process 2`; из первой Close Browser убирается.
2. В **Test Configuration** TestCase задайте `Browser` как ссылку на Buffer; в демо это `{B[B_browser]}` для Buffer с именем `B_browser`.
3. **Первым TestStep** каждой папки добавьте **TBox Set Buffer** (см. [Операции с буферами](/ToscaBase/ru/standard-modules/buffer-operations/)): имя Buffer `B_browser`, значение `Chrome` в первой папке, `Edge` во второй.
4. Запустите. В логе видно, как Buffer получает `Chrome`, URL открывается в Chrome, затем Buffer получает `Edge` и URL открывается в Edge; шаг Close Browser закрывает браузер, открытый текущей папкой.

Поскольку браузер читается из Buffer в момент каждого Open URL, один TestCase покрывает столько браузеров, сколько у вас шагов Set Buffer. Дублировать TestCase на каждый браузер и поднимать распределённое выполнение для этого не нужно.

Имя Buffer — на ваш выбор, оно лишь должно совпадать в шаге Set Buffer и ссылке `{B[...]}`.

Если первая папка не закрывает свой браузер, он остаётся открытым после прогона, что демо и показывает для Chrome.

## «Unable to run the selected items. No feasible executor was found»

Эта ошибка появляется при запуске TestCase, ExecutionList или TestEvent. Её легко принять за проблему окружения выполнения, особенно у TestEvent, где она намекает на сломанный DEX-агент. Обычная причина гораздо проще: **TestStep больше не ссылается на Module**.

Иногда сообщение содержит причину («this TestStep is not referencing a Module»), иногда показывается только первая строка.

### Как это происходит

Откройте TestCase и посмотрите на проблемный TestStep: значения на месте, но ModuleAttribute не привязан и **Jump to Module** не предлагается. Module, из которого строился шаг, был удалён, заменён или переименован в workspace. В многопользовательском workspace это обычно чья-то чистка Module; Tosca предупреждает при удалении, что Module используется TestStep, но удаление всё равно можно продолжить. Стандартные Module вроде Open URL и Close Browser удалить нельзя, так что виновник — прикладной Module.

Одного осиротевшего шага достаточно, чтобы весь TestCase не запускался, хотя остальные шаги в порядке.

### Исправление

1. Удалите осиротевший TestStep. TestCase (и содержащий его ExecutionList или TestEvent) сразу снова запускается.
2. Чтобы восстановить покрытие, пересканируйте приложение, создайте Module заново и верните TestStep.

См. [Гигиена Module](/ToscaBase/ru/best-practices/module-hygiene/) о том, как чистить Module, не ломая TestCase, и [Rescan Modules](/ToscaBase/ru/modules/rescan-modules/) о пересканировании.
