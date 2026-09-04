---
title: Путь обучения
description: Рекомендуемый порядок чтения ToscaBase — от первых понятий до корпоративной настройки.
level: 1
sidebar:
  order: 5
---

Маршрут по базе знаний, выстроенный так, что каждый документ опирается на предыдущие.
Если вы только начинаете работать с Tosca, идите сверху вниз; если основы уже знакомы, переходите сразу к нужному уровню.
У каждого документа есть значок уровня, а [Глоссарий](/ToscaBase/ru/reference/glossary/) объясняет любой встреченный термин.

Четыре уровня совпадают с группами в боковом меню: Основы (что такое Tosca и как устроены Module и TestCase),
Построение тестов (данные, выражения, переиспользуемые блоки и выполнение), Специализация (движки, тестирование API,
отчётность, лучшие практики и устранение проблем) и Enterprise (администрирование многопользовательской работы).

## Уровень 1 · Основы

Пройдя этот уровень, вы сможете установить Tosca, создать workspace, отсканировать приложение в Module через XScan, добиться уникальной идентификации каждого контрола, а также собрать и запустить TestCase в ScratchBook с правильными ActionMode, условиями, циклами и сценариями восстановления.

### [Начало работы](/ToscaBase/ru/getting-started/)

1. [Что такое Tosca](/ToscaBase/ru/getting-started/what-is-tosca/) — Tricentis Tosca на одной странице — бесскриптовая платформа автоматизации тестирования на основе моделей, её основные возможности, поддерживаемые приложения и сравнение с Selenium.
2. [Архитектура](/ToscaBase/ru/getting-started/architecture/) — Компоненты пакета Tosca — Tosca Commander, XScan, Executor, репозиторий тестов и сервер лицензий — и интерфейсы, через которые используется Tosca.
3. [Лицензирование](/ToscaBase/ru/getting-started/licensing/) — Как получить trial- или учебную лицензию Tosca — регистрация на портале поддержки, страница запроса учебной лицензии, бесплатный trial на tricentis.com и подключение Tosca Commander к облачному серверу лицензий.
4. [Установка](/ToscaBase/ru/getting-started/installation/) — Загрузка установщика Tosca, прохождение мастера установки, установка расширения браузера для XScan и, при необходимости, запуск Tosca на Windows Server в AWS EC2 вместо локальной машины.
5. [Workspace и настройка проекта](/ToscaBase/ru/getting-started/workspace-and-project-setup/) — Что такое workspace в Tosca, однопользовательские и многопользовательские workspace, типы репозитория, стандартный шаблон workspace и пошаговое создание обоих видов.
6. [Обзор Commander](/ToscaBase/ru/getting-started/commander-overview/) — Экскурсия по Tosca Commander — стартовая страница и проект-пример First Steps, разделы workspace, устройство TestCase изнутри, Test Configuration Parameters и запуск TestCase в ScratchBook.
7. [Первый TestCase](/ToscaBase/ru/getting-started/first-test-case/) — Построение и запуск полного TestCase входа в систему с нуля — структура папок, сканирование страницы в Module, перетаскивание Module в TestCase, значения и ActionMode, параметр Browser, открытие и закрытие браузера, запуск в ScratchBook.
8. [Что нового в Tosca 16](/ToscaBase/ru/getting-started/whats-new-in-tosca-16/) — Выпуск Tosca 16.0 — Tosca ID Mapper и поддержка ARIA для Oracle и других ERP-приложений, новые темы оформления, pre-execution approval для TestCase и список менее крупных улучшений.

### [Module](/ToscaBase/ru/modules/)

9. [Обзор Module](/ToscaBase/ru/modules/modules-overview/) — Что такое Module в Tosca, как ModuleAttribute соответствуют контролам, чем классические Module отличаются от XModule, какие движки за ними стоят и чем стандартные Module отличаются от пользовательских.
10. [XScan](/ToscaBase/ru/modules/xscan/) — Отсканируйте запущенное приложение в XScan, чтобы создать TBox Module, выберите контролы на экране, прочитайте сообщения unique / not unique и сохраните Module.
11. [Идентификация контролов](/ToscaBase/ru/modules/control-identification/) — Четыре способа, которыми XScan идентифицирует контрол (properties, anchor, image, index), порядок их применения и параметр ExplicitName для выбора одного из одинаковых контролов из TestCase.
12. [Пересканирование Module](/ToscaBase/ru/modules/rescan-modules/) — Используйте Rescan, чтобы заново открыть существующий Module в XScan, добавить технические свойства неуникальному контролу, добавить недостающие контролы и обновить использующие его TestCase.
13. [Дубликаты и слияние Module](/ToscaBase/ru/modules/duplicate-and-merge-modules/) — Найдите дубликаты Module в workspace и слейте их с помощью Module merge assistant, включая разрешение конфликтов атрибутов и то, что происходит с TestCase, использующими слитый Module.
14. [Свойства и параметры Module](/ToscaBase/ru/modules/module-properties-and-parameters/) — Свойства, которые Tosca хранит у Module и ModuleAttribute (cardinality, business type, synchronization policy, идентификаторы), и четыре типа параметров — configuration, identification, steering и transition — с теми, что реально пригодятся.
15. [Табличные контролы](/ToscaBase/ru/modules/table-controls/) — Как отсканированная таблица устроена в Module, селекторы строк, столбцов и ячеек, ActionMode и свойства таблиц, разобранные примеры steering, встроенные контролы внутри ячеек и проверка числа строк и столбцов.
16. [Сравнение таблицы с baseline](/ToscaBase/ru/modules/table-baseline-comparison/) — Сохраните снимок веб-таблицы как baseline, сравнивайте с ним последующие выполнения, исключайте динамические строки и столбцы, обновляйте или генерируйте baseline автоматически.

### [Тест-кейсы](/ToscaBase/ru/test-cases/)

17. [Основы TestCase](/ToscaBase/ru/test-cases/test-case-basics/) — Что такое TestCase в Tosca, технические и бизнес-TestCase, как TestStep собираются из Module, и первый сквозной пример с WaitOn, Input и Verify.
18. [Режимы действия](/ToscaBase/ru/test-cases/action-modes/) — Полный справочник по ActionMode в Tosca — Input, Insert, Verify, Buffer, WaitOn, Select и Constraint — с синтаксисом значений, настройками и рабочими примерами на формах и таблицах.
19. [Управление потоком](/ToscaBase/ru/test-cases/control-flow/) — Условия If/Then и циклы While и Do-While внутри TestCase — как их создать, что писать в Condition и как свойство Maximum repetitions защищает от бесконечных циклов.
20. [Повторения](/ToscaBase/ru/test-cases/repetitions/) — Выполнение TestStep папки фиксированное число раз через свойство Repetition, задаваемое через выбор колонок или свойства папки.
21. [Сценарии восстановления и очистки](/ToscaBase/ru/test-cases/recovery-and-cleanup-scenarios/) — Как recovery engine Tosca повторяет упавший TestCase — включение восстановления глобально или на папке, создание Recovery Scenario Collection, настройка Retry level и добавление Cleanup Scenario на случай, если само восстановление упадёт.
22. [Рекордер](/ToscaBase/ru/test-cases/recorder/) — Запишите действия в приложении, и Tosca автоматически сгенерирует Module и TestCase — панель рекордера, режим верификации, настройки, что генерируется и что придётся доработать.
23. [Исследовательское тестирование](/ToscaBase/ru/test-cases/exploratory-testing/) — Поддержка исследовательского тестирования в Tosca — explorative session, запись взаимодействия через Explorative Scenario Manager и экспорт документа сценария со скриншотами в PDF или DOCX.

## Уровень 2 · Построение тестов

Пройдя этот уровень, вы сможете хранить тестовые данные отдельно от TestCase с помощью TestCase-Design, применять стандартные модули TBox и динамические выражения в значениях TestStep, передавать значения через Buffer, Test Configuration Parameter и переиспользуемые TestStepBlock, а также запускать всё из ExecutionList, читать результаты и автоматизировать прогоны через планировщик, Jenkins или распределённое выполнение.

### [Дизайн тест-кейсов](/ToscaBase/ru/test-case-design/)

1. [Обзор TestCase-Design](/ToscaBase/ru/test-case-design/test-case-design-overview/) — Что такое TestCase-Design (TCD), из каких объектов он состоит, зачем тестовые данные хранятся отдельно от TestCase и как выглядит путь от TestSheet до сгенерированных TestCase.
2. [TestSheet и атрибуты](/ToscaBase/ru/test-case-design/test-sheets-and-attributes/) — Создание TestSheet в разделе TestCase-Design, структура из четырёх рекомендуемых атрибутов и свойство Business Relevant со значениями yes, no и result.
3. [Экземпляры и комбинаторика](/ToscaBase/ru/test-case-design/instances-and-combinatorics/) — Экземпляры как значения атрибутов и как TestCase, свойства Character и Position и четыре комбинаторных метода (all combinations, orthogonal, pairwise, linear expansion).
4. [Шаблоны и инстанцирование](/ToscaBase/ru/test-case-design/templates-and-instantiation/) — Преобразование TestCase в шаблон, привязка к TestSheet через schema path, проверка, инстанцирование в сгенерированные TestCase, условные TestStep и реинстанцирование после изменений.
5. [Классы дизайна](/ToscaBase/ru/test-case-design/design-classes/) — Классы TestCase-Design хранят атрибуты и экземпляры, общие для нескольких TestSheet; ссылки на класс держат их под центральным управлением, а разрешение ссылки отсоединяет копию.
6. [Разбор: от начала до конца](/ToscaBase/ru/test-case-design/worked-example-end-to-end/) — Один проход через TestCase-Design на демо Vehicle Insurance — от TestSheet с атрибутами и экземплярами до сгенерированных TestCase в ExecutionList, со ссылками на каждый концепт.

### [Стандартные модули](/ToscaBase/ru/standard-modules/)

7. [Операции с файлами и папками](/ToscaBase/ru/standard-modules/file-and-folder-operations/) — Стандартные модули TBox для создания, копирования, сравнения и удаления файлов и папок, а также для проверки существования папки.
8. [Операции с буферами](/ToscaBase/ru/standard-modules/buffer-operations/) — Четыре модуля TBox для буферов (Set Buffer, Partial Buffer, Name to Buffer, Delete Buffer) и их применение для извлечения значения, например номера заказа.
9. [Запуск и закрытие программ](/ToscaBase/ru/standard-modules/start-and-close-programs/) — TBox Start Program для запуска приложений с аргументами, закрытия их через taskkill, очистки кэша Chrome через cmd, а также TBox Start/Stop Timer для измерения длительности шагов.
10. [TBox Evaluation Tool](/ToscaBase/ru/standard-modules/evaluation-tool/) — TBox Evaluation Tool сравнивает два динамических выражения (буферы, Configuration Parameters, литералы) с результатом true/false; используется для верификаций и как условие If, операнды в кавычках.
11. [Скриншоты при сбое](/ToscaBase/ru/standard-modules/screenshots-on-failure/) — Снимок экрана на любом TestStep через TBox Take Screenshot и автоматический скриншот при каждой неудачной верификации через настройки проекта.
12. [Операции с окнами](/ToscaBase/ru/standard-modules/window-operations/) — TBox Window Operation (на передний план, развернуть, свернуть, закрыть, ждать открытия) и TBox Scroll Window Operation, включая закрытие всплывающего окна без его сканирования.
13. [Диалоги рабочего стола](/ToscaBase/ru/standard-modules/desktop-dialogs/) — Автоматизация диалога Windows «Save As» модулем TBox Save As, включая всплывающее окно подтверждения после нажатия Save.
14. [Выполнение JavaScript](/ToscaBase/ru/standard-modules/execute-javascript/) — Запуск JavaScript в браузере модулем Execute JavaScript и проверка возвращаемого значения модулем Verify JavaScript Result; обоим нужен Test Configuration Parameter Browser.

### [Выражения](/ToscaBase/ru/expressions/)

15. [Случайные значения](/ToscaBase/ru/expressions/random-values/) — Генерация случайных чисел, десятичных дробей и строк в TestStepValue через RND, RNDDECIMAL и RANDOMTEXT, а также работа со случайными значениями, которые создаёт приложение.
16. [Выражения дат](/ToscaBase/ru/expressions/date-expressions/) — Генерация, расчёт и форматирование дат и времени через DATE, MONTHFIRST, LDAY и родственные выражения, а также решение проблемы формата даты Tosca.
17. [Строковые операции](/ToscaBase/ru/expressions/string-operations/) — Длина, смена регистра, подсчёт вхождений, обрезка пробелов, замена с экранированием символов, Base64-кодирование и арифметика над очищенными строками.
18. [Интервалы и выражения проверки](/ToscaBase/ru/expressions/intervals-and-verification-expressions/) — Проверка значения в числовом диапазоне через INTERVAL, регулярные выражения в ModuleAttribute и шагах Verify для многоязычной идентификации, разбиение значения на буферы именованными группами.

### [Данные и параметры](/ToscaBase/ru/data-and-parameters/)

19. [Буферы](/ToscaBase/ru/data-and-parameters/buffers/) — Что такое буфер в Tosca, как создать его через ActionMode Buffer или TBox Set Buffer, прочитать через {B[имя]}, извлечь динамический текст XBuffer-ом {XB[имя]} и просматривать или править буферы в Buffer Viewer.
20. [Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/) — Test Configuration Parameters (TCP) хранят данные окружения и настройки вне TestStep; где их задавать, синтаксис {CP[имя]}, системные параметры, Configurations уровня проекта и Configuration Parameter модуля ConstraintIndex для одинаковых вкладок браузера.
21. [Business Parameters и библиотеки TestStep](/ToscaBase/ru/data-and-parameters/business-parameters-and-libraries/) — Группировка TestStep в TestStepBlock, перенос их в TestStep Library как переиспользуемых TestStepBlock, на которые ссылаются многие TestCase, и передача разных данных в каждую ссылку через Business Parameters.
22. [Test Data Services](/ToscaBase/ru/data-and-parameters/test-data-services/) — Test Data Services (TDS) в Tosca регистрируют тестовые данные централизованно на Tosca Server, отслеживают их состояние между процессами и делят между приложениями; как устроены репозитории, типы и элементы в веб-интерфейсе и какие Test Configuration Parameters нужны TestCase для их использования.
23. [Модули Test Data Service](/ToscaBase/ru/data-and-parameters/test-data-service-modules/) — Стандартные модули, управляющие Test Data Services из TestCase (Create and Provide New Item, Find and Provide Item, Update Item, Move Item to Type, Delete Item, Expert Module), поток create-find-update, чтение элементов через {TDS[тип.атрибут]} и массовая генерация данных случайными значениями и Repetitions.

### [Выполнение](/ToscaBase/ru/execution/)

24. [ExecutionList](/ToscaBase/ru/execution/execution-lists/) — Почему ExecutionList приходит на смену ScratchBook, когда TestCase готов, как собрать список из папок и TestCase, запустить его и держать в синхронизации с разделом TestCases.
25. [Результаты и логи](/ToscaBase/ru/execution/execution-results-and-logs/) — Чтение ActualLog у ExecutionList, настройка представления, трендовые диаграммы, очистка и архивирование логов, копирование результатов в Excel и LogViewer для низкоуровневой диагностики.
26. [Ручное выполнение](/ToscaBase/ru/execution/manual-execution/) — Запуск execution entry как ручного TestCase через окно чек-листа, прикрепление скриншотов и комментариев, возврат к автоматизации и установка результата вручную.
27. [Repetitions и бизнес-TestCase](/ToscaBase/ru/execution/execution-repetitions-and-business-test-cases/) — Многократный запуск execution entry через свойство Repetitions и сборка business TestCase и business ExecutionList в сквозное представление для заинтересованных сторон.
28. [Запись выполнения](/ToscaBase/ru/execution/recording-executions/) — Запись прогонов из ScratchBook и ExecutionList в MP4 через настройку Execution Recorder, ограничение записи сбоями и исключение TestCase параметром AvoidExecutionRecorder.
29. [DokuSnapper](/ToscaBase/ru/execution/dokusnapper/) — Включение DokuSnapper, чтобы каждый прогон из ExecutionList или ScratchBook создавал документ с логом и скриншотом на каждый TestStep.
30. [Кросс-браузерное выполнение](/ToscaBase/ru/execution/cross-browser-execution/) — Запуск одного TestCase в нескольких браузерах через Test Configuration Parameter Browser, берущий значение из Buffer, и исправление ошибки «No feasible executor found», вызванной TestStep без Module.
31. [Планирование выполнения](/ToscaBase/ru/execution/scheduling-executions/) — Прогоны без участия человека и без CI-сервера: запуск скрипта TCShell через bat-файл из Планировщика заданий Windows.
32. [Интеграция с Jenkins](/ToscaBase/ru/execution/ci-integration-jenkins/) — Запуск задач Tosca Commander из freestyle-задания Jenkins через выполнение bat-файла Windows, который вызывает TCShell со скриптом .tcs.
33. [Распределённое выполнение (DEX)](/ToscaBase/ru/execution/distributed-execution-dex/) — Настройка распределённого выполнения Tosca с AOS: workspace для AOS, DEX-агент, настройки Commander, Configurations, TestEvent и сопоставление агентов с конфигурациями.
34. [Tosca Execution Client](/ToscaBase/ru/execution/tosca-execution-client/) — Запуск DEX TestEvent из командной строки или CI/CD-конвейера скриптом Tosca Execution Client (PowerShell/shell) и вызов его из Jenkins.

## Уровень 3 · Специализация

Пройдя этот уровень, вы сможете автоматизировать документы Excel, PDF и XML и трудно сканируемые десктопные контролы, тестировать REST- и SOAP-сервисы через API Scan, связывать тесты с требованиями, строить отчёты и TQL-запросы, следовать лучшим практикам Tricentis и распознавать и обходить классические препятствия автоматизации.

### [Движки](/ToscaBase/ru/engines/)

1. [Движок Excel](/ToscaBase/ru/engines/excel-engine/) — Сравнение двух книг модулем Excel 1:1 File Compare и создание, заполнение, проверка и чтение листов Excel стандартными модулями TBox Excel — открытие, лист, диапазон, манипуляция, закрытие, число строк и столбцов.
2. [Движок PDF](/ToscaBase/ru/engines/pdf-engine/) — Сравнение двух PDF модулем 1:1 Compare, сканирование текста, картинок и таблиц через PDF Scan и подсчёт страниц PDF без номеров страниц.
3. [Движок XML](/ToscaBase/ru/engines/xml-engine/) — Открытие, создание и проверка XML-файлов модулями XML engine, составление XPath, сканирование XML-файла в Module и извлечение значений из XML в буферы и веб-формы.
4. [UIA engine и десктопные контролы](/ToscaBase/ru/engines/uia-engine-and-desktop/) — Что делать, когда Application scan не видит контролы — сменить движок XScan (WinX, UIA, Vision AI), добавить generic list item в combo box и закрыть JavaScript alert.

### [Тестирование API](/ToscaBase/ru/api-testing/)

5. [Основы API Scan](/ToscaBase/ru/api-testing/api-scan-basics/) — Зачем тестировать API в Tosca, как запустить Tosca API Scan, отправить запрос вручную и отсканировать определение Swagger, OpenAPI, WSDL или WADL в готовые сообщения.
6. [TestCase для API](/ToscaBase/ru/api-testing/api-test-cases/) — Экспорт сообщений из API Scan в Tosca Commander, добавление ModuleAttribute для кодов состояния и полей payload, верификация ответов, буферизация значений для цепочки запросов и запуск API TestCase из ExecutionList.
7. [Аутентификация API](/ToscaBase/ru/api-testing/api-authentication/) — Авторизация API-запросов в Tosca API Scan с Basic и Digest аутентификацией, чем Digest отличается внутри, и куда попадают токены и учётные данные при сканировании.
8. [Структура сообщений, SOAP и вложения](/ToscaBase/ru/api-testing/api-message-structure-and-soap/) — Инструменты Validate, Pretty Print, Word Wrap и Search in payload в API Scan, сканирование и верификация SOAP-сервиса, отправка файла как вложения.
9. [Message Recorder](/ToscaBase/ru/api-testing/api-message-recorder/) — Захват HTTP-трафика между приложением и его бэкендом с помощью Message Recorder в API Scan, разбор вызовов и экспорт их как API-сообщений для построения TestCase.

### [Требования и отчётность](/ToscaBase/ru/requirements-and-reporting/)

10. [Требования и взвешивание по риску](/ToscaBase/ru/requirements-and-reporting/requirements-and-risk/) — Как структурировать требования в Tosca, взвесить их по бизнес-риску, привязать TestCase и ExecutionList и читать дашборд покрытия и состояния выполнения.
11. [Поиск TQL и виртуальные папки](/ToscaBase/ru/requirements-and-reporting/tql-and-virtual-folders/) — Запросы к workspace на Tosca Query Language, фильтрация ExecutionList и TestCase по их свойствам и сохранение запроса как обновляемой виртуальной папки.
12. [Отчёты и определения отчётов](/ToscaBase/ru/requirements-and-reporting/reports/) — Экспорт любого раздела через Print View, печать стандартных определений отчётов для ExecutionList, TestCase и требований и создание собственного определения отчёта с набором данных, TQL-запросом и дизайнером.
13. [Импорт структуры папок из Excel](/ToscaBase/ru/requirements-and-reporting/import-from-excel/) — Постройте дерево папок TestCase или компонента в Excel и вставьте его в Tosca Commander через Create Folder Structure, соблюдая правило «столбец на уровень».

### [Лучшие практики](/ToscaBase/ru/best-practices/)

14. [Соглашения об именовании](/ToscaBase/ru/best-practices/naming-conventions/) — Почему единообразные имена Module, TestCase, папок и TestStep решают, останется ли проект Tosca поддерживаемым, с примером «до и после».
15. [Структура TestCase](/ToscaBase/ru/best-practices/test-case-structure/) — Четыре структурных правила поддерживаемого TestCase — всегда что-то проверять, группировать TestStep в папки, предпочитать Repetition и Constraint циклам и поддерживать актуальный Workstate.
16. [Гигиена Module](/ToscaBase/ru/best-practices/module-hygiene/) — Держите Module небольшими и разбитыми по функциональности и регулярно сливайте дубликаты, чтобы беречь размер workspace и скорость выполнения.
17. [Синхронизация вместо ожиданий](/ToscaBase/ru/best-practices/synchronisation-not-waits/) — Замените статические шаги TBox Wait на ActionMode WaitOn и откажитесь от методов мыши и клавиатуры в значениях TestStep; пример с индикатором прогресса Calculate / Send разобран в обоих вариантах.
18. [Процесс ревью](/ToscaBase/ru/best-practices/review-process/) — Рабочий процесс ревью на папках с тремя стадиями утверждения и принципом «четырёх глаз» для Module, TestCase и других артефактов Tosca.

### [Устранение проблем](/ToscaBase/ru/troubleshooting/)

19. [Препятствия: идентификация контролов](/ToscaBase/ru/troubleshooting/obstacles-identification/) — Одинаковые ID, «близнецы», меняющиеся ID, мультиселект, автодополнение, скрытые и невидимые на экране элементы и как их «стирить».
20. [Препятствия: таблицы](/ToscaBase/ru/troubleshooting/obstacles-tables/) — Псевдотаблицы из div, «плавающие» строки, подсчёт строк, значение последней строки, поиск по ячейкам, заголовки строк и столбцов, выпадающие списки внутри ячеек.
21. [Препятствия: ввод и клики](/ToscaBase/ru/troubleshooting/obstacles-input-and-clicks/) — Перетаскивание, клики до смены подписи, ввод текста, который Tosca принимает за команду, клик со смещением и клик по координатам экрана.
22. [Типичные проблемы и решения](/ToscaBase/ru/troubleshooting/common-problems-and-fixes/) — Переключение вкладок браузера через SendKeys, подсчёт всех ссылок или похожих контролов через ResultCount, скачивание и проверка файла через curl из Tosca.
23. [Разбор: сквозной живой проект](/ToscaBase/ru/troubleshooting/worked-example-live-project/) — Завершение примера Vehicle Insurance end-to-end — условные папки шаблона, выбор тарифа из данных, WaitOn для подтверждения и отчётность из ExecutionList.

## Уровень 4 · Enterprise

Пройдя этот уровень, вы сможете поднять многопользовательский workspace на общем репозитории, управлять пользователями, группами, ветками, резервными копиями и версиями, дать нескольким тестировщикам общий ExecutionList через test mandate, управлять Commander из командной строки и обслуживать Tosca Server.

### [Администрирование](/ToscaBase/ru/administration/)

1. [Многопользовательские workspace](/ToscaBase/ru/administration/multi-user-workspaces/) — Создайте многопользовательский workspace на общем репозитории (SQLite для практики, Oracle, MS SQL Server или DB2 для проектов), работайте через Update All, Checkout, Checkout Tree и Check In All, смотрите и отзывайте чужой checkout.
2. [Пользователи и группы](/ToscaBase/ru/administration/users-and-groups/) — Создавайте пользователей и группы в многопользовательском workspace, задавайте и меняйте пароли, выдавайте роль Admins, ограничивайте разделы через группы owning и viewing, отключайте пользователей и читайте personal data report.
3. [Ветки](/ToscaBase/ru/administration/branches/) — Создайте ветку многопользовательского репозитория, работайте в ней в отдельном workspace, слейте обратно в Master и удалите — по Git-подобному workflow.
4. [Резервное копирование и восстановление](/ToscaBase/ru/administration/backup-and-restore/) — Сохраните однопользовательский проект через Export subset, сделайте резервную копию общего репозитория многопользовательского проекта как администратор и восстановите её в новый репозиторий.
5. [Версионирование и восстановление объектов](/ToscaBase/ru/administration/versioning-and-recovery/) — Управляйте историей версий многопользовательского репозитория, читайте историю изменений проекта или дерева и восстанавливайте удалённый TestCase через Export subset for revision.
6. [Test mandate](/ToscaBase/ru/administration/test-mandates/) — Позвольте нескольким пользователям выполнять один ExecutionList одновременно, не перезаписывая результаты друг друга, связав его с test mandate, и снимите auto-merge-связь, когда она больше не нужна.
7. [Инструменты командной строки](/ToscaBase/ru/administration/command-line-tools/) — Управляйте Tosca Commander из командной строки через TCShell в интерактивном или скриптовом режиме, чтобы выполнять ExecutionList и делать check-in, и клонируйте workspace для каждого участника команды через TCWorkspaceUtil вместо копирования.
8. [Tosca Server](/ToscaBase/ru/administration/tosca-server/) — Что такое Tosca Server в архитектуре Tosca, как скачать и установить его с версией, совпадающей с Commander, какие сервисы он запускает, как их перезапускать и что показывают дашборд и DEX monitor.
