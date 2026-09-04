---
title: Режим self-healing
description: Что делает режим self-healing в Tosca, когда контрол меняется в новой сборке, как self-healing properties захватываются в XScan, как включить режим через Test Configuration Parameter SelfHealing и как «вылеченные» шаги отображаются в логе и применяются к Module.
level: 2
sidebar:
  order: 120
sources:
  - id: c_zKy9iBeME
    title: "TRICENTIS Tosca 16.0 - Lesson 26 | Enable Self-healing Mode | Self-healing Test Cases | AI Powered"
    url: https://www.youtube.com/watch?v=c_zKy9iBeME
    at: "01:05"
---

**Self-healing mode (режим самовосстановления)** позволяет TestCase продолжать выполнение, когда контрол в тестируемой системе изменился. Классический случай — новая сборка: у кнопки меняется идентифицирующее свойство, Module больше не совпадает, и каждый TestCase с этим Module падает, пока кто-нибудь не пересканирует его. При включённом self-healing Tosca обращается к набору **self-healing properties (свойств самовосстановления)**, сохранённых вместе с ModuleAttribute, всё равно находит контрол, помечает шаг в логе как «вылеченный» и позволяет одним кликом записать новую идентификацию обратно в Module. Выигрыш — более стабильные прогоны, явный список изменившихся контролов и куда меньше сопровождения Module после каждой сборки.

Tricentis описывает процесс в четыре шага: создать TestCase на Module, атрибуты которых несут self-healing properties, включить режим self-healing для TestCase, поместить TestCase в [ExecutionList](/ToscaBase/ru/execution/execution-lists/) и запустить. Урок записан на Tosca 2023, но утверждает, что функция одинаково есть в 15, 16 и 2023.

## Self-healing properties в Module

Self-healing работает только для ModuleAttribute, у которых есть self-healing properties. XScan добавляет их автоматически при сканировании или пересканировании контрола; какие оставить — решаете вы.

1. Отсканируйте контрол как обычно ([XScan](/ToscaBase/ru/modules/xscan/)). Свойства идентификации, например `Tag` = `input` и `Value` = `Sign in` для кнопки, выбираются как раньше ([Идентификация контролов](/ToscaBase/ru/modules/control-identification/)).
2. В окне сканирования переключите вид свойств на **Self-healing properties**. XScan перечисляет кандидатов: `Label`, `ClassName`, `Id`, `Name`, `Tag`, `Title`, `Value`, `Type`, `XPath` и action point. Отметьте стабильные и непустые (в уроке — `XPath`, `Tag`, `Type`, `ClassName`, `Value` и action point; `Id` и `Name` были пустыми и не взяты). Снимите отметку со свойства, уже используемого для идентификации, если ожидаете, что оно изменится.
3. Сохраните Module. В Tosca Commander у ModuleAttribute теперь есть вкладка **Self-healing properties** рядом с **Details**, где каждое свойство показано с весом: в уроке `Tag` 0.25, `Type` 0.5, `ClassName`, `XPath`, `Value` и action point — 1.0. Веса назначает Tosca, и они питают взвешенный алгоритм, описанный ниже.

:::tip
Захватывайте self-healing properties при **первом** сканировании. Если Module был отсканирован без них, контрол вылечить нельзя; придётся [пересканировать](/ToscaBase/ru/modules/rescan-modules/) его, пока приложение ещё совпадает с Module.
:::

## Включение режима

Self-healing включается через [Test Configuration Parameter](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/), поэтому его можно задать на TestCase, папке или ExecutionList:

1. Откройте вкладку **Test Configuration** у TestCase и создайте параметр; выберите `SelfHealing` из выпадающего списка.
2. Выберите значение:

| Значение | Поведение |
|---|---|
| `Weighted` | Использует веса self-healing properties, чтобы найти наиболее уникальный контрол |
| `Combination` | Перебирает все возможные комбинации сохранённых self-healing properties, пока одна из них не идентифицирует подходящий контрол |
| `False` | Self-healing выключен (по умолчанию) |

В уроке на TestCase заданы `Browser` = Edge и `SelfHealing` = `Combination`, а запуск сделан прямо из TestCase; документированный процесс запускает его из ExecutionList.

## Как отображается вылеченный шаг

Урок имитирует новую сборку, переименовав в браузере кнопку входа с `Sign in` на `Login` (Module идентифицировал её по `Value` = `Sign in`).

- **Без self-healing** шаг падает с обычным сообщением, что контрол не найден.
- **С self-healing** шаг проходит, а лог выполнения помечает его **иконкой self-healing** (символ сердца). Раскрыв шаг, вы видите метод (`Combination`), значение certainty (уверенности), сколько комбинаций перебрано (семь) и какое свойство в итоге дало уникальный контрол (`ClassName`).

TestCase, таким образом, доходит до конца, а лог заодно служит списком всех контролов, чья идентификация больше не работает.

## Применение найденной идентификации

Вылеченный шаг — обходной путь, а не исправление: следующий прогон будет лечить снова. Чтобы закрепить результат, кликните правой кнопкой по вылеченному шагу в логе > **Apply self-healing properties**. Tosca заменяет старое свойство идентификации в ModuleAttribute на найденное (`ClassName` вместо `Value` в уроке); сохраните Module, и TestCase выполняется штатно.

## Ограничения

- Лечатся только контролы, отсканированные с self-healing properties; для атрибутов без них ничего не угадывается.
- Для лечения нужно хотя бы одно стабильное свойство в сохранённом наборе. Если изменились все сохранённые свойства или найденное свойство подходит нескольким контролам, шаг всё равно падает.
- Функция включается через параметр на TestCase, папке или ExecutionList, а не глобально; TestCase без `SelfHealing` ведёт себя как раньше.
- Self-healing скрывает поломку, пока вы не заглянете в лог. Просматривайте вылеченные шаги после каждого прогона и применяйте или пересканируйте, иначе Module разойдутся с приложением.

## См. также

- [Идентификация контролов](/ToscaBase/ru/modules/control-identification/): свойства идентификации, от которых self-healing отступает к запасным
- [Пересканирование Module](/ToscaBase/ru/modules/rescan-modules/): ручная альтернатива при изменении контрола
- [Результаты и логи](/ToscaBase/ru/execution/execution-results-and-logs/): чтение лога выполнения
