---
title: ExecutionList
description: Почему ExecutionList приходит на смену ScratchBook, когда TestCase готов, как собрать список из папок и TestCase, запустить его и держать в синхронизации с разделом TestCases.
level: 2
sidebar:
  order: 10
sources:
  - id: H16RSCy6e_g
    title: "Tosca Tutorial | Lesson 59 - Execute Test Cases | Execution Lists | Test Results | Execution Entry|"
    url: https://www.youtube.com/watch?v=H16RSCy6e_g
    at: "00:02"
  - id: mFptsa3Wuts
    title: "Tricentis Tosca Tutorial Part-6 : Tosca Execution, Tosca Execution List, Dokusnapper"
    url: https://www.youtube.com/watch?v=mFptsa3Wuts
    at: "01:17"
  - id: c42YuuEksL0
    title: "Tosca Tutorial | Lesson 61 - Synchronize Execution List with Test Cases | Execution Lists |"
    url: https://www.youtube.com/watch?v=c42YuuEksL0
    at: "00:06"
---

**ExecutionList (список выполнения)** — это набор готовых к запуску TestCase вместе со всеми результатами, которые эти запуски когда-либо дали. Он живёт в разделе **Execution** workspace и является рекомендуемым способом выполнять тесты после завершения разработки: в отличие от ScratchBook, его логи сохраняются, так что позже можно отлаживать, строить отчёты и сравнивать итерации.

## ScratchBook и ExecutionList

Tosca запускает TestCase в двух местах.

| | ScratchBook | ExecutionList |
|---|---|---|
| Назначение | Пробный прогон, проверка готовности TestCase | Настоящее выполнение, результаты хранятся |
| Как запустить | Правый клик по TestCase (или отдельному TestStep) > **Run in ScratchBook** | Правый клик по execution entry, папке или списку > **Run** |
| Нужен ли check-out | Нет | Да, ExecutionList должен быть взят на check-out |
| Результаты | Временные, исчезают при закрытии ScratchBook | Хранятся в `ActualLog`, пока вы их не очистите или не заархивируете |

Tricentis советует использовать ScratchBook только для пробных прогонов. В обоих случаях каждый TestStep в логе получает зелёную галочку при успехе и красный крест при сбое, включая шаги верификации.

## Где находится раздел Execution

Если зелёная папка **Execution** не видна на домашней странице, откройте её из списка разделов и закрепите рядом с **TestCases**, чтобы перетаскивать между ними. В новом проекте уже есть объекты по умолчанию: ExecutionList с примерами стандартных модулей, виртуальные папки, Exploratory Testing, Interactive Testing, **Configurations** и **TestEvents** (последние два относятся к [распределённому выполнению](/ToscaBase/ru/execution/distributed-execution-dex/)).

## Создание ExecutionList

ExecutionList нельзя создать прямо в корне Execution; сначала нужна **папка ExecutionList (ExecutionList folder)**.

1. Возьмите на check-out папку Execution (или вашу родительскую папку).
2. Правый клик > **Create ExecutionList folder** (есть и как иконка на панели) и переименуйте её, например по названию приложения или релиза.
3. Правый клик по новой папке > **Create ExecutionList** и задайте имя.
4. Добавьте TestCase **перетаскиванием** из раздела TestCases. Перетаскивание целой папки TestCase воссоздаёт ту же структуру папок внутри списка; отдельные TestCase добавляются по одному. Можно и вручную собрать внутри списка свою структуру папок, например по функциональности.
5. Сделайте **check in**, чтобы сохранить список в общий репозиторий.

Каждый TestCase, добавленный в список, становится **execution entry (записью выполнения)**; папки становятся **execution entry folder**. У списка есть вкладка **Test Configuration**, где показаны Test Configuration Parameter, заданные при разработке TestCase; изменение там действует только на этот ExecutionList (см. [Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/)).

## Запуск ExecutionList

1. Возьмите ExecutionList на check-out.
2. Выберите одну execution entry, несколько, папку или весь список, правый клик > **Run**. (Соседний пункт **Run as manual TestCase** описан в [Ручное выполнение](/ToscaBase/ru/execution/manual-execution/).)
3. Tosca выполняет записи одну за другой, обрабатывает результаты и возвращает вас к списку.
4. Снова сделайте check in, чтобы результаты постоянно хранились в репозитории.

Панель **Details** показывает результат по каждой записи; раскройте запись, чтобы увидеть, какие TestStep прошли, а какие упали. Через **column chooser** добавьте колонки: summary, время начала и конца, длительность. Результаты остаются в списке, пока вы их не удалите или не заархивируете; как читать, настраивать и экспортировать их — в [Результаты и логи](/ToscaBase/ru/execution/execution-results-and-logs/).

## Синхронизация списка с TestCase

Execution entry — это ссылки на TestCase, а не копии. Часть изменений из раздела TestCases попадает в ExecutionList автоматически, для остальных нужен ручной **Synchronize**.

Синхронизируется автоматически:

- правка TestStep или значений внутри TestCase,
- переименование TestCase.

Не синхронизируется автоматически, нужен правый клик по ExecutionList (или папке) > **Synchronize**:

- переименование папки TestCase (execution entry folder сохраняет старое имя до синхронизации),
- перемещение TestCase в другую папку или удаление из папки (запись остаётся на месте до синхронизации, затем исчезает из старого места),
- добавление нового TestCase в папку, которая уже есть в списке (новая запись появится только после синхронизации).

:::tip
Синхронизация нужна только если вы продолжаете перестраивать TestCase после создания ExecutionList. Если список создан после окончания разработки и дальше правятся только TestStep, она не понадобится никогда. Другие уроки (например, [Recovery и Cleanup Scenarios](/ToscaBase/ru/test-cases/recovery-and-cleanup-scenarios/)) всё же советуют делать **Synchronize** после любого изменения TestCase «на всякий случай»; это безвредно, так что при сомнениях синхронизируйте перед запуском.
:::

## См. также

- [Результаты и логи](/ToscaBase/ru/execution/execution-results-and-logs/): чтение `ActualLog`, трендовые диаграммы, архивирование и экспорт в Excel.
- [Repetitions и бизнес-TestCase](/ToscaBase/ru/execution/execution-repetitions-and-business-test-cases/): многократный запуск записи и сборка сквозных представлений.
- [DokuSnapper](/ToscaBase/ru/execution/dokusnapper/): сгенерированный документ со скриншотом на каждый TestStep.
