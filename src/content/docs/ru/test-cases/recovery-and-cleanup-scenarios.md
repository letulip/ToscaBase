---
title: Сценарии восстановления и очистки
description: Как recovery engine Tosca повторяет упавший TestCase — включение восстановления глобально или на папке, создание Recovery Scenario Collection, настройка Retry level и добавление Cleanup Scenario на случай, когда TestCase восстановить не удаётся.
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
  - id: DWTkzYY0G7A
    title: "TRICENTIS Tosca 16.0 - Lesson 20 | Recovery Scenarios | Recovery Scenarios TestCase &TestStep Level"
    url: https://www.youtube.com/watch?v=DWTkzYY0G7A
    at: "01:03"
  - id: fx3rD0s5DxM
    title: "TRICENTIS Tosca 16.0 - Lesson 21 | Cleanup Scenarios | Recovery Scenarios  | Execution List"
    url: https://www.youtube.com/watch?v=fx3rD0s5DxM
    at: "01:01"
---

Любому инструменту автоматизации приходится справляться с неожиданными сбоями; в коде вы написали бы блок try/catch. В Tosca вместо этого есть **recovery engine** (движок восстановления): вы определяете набор TestStep, называемый **Recovery Scenario** (сценарий восстановления), и когда TestCase падает, Tosca выполняет эти шаги, а затем повторяет упавшую часть. Если восстановление не помогает, **Cleanup Scenario** (сценарий очистки) возвращает приложение в известное состояние, чтобы следующий TestCase всё же мог выполниться. Вместе они не дают долгому прогону остановиться на первой неожиданности; сбои вы разбираете потом, не теряя весь прогон.

## Настройка восстановления в три шага

1. **Включить восстановление** — для всего workspace в настройках или для папки через Test Configuration Parameters.
2. **Создать Recovery Scenario** в Recovery Scenario Collection, которая может находиться где угодно в секции TestCases: на папке или на отдельном TestCase.
3. **Задать свойство Retry level** сценария, чтобы Tosca знала, при каком сбое его запускать.

Все три шага обязательны.

### Шаг 1a: включить глобально

**Project > Settings > TBox > Recovery** перечисляет три типа сбоев, у каждого одни и те же четыре возможных значения:

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

Выберите **Recover** для каждого типа сбоя, который должны обрабатывать сценарии восстановления. Ещё три настройки в том же диалоге ограничивают число попыток: **TestCase retries**, **TestStep retries** и **TestStepValue retries** — максимальное число попыток восстановления на TestCase, TestStep и TestStepValue соответственно. Допустимы любые значения; они могут различаться. Закройте диалог — восстановление включено для всех объектов workspace.

### Шаг 1b: включить на папке

Если разным папкам нужно разное поведение, задайте те же опции как Test Configuration Parameters на папке TestCase; для этой папки они переопределяют глобальные настройки.

1. Выделите папку и откройте вкладку **Test Configuration**.
2. **Create Test Configuration Parameter**, выберите `On dialog failure`, поставьте `Recover`. Повторите для `On exception failure` и `On verification failure`.
3. Добавьте `TestCase retries`, `TestStep retries` и `TestStepValue retries` с нужными числами (в источнике 1, 2 и 2).

Механизм описан в [Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/).

### Шаг 2: создать Recovery Scenario

1. Щёлкните правой кнопкой по папке TestCase (или по TestCase) и выберите **Create Recovery Scenario Collection** (**Ctrl+N**, **Ctrl+R**). Tosca добавит папку `Recovery Scenarios` (значок с белым плюсом).
2. Щёлкните правой кнопкой по этой папке и выберите **Create Recovery Scenario** (значок с красным плюсом). Коллекция может содержать несколько сценариев: если первый падает, Tosca переходит к следующему сценарию в коллекции.
3. Добавьте TestStep, которые должны выполняться при срабатывании восстановления, — точно как в обычном TestCase.

### Шаг 3: задать Retry level

Откройте свойства Recovery Scenario и поставьте **Retry level** в `TestCase`, `TestStep` или `TestStepValue`. Это определяет, что Tosca выполнит заново после успешного восстановления: весь TestCase, упавший TestStep или упавший TestStepValue. Оба источника оставляют `TestCase`.

## Рабочие примеры

**Кнопка, которая ещё не готова.** Кнопка `Submit` недоступна около 13 секунд после загрузки. TestCase: `OpenUrl`; на `Submit` — `Verify` `Enabled == True`, затем клик `X`; закрыть страницу. Он падает на проверке. Recovery Scenario содержит один TestStep на той же кнопке с ActionMode `WaitOn` и значением `Enabled == True`; Retry level — `TestCase`, TestCase retries — 1. Запуск папки из ExecutionList даёт такой лог:

1. Проверка `Submit enabled` падает.
2. Recovery engine запускает Recovery Scenario; `WaitOn` ждёт, пока кнопка станет доступной.
3. TestCase выполняется заново: проверка теперь проходит, клик выполняется, TestCase проходит.

При retries = 1 попытка одна. Если сценарию нужно больше, поднимите `TestCase retries`; Tosca прекращает повторы, как только TestCase прошёл, иначе продолжает, пока счётчик не исчерпан.

**Оставшаяся сессия.** TestCase входа и выхода из урока 20 падает, когда браузер уже залогинен с предыдущего прогона: ссылка `Login` не находится. Recovery Scenario на том же Module верхнего меню кликает `Logout` (`X`), ждёт через `WaitOn` `Visible == True`, пока `Login` снова появится, и закрывает браузер (`Close Browser`, заголовок `Demo*`). В логе ExecutionList видно сбой, восстановление, которое выходит из системы и закрывает окно, и повторный TestCase, открывающий свежий браузер и проходящий.

:::caution
Recovery Scenario и Cleanup Scenario выполняются только когда TestCase запущен из **ExecutionList**. В ScratchBook они игнорируются, и TestCase просто падает.
:::

:::tip
Правки внутри TestCase попадают в запись ExecutionList автоматически; **Synchronize** (правой кнопкой по ExecutionList) нужен только после структурных изменений вроде перемещённых папок или новых TestCase. См. [ExecutionList](/ToscaBase/ru/execution/execution-lists/).
:::

В обоих примерах внутри восстановления используется `WaitOn`, латающий отсутствующий шаг синхронизации или предусловия; в реальном проекте вы бы ещё и починили TestCase. Восстановление — для сбоев, которые вы не предвидели. Про `WaitOn` см. [Режимы действия](/ToscaBase/ru/test-cases/action-modes/).

## Cleanup Scenario

Recovery Scenario меняет состояние приложения так, чтобы повтор мог пройти. Когда TestCase восстановить не удаётся — потому что восстановление упало или потому что в коллекции вообще нет Recovery Scenario, — приложение остаётся в состоянии, из которого упадёт и следующий TestCase. Тогда **Cleanup Scenario**, тоже часть recovery engine и хранящийся в той же коллекции, выполняет TestStep, сбрасывающие приложение: перезапустить его, убрать то, что оставил упавший прогон, выйти из системы — чтобы окружение было готово к следующему TestCase.

### Создание

Cleanup Scenario требует существующей Recovery Scenario Collection; наличия Recovery Scenario в ней он не требует.

1. Щёлкните правой кнопкой по папке `Recovery Scenarios` и выберите **Create Cleanup Scenario** (**Ctrl+N**, **Ctrl+C**).
2. Добавьте шаги очистки. Это могут быть копии собственных шагов TestCase (`Close URL` и `Open URL` в уроке 50) или существующий TestCase, перетащенный в сценарий, как урок 21 делает со своим TestCase опустошения корзины.

### Рабочие примеры

**Восстановление упало.** В TestCase с `Submit` добавляется шаг, кликающий ссылку `Open new page`. Если `Submit` всё ещё недоступен и восстановление упало, ссылку тоже не кликнуть; Cleanup Scenario переоткрывает страницу. В логе ExecutionList: проверка падает, Recovery Scenario выполняется и тоже падает, Cleanup Scenario выполняет `Close URL` и `Open URL`, и выполнение продолжается оставшимися TestStep.

**Без восстановления, только очистка.** TestCase оформления заказа из урока 21 намеренно падает из-за непринятых условий обслуживания: магазин показывает ошибку, и TestCase останавливается с десятью парами джинсов в корзине и открытой сессией; следующий TestCase стартовал бы в этом состоянии. Коллекция на TestCase содержит только Cleanup Scenario, собранный из цикла `While` опустошения корзины из [Управления потоком](/ToscaBase/ru/test-cases/control-flow/) плюс `Logout` и `Close Browser`. В логе ExecutionList TestCase падает, Cleanup Scenario опустошает корзину, выходит из системы и закрывает браузер, и окружение готово к следующему прогону.

## См. также

- [Управление потоком](/ToscaBase/ru/test-cases/control-flow/) — когда ситуация это известное условие, а не сбой: `If` дешевле восстановления.
- [ExecutionList](/ToscaBase/ru/execution/execution-lists/) и [Результаты и логи выполнения](/ToscaBase/ru/execution/execution-results-and-logs/) — чтение записей о восстановлении в логе.
