---
title: Запись выполнения
description: Запись прогонов из ScratchBook и ExecutionList в MP4 через настройку Execution Recorder, ограничение записи сбоями и исключение TestCase параметром AvoidExecutionRecorder.
level: 2
sidebar:
  order: 50
sources:
  - id: piCdpKk86Zc
    title: "Tosca Tutorial | Lesson 70 - Record Test Executions and save it in MP4 format | Debug Errors |"
    url: https://www.youtube.com/watch?v=piCdpKk86Zc
    at: "00:08"
---

Tosca умеет записывать весь экран во время выполнения TestCase и сохранять результат в MP4. Это рассчитано на прогоны, за которыми никто не следит: удалённые или [распределённые](/ToscaBase/ru/execution/distributed-execution-dex/) выполнения и длинные TestCase, где лог говорит, *что* упало, но не *почему*. Запись показывает состояние приложения в момент сбоя без повторного запуска теста.

:::note
**Execution Recorder (рекордер выполнения)** есть только в новых версиях; автор относит его к Tosca 15.1 и выше и показывает на Tosca 16. Если настройки нет, обновите Commander.
:::

## Включение рекордера

**Project > Settings > TBox > Execution Recorder**:

| Настройка | Значение |
|---|---|
| Enable Execution Recorder | По умолчанию выключено. Выбор между записью **всех выполнений** и **только упавших** |
| Output file name template | По умолчанию сочетает имя TestCase и время начала выполнения, `.mp4` |
| Output path | По умолчанию папка `Recordings` в каталоге проектов Tosca (`C:\Tosca_Projects\Tosca_Commander\Recordings` в демо) |

Закройте настройки, и каждый прогон, из ScratchBook или из ExecutionList, создаёт файл в этой папке. При записи из ExecutionList файл называется по списку и TestCase, так что записи ScratchBook и ExecutionList для одного TestCase лежат рядом.

Запись только при сбое — разумное значение по умолчанию: смотреть хочется именно упавший прогон, а видео занимает реальное место на диске.

:::caution
Пауза выполнения не ставит запись на паузу; она продолжается до завершения прогона.
:::

## Исключение отдельных TestCase

Даже с рекордером в режиме *all* можно исключить отдельные TestCase, например стабильные или очень длинные, не меняя каждый раз настройку проекта:

1. На TestCase, его папке или корне проекта создайте **Test Configuration Parameter**.
2. Назовите его `AvoidExecutionRecorder` и задайте значение `True`.

Поставьте `False` (или удалите), чтобы снова записывать. Как Test Configuration Parameter он наследуется вниз по дереву папок, так что целую папку можно исключить одним параметром (см. [Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/)).

## Управление файлами

Записи — обычные MP4-файлы; никакого хранения по сроку внутри Tosca нет. Решите, кто и когда удаляет старые записи, или оставьте рекордер в режиме *только сбои*. Если вместо видео нужен статичный кадр, используйте [Скриншоты при сбое](/ToscaBase/ru/standard-modules/screenshots-on-failure/).
