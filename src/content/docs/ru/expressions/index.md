---
title: Выражения
description: Динамические значения в TestStepValue - случайные данные, расчётные даты, строковые операции, арифметика и регулярные выражения.
sidebar:
  order: 0
---

TestStepValue (значение тестового шага) может быть не только литералом: всё, что записано в фигурных скобках, — динамическое выражение, которое Tosca вычисляет при прогоне. Ввод `{` в ячейке значения открывает список автодополнения со всеми выражениями; **Translate value** в контекстном меню показывает, что выражение выдаст, ещё до запуска TestCase (тестового случая). Этот раздел — справочник по таким выражениям, сгруппированный по назначению.

- [Случайные значения](/ToscaBase/ru/expressions/random-values/) - `RND`, `RNDDECIMAL` и `RANDOMTEXT` для генерируемых данных, а также `MATH` и `SENDKEYS` для расчётов над значениями, которые создаёт приложение, и их ввода обратно.
- [Выражения дат](/ToscaBase/ru/expressions/date-expressions/) - `DATE`, `DATETIME`, `MONTHFIRST`, `LDAY` и родственные выражения с базовой датой, смещением и форматом, а также параметр `ToscaDateFormat`, когда литерал даты не распознаётся.
- [Строковые операции](/ToscaBase/ru/expressions/string-operations/) - `STRINGLENGTH`, `STRINGTOUPPER`/`STRINGTOLOWER`, `NUMBEROFOCCURRENCES`, `TRIM`, `STRINGREPLACE` с экранированием символов, `BASE64` для кодирования и декодирования и `CALC`.
- [Интервалы и выражения проверки](/ToscaBase/ru/expressions/intervals-and-verification-expressions/) - `INTERVAL` для проверки значения в диапазоне, `REGEX` в ModuleAttribute и шагах Verify, многоязычная идентификация через альтернативы и именованные группы, разбивающие значение на буферы.

Выражения обычно сочетаются с буферами (`{B[имя]}`) и параметрами конфигурации (`{CP[имя]}`); о них — в разделе [Буферы](/ToscaBase/ru/data-and-parameters/buffers/). Как ActionMode Verify, Buffer и Input взаимодействуют с выражениями, объясняется в разделе [ActionModes](/ToscaBase/ru/test-cases/action-modes/).
