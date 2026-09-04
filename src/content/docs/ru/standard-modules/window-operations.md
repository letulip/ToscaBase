---
title: Операции с окнами
description: TBox Window Operation (на передний план, развернуть, свернуть, закрыть, ждать открытия) и TBox Scroll Window Operation, включая закрытие всплывающего окна без его сканирования.
level: 2
sidebar:
  order: 60
sources:
  - id: _WKauyXPI8g
    title: "Tosca Tutorial | Lesson 18 - Window Operations | TBox Automation Module |"
    url: https://www.youtube.com/watch?v=_WKauyXPI8g
    at: "00:10"
  - id: SZj-04A7aQA
    title: "Tosca Tutorial | Lesson 25 - Scroll Window | TBox Window Scroll Operation | Standard Module |"
    url: https://www.youtube.com/watch?v=SZj-04A7aQA
    at: "00:07"
  - id: doHtSzuBCFY
    title: "Tosca Tutorial | Lesson 122 - Close Window Popup | Window Operations |Obstacle 16 |"
    url: https://www.youtube.com/watch?v=doHtSzuBCFY
    at: "02:14"
  - id: zr-SyuOhTeQ
    title: "TRICENTIS Tosca 16.0 - Lesson 58 | OBSTACLE #16 | Window Operations | Window Popup | Standard Module"
    url: https://www.youtube.com/watch?v=zr-SyuOhTeQ
    at: "06:24"
---

**TBox Window Operation (операция с окном)** посылает команду окну, найденному по заголовку (caption): вывести на передний план, изменить размер, закрыть или дождаться появления. **TBox Scroll Window Operation** прокручивает содержимое окна на заданное число пикселей или строк. Оба Module находятся в **Modules > Standard modules > TBox Automation Tools > Basic window operations** и рассчитаны прежде всего на Windows-приложения, но работают и с окнами браузера, например со всплывающими.

## TBox Window Operation

| ModuleAttribute | Значение |
|---|---|
| Caption | Заголовок окна. Поддерживает регулярные выражения |
| Window index | Какое окно взять, если несколько имеют одинаковый заголовок; если пусто, первое |
| Operation | Выпадающий список с командой |

Доступные операции: **Bring to front**, **Close**, **Maximize**, **Minimize**, **Move to center**, **Normal** (вернуть исходный размер), **Resize**, **Verify window exists**, **Wait on close**, **Wait on open**.

### Заголовки и регулярные выражения

Окно Notepad называется `Untitled - Notepad`, и первая часть меняется вместе с именем файла. Запишите caption как регулярное выражение, совпадающее со стабильной частью (`Notepad`) и допускающее любое остальное, чтобы шаг работал при смене заголовка. Тот же приём решает задачу всплывающих окон с частично предсказуемым заголовком (ниже).

### Пример: управление Notepad

1. **TBox Start Program** с путём к Notepad; см. [Запуск и закрытие программ](/ToscaBase/ru/standard-modules/start-and-close-programs/). Это операция с процессом, не с окном, но окно должно сначала существовать.
2. **TBox Window Operation**, caption `Notepad` как regex, операция `Maximize`.
3. Скопируйте шаг и измените только операцию: `Minimize`.
4. `Bring to front` после сворачивания, чтобы свёрнутое окно вернулось.
5. `Normal`, чтобы вернуть исходный размер.
6. `Close`.

Выполняйте шаги по одному в ScratchBook, чтобы видеть эффект каждого; полный прогон слишком быстр. Остальные операции можно попробовать на том же окне.

## Закрытие всплывающего окна

Одно из «препятствий» автоматизации открывает новое окно по нажатию кнопки и просит закрыть его. Сканировать всплывающее окно **не нужно**: TBox Window Operation находит его по caption.

1. Отсканируйте в Module только кнопку и добавьте TestStep, который её нажимает.
2. Добавьте **TBox Window Operation** (перетащите из **Standard modules > TBox Automation Tools > Basic window operations**). Для caption возьмите уникальную часть заголовка попапа (в примере это имя аккаунта вида `@tricentis`; слово `Tricentis` само по себе есть и в заголовке основного окна, так что `*tricentis*` закрыл бы основную страницу) и окружите её подстановочными знаками regex.
3. Операция `Wait on open`. Попап загружается не мгновенно; без ожидания шаг выполняется до появления окна и падает.
4. Операция `Close` с тем же caption. В уроке 122 она стоит во втором шаге TBox Window Operation; в уроке 58 (Tosca 16) выбор операции добавляет в тот же TestStep ещё одну пустую строку *Operation*, поэтому `Wait on open` и `Close` стоят в одном шаге. Оба варианта проходят.
5. Установите workstate Completed и выполните: кнопка нажимается, попап появляется, дожидается и закрывается.

:::tip
`Wait on open` — аналог ActionMode `WaitOn` на уровне окна. Ставьте его перед любой операцией с окном, которое появляется не сразу, вместо статического ожидания. См. [Синхронизация вместо ожиданий](/ToscaBase/ru/best-practices/synchronisation-not-waits/).
:::

## TBox Scroll Window Operation

В **Add TestStep** найдите `TBox Scroll`.

| ModuleAttribute | Значение |
|---|---|
| Caption | Заголовок страницы или окна приложения для прокрутки (regex допустим) |
| Window index | Какое окно, по порядку открытия, если заголовки повторяются |
| Vertical | Насколько прокрутить по вертикали, в пикселях или строках |
| Horizontal | Насколько прокрутить по горизонтали, в пикселях или строках |
| Mouse policy | `None` (указатель не двигается) или `Center` (указатель позиционируется во время прокрутки) |
| Direction policy | `No direction policy`, `Vertical first` или `Horizontal first`: какая ось прокручивается первой, если заданы обе |
| Delay | Миллисекунды паузы между вертикальной и горизонтальной прокруткой, если заданы обе |

Обязательны не все атрибуты: caption и хотя бы одно из Vertical или Horizontal. Index, mouse policy (`Center` подходит), direction policy и delay необязательны.

Пример на странице с бесконечной прокруткой и заголовком `The Internet`: caption `The Internet` с regex, чтобы будущая смена заголовка не сломала шаг, без index, Vertical `500` (пикселей), mouse policy `Center`, direction policy `Vertical first`, без delay. Запуск в ScratchBook прокручивает страницу на 500 пикселей вниз; для большей прокрутки увеличьте значение. Module работает с любым окном с полосами прокрутки, веб или настольным.

:::note
Module появился в Tosca 16 и недоступен в более старых версиях. В названии видео он назван «TBox Window Scroll Operation», а автор говорит «scroll window operation»; ищите его по запросу `TBox Scroll`.
:::

## См. также

- [Диалоги рабочего стола](/ToscaBase/ru/standard-modules/desktop-dialogs/)
- [Препятствия: идентификация](/ToscaBase/ru/troubleshooting/obstacles-identification/)
