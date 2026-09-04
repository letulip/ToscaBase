---
title: Результаты и логи
description: Чтение ActualLog у ExecutionList, настройка представления, трендовые диаграммы, очистка и архивирование логов, копирование результатов в Excel и LogViewer для низкоуровневой диагностики.
level: 2
sidebar:
  order: 20
sources:
  - id: 26Uj-nXXcAw
    title: "Tosca Tutorial | Lesson 60 - Change View of Execution Results | Execution Lists | Actual Logs |"
    url: https://www.youtube.com/watch?v=26Uj-nXXcAw
    at: "00:08"
  - id: IJyo8YlR2Dg
    title: "Tosca Tutorial | Lesson 62 - Create Trend Charts from Execution Results | Execution Lists | Logs |"
    url: https://www.youtube.com/watch?v=IJyo8YlR2Dg
    at: "00:04"
  - id: el-UnoqLoCA
    title: "Tosca Tutorial Lession 63 - Clear and Archive actual execution logs | Execution Lists | Logs |"
    url: https://www.youtube.com/watch?v=el-UnoqLoCA
    at: "00:08"
  - id: R-am5RdZYUw
    title: "Tosca Tutorial | Lesson 64 - Transfer Execution Results from Execution Lists to Microsoft Excel |"
    url: https://www.youtube.com/watch?v=R-am5RdZYUw
    at: "00:08"
  - id: w-g6OTmrr7M
    title: "Tosca Tutorial | Lesson 69 - Monitor TestCase Execution Logs using Log Viewer | Monitoring | Debug |"
    url: https://www.youtube.com/watch?v=w-g6OTmrr7M
    at: "00:08"
---

Каждый запуск [ExecutionList](/ToscaBase/ru/execution/execution-lists/) пишет в свой `ActualLog (текущий лог)`. Этот документ охватывает всё, что делают с логами после прогона: настройку представления, диаграммы результатов по времени, поддержание лога в чистоте между релизами, передачу результатов тем, кто работает в Excel, и, когда самого лога выполнения недостаточно, наблюдение за внутренним потоком логов Tosca в **LogViewer**.

## Настройка представления ExecutionList

Панель **Details** папки ExecutionList показывает набор колонок по умолчанию. Есть два уровня настройки:

- **Column chooser**: добавить или убрать колонки (summary, время начала и конца, длительность и т. д.).
- Выпадающий список **View > ExecutionList**: переключатели, меняющие содержимое всего представления. Значения по умолчанию уже отмечены; остальные:

| Опция | Эффект |
|---|---|
| Show only last ActualLog | Скрывает старые логи, оставляя только лог последнего прогона каждой записи |
| Multi-line logs | Колонка log info показывает полное многострочное сообщение вместо одной строки; полезно при отладке сбоев |
| Show statistics | Полосы и счётчики pass/fail по папкам; отключение убирает все полосы |
| Show statistics only on visible ExecutionLists | Статистика только для списков, видимых сейчас |
| Show statistics logarithmically | Сжимает полосы с полной ширины колонки до логарифмической шкалы |
| Show failed logs only | Оставляет в логе только упавшие TestCase |
| Duration in seconds | Длительность в секундах вместо ч:м:с, удобно для замера отдельных шагов |

## Трендовые диаграммы

Трендовые диаграммы включаются один раз на проект: **Project > Options > View > Enable trend charts**. После этого у каждой папки ExecutionList и каждого ExecutionList появляется вкладка **Trend chart** рядом с **Details** и **Test Configuration**.

- По оси y — количество выполненных TestCase; по оси x — время, сгруппированное по выбранному интервалу (**Months** по умолчанию; также **Years**, **Weeks**, **Days**, **Hours**).
- При наведении на столбец видны интервал и число прошедших, упавших и без результата.
- Тип диаграммы по умолчанию **Stacked bar**; доступны **Bar**, **Line** и несколько 3D-вариантов.
- Можно приблизить до одного дня или отдалить до всего диапазона и сбросить к виду по умолчанию.
- **Print view** экспортирует диаграмму в PDF, HTML, DOCX или XLS. HTML-экспорт открывается в браузере, его можно отправить как есть.

## Очистка и архивирование ActualLog

Каждое выполнение добавляет ещё одну запись в `ActualLog`. Если ExecutionList привязаны к требованиям, дашборд требований отражает всё, что есть в логе, и лог прошлого квартала всё ещё считается текущим результатом. Два способа начать с чистого листа:

- **Очистить**: правый клик по `ActualLog` > **Clear log**. Старые результаты удаляются, увидеть их больше нельзя.
- **Архивировать**: правый клик по ExecutionList > **Archive actual execution log**, введите имя архива (например `RC01`) и ответьте на вопрос, **отбросить ли ActualLog**. **Yes** опустошает `ActualLog` и оставляет под списком только архив; **No** сохраняет оба.

Архив — не история только для чтения. Перетащите его обратно на `ActualLog`, и он снова станет текущим логом (`ActualLog` зеленеет). Архивы упрощают отладку: когда шаг падает в новом прогоне, можно открыть архив и увидеть, что в прошлом релизе тот же шаг проходил, что сужает поиск изменения в приложении.

:::tip
Архивируйте по релизам (`RC01`, `RC02`...), а не очищайте, чтобы дашборд требований показывал текущую картину, а прошлые результаты оставались для сравнения.
:::

## Копирование результатов в Excel

Команды, отчитывающиеся в Excel, могут перенести таблицу ExecutionList без всякого мастера экспорта:

1. В ExecutionList выделите нужные папки, списки и execution entry (иерархия сохраняется).
2. Правый клик > **Copy table to clipboard** (`Ctrl+Shift+C`).
3. Откройте лист Excel, выберите ячейку и нажмите `Ctrl+V`.

Вставляются ровно те колонки, что видны в списке, поэтому добавьте или уберите колонки через column chooser до копирования. Заголовки и форматирование правьте потом в Excel.

## LogViewer

Лог выполнения говорит, какой TestStep упал; **LogViewer** показывает, что в это время делала сама Tosca. Это отдельное приложение `LogViewer.exe`, которое лежит и в домашней папке Commander, и в домашней папке TBox. Запустите его двойным кликом (или из командной строки) и держите открытым рядом с Commander.

Опции на верхней панели:

- **Log level**: `Off` (по умолчанию, ничего не показывает), только ошибки, предупреждения, информация или все уровни. `All` заливает консоль сразу после старта Commander, поэтому чаще всего достаточно ошибок или предупреждений.
- **Display mode**: **Console** показывает события вживую; **File** лишь указывает на записываемый файл лога. Список **Files** открывает созданные файлы, включая `diagnostic log.txt`.
- **Clear** очищает консоль; **Save** записывает собранные события в выбранный файл.
- **Chrome trace** сохраняет события в JSON для инструмента трассировки и профилирования Google Chrome.
- **Previous/Next error** переходят между ошибками; **Find** ищет, с поддержкой regex.

Запустите TestCase в ScratchBook с уровнем `All`, и вы увидите debug- и info-события от каждого компонента Commander. Понимать их все не нужно: вьюер нужен для случаев, когда обычный лог не даёт внятной причины, а его вывод — то, что стоит отправить технической команде или поддержке Tricentis. Он полезен и при проблемах конфигурации, например когда в фоне падают транзакции с сервером, не связанные с TestCase.

## См. также

- [Ручное выполнение](/ToscaBase/ru/execution/manual-execution/): установка результата вручную.
- [Запись выполнения](/ToscaBase/ru/execution/recording-executions/) и [Скриншоты при сбое](/ToscaBase/ru/standard-modules/screenshots-on-failure/): визуальные свидетельства сбоя.
- [Отчёты](/ToscaBase/ru/requirements-and-reporting/reports/): формальные определения отчётов.
