---
title: Repetitions и бизнес-TestCase
description: Многократный запуск execution entry через свойство Repetitions и сборка business TestCase и business ExecutionList в сквозное представление для заинтересованных сторон.
level: 2
sidebar:
  order: 40
sources:
  - id: jQ-UZfAcU9o
    title: "Tosca Tutorial | Lesson 67 - Execute Test Case Multiple Times from Execution Lists | Repetitions |"
    url: https://www.youtube.com/watch?v=jQ-UZfAcU9o
    at: "00:08"
  - id: D9N2HVczgPc
    title: "Tosca Tutorial | Lesson 68 - Use Business Test Cases | Execution Lists | End-to-End Scenarios |"
    url: https://www.youtube.com/watch?v=D9N2HVczgPc
    at: "00:08"
---

Две возможности раздела Execution, которые меняют, *как* выполняется список и *как читаются его результаты*, не трогая сами TestCase: свойство **Repetitions (повторения)** у execution entry и пара **business TestCase (бизнес-TestCase)** плюс **business ExecutionList**, сшивающая несколько ExecutionList в один сквозной результат.

## Повторение execution entry

Свойство `Repetitions` знакомо по папкам TestCase (см. [Repetitions](/ToscaBase/ru/test-cases/repetitions/)). То же свойство есть у **execution entry**, так что TestCase без настроенных внутри повторений всё равно можно прогнать несколько раз из ExecutionList.

1. Перетащите TestCase в ExecutionList; он станет execution entry.
2. Откройте **Properties** записи и задайте `Repetitions`, например `3`.
3. Запустите запись или её папку. Раскрыв запись после прогона, вы увидите три выполнения в логе.

Значения для каждого повторения по-прежнему можно варьировать обычным способом. Выбирайте свойство на уровне записи, когда повторение — решение о выполнении (прогон на стабильность, повтор, прогоны по окружениям), а не часть дизайна теста.

## Business TestCase и business ExecutionList

Отдельные TestCase покрывают по одной функции: регистрация пользователя, вход, обработка заказа. Руководство хочет знать, работает ли **бизнес-процесс**, собранный из них, от начала до конца, возможно через несколько приложений, релизов или прогонов. Business TestCase и business ExecutionList дают такое представление.

- **Business TestCase** — структурный TestCase в разделе TestCases. Он лишь ссылается на другие TestCase и фиксирует их порядок. Выполнить его нельзя.
- **Business ExecutionList** — структурный список в разделе Execution. Он связывает business TestCase и те ExecutionList, чьи результаты к нему относятся. Выполнить его тоже нельзя; он **склеивает результаты** связанных ExecutionList.

### Создание

1. В разделе TestCases создайте папку (например `Business scenarios`), правый клик по ней и выберите пункт с **иконкой портфеля**, создающий business TestCase. Назовите его, например `End-to-end scenario`.
2. Перетащите в него отдельные TestCase в порядке бизнес-процесса: регистрация, вход, обработка заказа.
3. В разделе Execution в соответствующей папке создайте **business ExecutionList** с тем же именем.
4. Перетащите business TestCase на business ExecutionList, чтобы связать их.
5. Перетащите на business ExecutionList отдельные **ExecutionList**, в которых выполнялись эти TestCase, в том же порядке.

Business ExecutionList теперь показывает сводный результат: в примере регистрация и вход прошли, а обработка заказа упала — ровно та фраза, которую нужно сказать бизнесу: процесс сломан на обработке заказа.

:::note
Поскольку оба объекта структурные, у них нет пункта **Run**. Выполняйте базовые ExecutionList как обычно; business ExecutionList отражает их `ActualLog`.
:::

Связанные списки не обязаны относиться к одному приложению или релизу. Перетаскивание ExecutionList из прогонов разных релизов даёт хронологическую картину одного процесса по релизам.

## См. также

- [ExecutionList](/ToscaBase/ru/execution/execution-lists/): создание списков, питающих business ExecutionList.
- [Результаты и логи](/ToscaBase/ru/execution/execution-results-and-logs/): архивирование по релизам, которое сохраняет точность бизнес-представлений.
- [Требования и риск](/ToscaBase/ru/requirements-and-reporting/requirements-and-risk/): те же результаты со стороны требований.
