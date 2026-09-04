---
title: Сценарии восстановления и очистки
description: Как recovery engine Tosca повторяет упавший TestCase - включение восстановления глобально или на папке, создание Recovery Scenario Collection, настройка Retry level и добавление Cleanup Scenario на случай, если само восстановление упадёт.
level: 1
sidebar:
  order: 50
sources:
  - id: d_9ugVdRpZY
    title: "Tosca Tutorial | Lesson 49 - Create Recovery Scenarios | Handle Unexpected Errors | Recovery Engine"
    url: https://www.youtube.com/watch?v=d_9ugVdRpZY
    at: "00:02"
  - id: 2xPO0SHEHLo
    title: "Tosca Tutorial | Lesson 50 - Add Cleanup Scenarios to Test Cases | Recovery Engine |"
    url: https://www.youtube.com/watch?v=2xPO0SHEHLo
    at: "00:55"
---

Любому инструменту автоматизации приходится справляться с неожиданными сбоями; в коде вы написали бы блок try/catch. В Tosca вместо этого есть **recovery engine** (движок восстановления): вы определяете набор TestStep, называемый **Recovery Scenario** (сценарий восстановления), и когда TestCase падает, Tosca выполняет эти шаги, а затем повторяет упавшую часть. Если шаги восстановления тоже падают, **Cleanup Scenario** (сценарий очистки) возвращает приложение в известное состояние, чтобы оставшиеся TestStep всё же могли выполниться. Вместе они не дают долгому прогону остановиться на первой неожиданности; сбои вы разбираете потом, не теряя весь прогон.

## Настройка восстановления в три шага

1. **Включить восстановление** - для всего workspace в настройках или для папки через Test Configuration Parameters.
2. **Создать Recovery Scenario** на папке TestCase или на отдельном TestCase.
3. **Задать свойство Retry level** сценария, чтобы Tosca знала, при каком сбое его запускать.

Все три шага обязательны.

### Шаг 1a: включить глобально

**Settings > TBox > Recovery** перечисляет три типа сбоев, у каждого одни и те же четыре возможных значения:

| Настройка | Срабатывает при |
|---|---|
| **On dialog failure** | Tosca больше не может взаимодействовать с приложением (сбой на уровне диалога) |
| **On exception failure** | Исключение во время выполнения |
| **On verification failure** | Падение шага `Verify` |

| Значение | Смысл |
|---|---|
| Halt execution | Полностью остановить |
| Execute next test case | Перейти к следующему TestCase |
| Continue execution | Продолжить со следующего шага |
| Recover | Выполнить Recovery Scenario |

Выберите **Recover** для каждого типа сбоя, который должны обрабатывать сценарии восстановления. Ещё три настройки в том же диалоге ограничивают число попыток: **TestCase retries**, **TestStep retries** и **TestStepValue retries** - максимальное число попыток восстановления на TestCase, TestStep и TestStepValue соответственно. Допустимы любые значения; они могут различаться. Закройте диалог - восстановление включено для всех объектов workspace.

### Шаг 1b: включить на папке

Если разным папкам нужно разное поведение, задайте те же опции как Test Configuration Parameters на папке TestCase; для этой папки они переопределяют глобальные настройки.

1. Выделите папку и откройте вкладку **Test Configuration**.
2. **Create Test Configuration Parameter**, выберите `On dialog failure`, поставьте `Recover`. Повторите для `On exception failure` и `On verification failure`.
3. Добавьте `TestCase retries`, `TestStep retries` и `TestStepValue retries` с нужными числами (в источнике 1, 2 и 2).

Механизм описан в [Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/).

### Шаг 2: создать Recovery Scenario

1. Щёлкните правой кнопкой по папке TestCase и выберите **Create Recovery Scenario Collection** (**Ctrl+N**, **Ctrl+R**). Tosca добавит папку `Recovery Scenarios` (значок с белым плюсом).
2. Щёлкните правой кнопкой по этой папке и выберите **Create Recovery Scenario** (значок с красным плюсом). Коллекция может содержать несколько сценариев.
3. Добавьте TestStep, которые должны выполняться при срабатывании восстановления, - точно как в обычном TestCase.

### Шаг 3: задать Retry level

Откройте свойства Recovery Scenario и поставьте **Retry level** в `TestCase`, `TestStep` или `TestStepValue`. Это определяет, какой сбой запускает восстановление: падение всего TestCase, одного TestStep или одного TestStepValue. В источнике оставлено `TestCase`.

## Рабочий пример

На странице есть кнопка `Submit`, которая после недавнего изменения недоступна около 13 секунд после загрузки. TestCase: `OpenUrl`; на `Submit` - `Verify` `Enabled == True`, затем клик `X`; закрыть страницу. Он падает на проверке, потому что кнопка ещё не доступна.

Recovery Scenario содержит один TestStep на той же кнопке с ActionMode `WaitOn` и значением `Enabled == True`, переименованный в `Check submit`. Retry level - `TestCase`, TestCase retries - 1. Запуск папки из ExecutionList даёт такой лог:

1. Проверка `Submit enabled` падает.
2. Recovery engine запускает Recovery Scenario; `Check submit` ждёт, пока кнопка станет доступной.
3. TestCase выполняется заново: проверка теперь проходит, клик выполняется, TestCase проходит.

При retries = 1 попытка одна. Если сценарию нужно больше, поднимите `TestCase retries`; Tosca прекращает повторы, как только TestCase прошёл, иначе продолжает, пока счётчик не исчерпан.

:::caution
Recovery Scenario выполняются только когда TestCase запущен из **ExecutionList**. В ScratchBook сценарий игнорируется, и TestCase просто падает.
:::

:::tip
Правки TestStep и значений внутри TestCase попадают в запись ExecutionList автоматически. **Synchronize** (правой кнопкой по ExecutionList) строго необходим только при структурных изменениях - переименовании или перемещении папок и добавлении новых TestCase; запускать его после любого изменения - безвредная предосторожность. См. [ExecutionList](/ToscaBase/ru/execution/execution-lists/).
:::

В примере внутри восстановления используется `WaitOn` - это обходной путь для отсутствующего шага синхронизации; в реальном проекте вы бы ещё и починили TestCase. Восстановление - для сбоев, которые вы не предвидели. Про `WaitOn` см. [Режимы действия](/ToscaBase/ru/test-cases/action-modes/).

## Cleanup Scenario

Recovery Scenario меняет состояние приложения так, чтобы повтор мог пройти. Если само восстановление падает, приложение застревает в состоянии, из которого упадёт и каждый следующий TestStep. **Cleanup Scenario**, тоже часть recovery engine, выполняется, когда сценарий восстановления упал, и содержит TestStep, возвращающие приложение в исходное состояние: например, перезапустить приложение, войти и вернуться на страницу, где следующие шаги ожидают оказаться.

### Создание

Cleanup Scenario требует существующей Recovery Scenario Collection.

1. Щёлкните правой кнопкой по папке `Recovery Scenarios` и выберите **Create Cleanup Scenario** (**Ctrl+N**, **Ctrl+C**).
2. Добавьте шаги очистки. В примере это копии собственных шагов TestCase `Close URL` и `Open URL`.

### Продолжение примера

В TestCase добавляется ещё один шаг: клик по ссылке `Open new page`, открывающей ту же страницу в другой вкладке. Если `Submit` всё ещё недоступен и восстановление упало, ссылку тоже не кликнуть; переоткрытие страницы делает её кликабельной, минуя кнопку. В логе ExecutionList:

1. `Submit enabled` падает.
2. Recovery Scenario выполняется и тоже падает.
3. Выполняется Cleanup Scenario: `Close URL`, `Open URL`.
4. Выполнение продолжается оставшимися TestStep, которые без очистки были бы заблокированы.

## См. также

- [Управление потоком](/ToscaBase/ru/test-cases/control-flow/) - когда ситуация это известное условие, а не сбой: `If` дешевле восстановления.
- [ExecutionList](/ToscaBase/ru/execution/execution-lists/) и [Результаты и логи выполнения](/ToscaBase/ru/execution/execution-results-and-logs/) - чтение записей о восстановлении в логе.
