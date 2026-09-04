---
title: DokuSnapper
description: Включение DokuSnapper, чтобы каждый прогон из ExecutionList или ScratchBook создавал документ с логом и скриншотом на каждый TestStep.
level: 2
sidebar:
  order: 60
sources:
  - id: mFptsa3Wuts
    title: "Tricentis Tosca Tutorial Part-6 : Tosca Execution, Tosca Execution List, Dokusnapper"
    url: https://www.youtube.com/watch?v=mFptsa3Wuts
    at: "04:24"
---

**DokuSnapper** — необязательная функция, заставляющая Tosca создавать документ для каждого выполненного TestCase с логом выполнения и скриншотом каждого TestStep. Это доказательство выполнения для аудитов или заинтересованных сторон, которые не открывают Commander. Включение — настройка проекта; в TestCase ничего не меняется.

## Включение DokuSnapper

1. **Project > Settings** открывает мастер настроек.
2. В дереве слева откройте узел DokuSnapper и установите **Enable Snapper** в `Yes`.
3. При необходимости настройте другие опции DokuSnapper, включая пути к документам.
4. Закройте мастер.

:::note
Транскрипт основан на субтитрах и называет узел неоднозначно («navigation engine and DokuSnapper ... under Settings»). Ищите пункт DokuSnapper в дереве настроек; переключаемая опция — **Enable Snapper**.
:::

## Что создаётся

С этого момента каждое выполнение, из [ExecutionList](/ToscaBase/ru/execution/execution-lists/) или ScratchBook, создаёт документ с именем TestCase. Документы из прогонов ScratchBook получают префикс `ScratchBook`. Документ содержит лог выполнения и по одному скриншоту на каждый TestStep.

Расположение по умолчанию из видео — папка AppData пользователя: `AppData\...\Tricentis\Tosca TestSuite\7.0.0\DokuSnapper` (сегмент версии зависит от установки). Измените его в настройках DokuSnapper, если нужно общее расположение.

## Типичный порядок работы

1. Включите DokuSnapper один раз, как описано выше.
2. Возьмите ExecutionList на check-out, правый клик по записям или всему списку > **Run**.
3. Сделайте check in, чтобы сохранить результаты в общий репозиторий.
4. Откройте папку DokuSnapper и найдите документ с именем TestCase: в нём лог выполнения и по скриншоту на каждый TestStep — доказательство выполнения, которое можно приложить к релизу или запросу аудита.

Документ создаётся и для прошедших, и для упавших прогонов, так что это ещё и быстрый способ увидеть, как выглядел экран на упавшем шаге, не перезапуская TestCase.

## См. также

- [Запись выполнения](/ToscaBase/ru/execution/recording-executions/): видео вместо документа.
- [Скриншоты при сбое](/ToscaBase/ru/standard-modules/screenshots-on-failure/): скриншоты только там, где прогон падает.
