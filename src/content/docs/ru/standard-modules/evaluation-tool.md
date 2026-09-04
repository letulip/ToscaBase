---
title: TBox Evaluation Tool (инструмент вычисления)
description: TBox Evaluation Tool сравнивает два динамических выражения (буферы, Test Configuration Parameters, литералы) с результатом true/false; используется для верификаций и как условие If, операнды в кавычках.
level: 2
sidebar:
  order: 40
sources:
  - id: IkPL7G4QR7k
    title: "Tosca Tutorial | Lesson 16 - Using TBox Evalutation Tool | Compare Dynamic Expressions|"
    url: https://www.youtube.com/watch?v=IkPL7G4QR7k
    at: "00:10"
  - id: 2sbIUWs5wcI
    title: "Tosca Tutorial | Lesson 126 - Random Mathematical Operations | Evaluation Tool | Obstacle 20 |"
    url: https://www.youtube.com/watch?v=2sbIUWs5wcI
    at: "04:19"
  - id: P387hZrvq_k
    title: "TRICENTIS Tosca 16.0 - Lesson 62 | OBSTACLE #20 | Random Mathematical Operations | Evaluation Tool"
    url: https://www.youtube.com/watch?v=P387hZrvq_k
    at: "08:35"
---

**TBox Evaluation Tool (инструмент вычисления выражений)** — стандартный Module из группы *expression evaluation* стандартного набора. Он вычисляет сравнение и возвращает true или false: true проходит шаг, false его роняет. Единственный ModuleAttribute — **Expression** с ActionMode `Verify` по умолчанию, поскольку шаг является верификацией. Выражение содержит два значения и оператор сравнения (`==`, `!=`, `<`, `>` и т. д.), и каждое значение может быть любым динамическим выражением: буфер с буфером, буфер с Test Configuration Parameter (параметром тестовой конфигурации, TCP), буфер с литералом или вычисляемым выражением. Это универсальный шаг сравнения в Tosca, а внутри `If` — способ построить многовариантное ветвление.

## Сравнение буфера с Test Configuration Parameter

Сценарий: в демонстрационном интернет-магазине нажать Login, войти с email и паролем, хранящимися в Test Configuration Parameters (TCP), и проверить, что имя пользователя отображается на странице.

### Обычный способ

TestStep на контроле с именем пользователя, ActionMode `Verify`, значение `=={CP[username]}`: inner text контрола сравнивается с TCP. Это работает, лог показывает ожидаемое и фактическое значения.

### Через Evaluation Tool

1. Отключите старый шаг верификации: правый клик на шаге, **Disable**. Tosca спросит причину (необязательно) и запишет время и пользователя.
2. Добавьте TestStep на Module для контрола имени пользователя, ActionMode `Buffer`, имя буфера `email`. Поставьте его перед сравнением.
3. Добавьте **TBox Evaluation Tool**, переименуйте в `Compare email` и введите выражение `{B[email]}=={CP[username]}`.
4. Запустите. Шаг **падает** с сообщением в логе о *missing end of file*: значения содержат специальные символы, ломающие разбор выражения.
5. Заключите оба операнда в кавычки: `'{B[email]}'=='{CP[username]}'`. Запустите снова: TestCase входит, Evaluation Tool вычисляется в true, буфер `email` виден со значением, шаг выхода подтверждает, что сценарий прошёл.

:::tip
Всегда заключайте операнды выражения Evaluation Tool в **одинарные кавычки**. Это экранирует специальные символы в значениях и исправляет ошибку «missing end of file». То же правило действует, когда выражение используется как условие `If`.
:::

Сценарий — один из самых частых в веб-автоматизации, и оба способа его решают; вариант с Evaluation Tool более динамичен, потому что любую сторону сравнения можно заменить любым выражением, не трогая Module.

## Как условие If: рандомизированная арифметика

«Препятствие» автоматизации показывает два случайных числа и случайный оператор (`+`, `-`, `*` или остаток от деления); обновление страницы меняет все три. Тест должен вычислить результат и ввести его в поле результата. В языке программирования взяли бы `switch`/`case`; в Tosca switch нет, поэтому шаблон — один `If` на оператор с Evaluation Tool в качестве условия.

### Module

Отсканируйте страницу в Module с четырьмя контролами: первое число, оператор, второе число, поле результата. Поскольку числа и оператор меняются при каждой загрузке, **переименуйте ModuleAttributes** в стабильные имена (`Num1`, `Operand`, `Num2`, `Result`); иначе TestCase покажет значения, захваченные при сканировании. См. [Свойства и параметры Module](/ToscaBase/ru/modules/module-properties-and-parameters/).

### TestCase

1. **Буферизация значений.** Один TestStep с ActionMode `Buffer` для `Num1`, `Operand` и `Num2`.
2. **If (сложение).** Правый клик на TestCase, **Create If statement**. Под *Condition* добавьте шаг **TBox Evaluation Tool** (ActionMode `Verify`) с выражением `'{B[Operand]}'=='+'`.
3. **Then.** Перетащите Module под *Then* и введите в `Result` значение `{MATH[{B[Num1]}+{B[Num2]}]}` с ActionMode `Input`.
4. Скопируйте блок `If` три раза, меняя только оператор в условии (`-`, `*`, знак остатка) и внутри выражения `MATH`.
5. Установите workstate Completed и запустите несколько раз, нажимая между прогонами *Try again* на странице. Каждый запуск буферизует другие значения, срабатывает ровно один `If`, поле результата получает верное значение.

:::note
В уроке 126 оператор и выражение видны только на экране; урок 62 (Tosca 16) проговаривает их так, как записано выше. Синтаксис `MATH` описан в разделах [Строковые операции](/ToscaBase/ru/expressions/string-operations/) и [Случайные значения](/ToscaBase/ru/expressions/random-values/).
:::

Четыре последовательных блока `If` не элегантны, но это единственный способ выразить многовариантное ветвление в Tosca. По сути получается автоматизированный калькулятор.

## См. также

- [Управление потоком](/ToscaBase/ru/test-cases/control-flow/) об `If`, `Do` и `While`
- [Операции с буферами](/ToscaBase/ru/standard-modules/buffer-operations/)
- [Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/)
- [Случайные значения](/ToscaBase/ru/expressions/random-values/)
