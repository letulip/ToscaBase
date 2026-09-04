---
title: Глоссарий
description: Краткие определения всех терминов Tricentis Tosca, используемых в ToscaBase, со ссылками на документы, где они объяснены.
level: 1
sidebar:
  order: 10
---

Все термины Tosca, используемые в этой базе знаний, по алфавиту. Заголовок — английский термин, как он выглядит в Tosca Commander (`ExecutionList`, `TestStep`, `XScan`), затем русский вариант в скобках, определение в одно-два предложения и ссылка на документ, где понятие разобрано подробно. Если термина из документа здесь нет, его объясняет документ, который его вводит, а глоссарий стоит дополнить.

## Символы и цифры

**{DRAG} / {DROP}** (перетаскивание) — встроенные значения TestStep для drag and drop: `{DRAG}` на исходном контроле и `{DROP}` на целевом в одном TestStep. См. [Препятствия: ввод и клики](/ToscaBase/ru/troubleshooting/obstacles-input-and-clicks/).

**{TDS[type.attribute]}** (выражение TDS) — выражение, читающее атрибут элемента Test Data Services, который сейчас предоставлен TestCase. TDQL (Test Data Query Language, например `vehicle[make=="BMW"]`) отбирает, какой элемент будет предоставлен. См. [Модули Test Data Service](/ToscaBase/ru/data-and-parameters/test-data-service-modules/).

**1:1 Compare** (сравнение PDF один к одному) — стандартный Module TBox движка PDF, сравнивающий целевой PDF с эталонным при заданной точности в процентах, с возможностью исключить страницы. См. [Движок PDF](/ToscaBase/ru/engines/pdf-engine/).

## A

**ActionMode** (режим действия) — способ применения значения TestStep к контролу: `Input`, `Insert`, `Verify`, `Buffer`, `WaitOn`, `Select` или `Constraint`. См. [Режимы действия](/ToscaBase/ru/test-cases/action-modes/).

**ActualLog** (текущий лог) — объект лога под ExecutionList, хранящий текущие результаты выполнения. Его можно очистить, архивировать как именованный снимок (архив можно перетащить обратно и сделать текущим) и построить по нему трендовую диаграмму passed/failed/no result во времени. См. [Результаты и логи](/ToscaBase/ru/execution/execution-results-and-logs/).

**Anchor** (якорь) — уникально идентифицируемый соседний контрол, относительно которого находят контрол, не уникальный сам по себе (Identify by anchor). См. [Идентификация контролов](/ToscaBase/ru/modules/control-identification/).

**AOS (Automation Object Service)** (сервис объектов автоматизации) — сервис Tosca Server с собственным workspace, посредник между Tosca Commander, общим репозиторием и DEX-сервером при распределённом выполнении. См. [Распределённое выполнение (DEX)](/ToscaBase/ru/execution/distributed-execution-dex/).

**API Engine** (движок API) — движок Tosca, который отправляет API-запросы и принимает ответы при выполнении API TestCase. См. [Тестирование API](/ToscaBase/ru/api-testing/).

**API message** (API-сообщение) — один запрос вместе с его ответом в API Scan; при экспорте становится Module запроса и Module ответа. См. [Основы API Scan](/ToscaBase/ru/api-testing/api-scan-basics/).

**API Module** (API-модуль) — Module, сгенерированный из API-сообщения. У него есть дополнительная вкладка Technical view, повторяющая вид сообщения в API Scan, где элементы payload и коды состояния добавляются как ModuleAttribute. См. [TestCase для API](/ToscaBase/ru/api-testing/api-test-cases/).

**API Scan** (сканер API) — отдельный инструмент Tosca, открываемый с вкладки API Testing в Commander или автономно (без лицензии), для составления, отправки и сканирования API-сообщений. См. [Основы API Scan](/ToscaBase/ru/api-testing/api-scan-basics/).

**ARIA support** (поддержка ARIA) — возможность Tosca 16.0 нативно идентифицировать контролы с ARIA-разметкой; включается в XScan settings > General settings. См. [Что нового в Tosca 16](/ToscaBase/ru/getting-started/whats-new-in-tosca-16/).

**Attribute (TestCase-Design)** (атрибут) — параметр данных в TestSheet или классе, обычно один на поле или бизнес-объект; атрибуты вкладываются на любую глубину. См. [TestSheet и атрибуты](/ToscaBase/ru/test-case-design/test-sheets-and-attributes/).

## B

**Baseline (table)** (эталон таблицы) — сохранённый снимок табличного контрола, с которым сверяются последующие выполнения; динамические строки и столбцы исключаются. См. [Сравнение таблицы с baseline](/ToscaBase/ru/modules/table-baseline-comparison/).

**Branch** (ветка) — отдельная линия разработки внутри одного многопользовательского репозитория; `Master` — ветка по умолчанию. Ветки сливаются обратно и удаляются по Git-подобному workflow. См. [Ветки](/ToscaBase/ru/administration/branches/).

**Buffer** (буфер) — именованное значение, записываемое во время выполнения (через ActionMode `Buffer` или TBox Set Buffer) и читаемое через `{B[имя]}`. Буферы локальны для workspace и переживают прогон. См. [Буферы](/ToscaBase/ru/data-and-parameters/buffers/).

**Buffer Viewer** (просмотр буферов) — окно из меню Tools со списком всех буферов workspace; поддерживает поиск, переименование, правку, добавление и удаление. См. [Буферы](/ToscaBase/ru/data-and-parameters/buffers/).

**Business Parameter** (бизнес-параметр) — именованный вход переиспользуемого TestStepBlock, читаемый через `{PL[имя]}`; значение задаётся отдельно для каждой ссылки. См. [Business Parameters и библиотеки TestStep](/ToscaBase/ru/data-and-parameters/business-parameters-and-libraries/).

**Business Relevant** (бизнес-значимость) — свойство атрибута TestSheet со значениями `Yes`, `No` и `Result`, отмечающее настоящие тестовые данные, метаданные или ожидаемые результаты. См. [TestSheet и атрибуты](/ToscaBase/ru/test-case-design/test-sheets-and-attributes/).

**Business TestCase** (бизнес-TestCase) — невыполняемая логическая группировка технических TestCase для отслеживания покрытия; business ExecutionList связывает один бизнес-TestCase с несколькими ExecutionList и склеивает их результаты. См. [Основы TestCase](/ToscaBase/ru/test-cases/test-case-basics/) и [Repetitions и бизнес-TestCase](/ToscaBase/ru/execution/execution-repetitions-and-business-test-cases/).

## C

**Caption** (заголовок окна) — заголовок окна, по которому TBox Window Operation, TBox Scroll Window Operation и подобные Module находят окно; поддерживает регулярные выражения. См. [Операции с окнами](/ToscaBase/ru/standard-modules/window-operations/).

**Cardinality** (кардинальность) — свойство ModuleAttribute (`0-1` по умолчанию, `0-n`), определяющее, сколько раз атрибут можно использовать в одном TestStep. См. [Свойства и параметры Module](/ToscaBase/ru/modules/module-properties-and-parameters/).

**Character and Position** (характер и позиция экземпляра) — свойства экземпляра в TestCase-Design: Character — `Valid`, `Invalid` или `Straight through`; Position — `Inner` или `Boundary`. См. [Экземпляры и комбинаторика](/ToscaBase/ru/test-case-design/instances-and-combinatorics/).

**Check-out / Check-in** (взятие на редактирование / возврат объектов) — цикл редактирования с блокировками в многопользовательском workspace: Checkout или Checkout Tree блокируют объекты, Check In All публикует изменения, Update All подтягивает check-in других пользователей. Администратор может отозвать чужой checkout (revoke), при этом изменения того пользователя теряются. См. [Многопользовательские workspace](/ToscaBase/ru/administration/multi-user-workspaces/).

**Class (TestCase-Design)** (класс) — переиспользуемый набор атрибутов и экземпляров, общий для нескольких TestSheet. Ссылка на класс — доступная только для чтения связь из листа; разрешение ссылки отсоединяет локальную копию. См. [Классы дизайна](/ToscaBase/ru/test-case-design/design-classes/).

**Cleanup Scenario** (сценарий очистки) — TestStep, выполняемые, когда сам Recovery Scenario завершился неудачей, чтобы вернуть приложение в известное состояние. См. [Сценарии восстановления и очистки](/ToscaBase/ru/test-cases/recovery-and-cleanup-scenarios/).

**Combinatorial methods** (комбинаторные методы) — варианты команды Generate Instances в TestCase-Design: all combinations, orthogonal, pairwise и linear expansion (рекомендуемый). Linear expansion требует по одному straight-through (happy-path) экземпляру на атрибут. См. [Экземпляры и комбинаторика](/ToscaBase/ru/test-case-design/instances-and-combinatorics/).

**Common repository** (общий репозиторий) — база данных (SQLite, Oracle, MS SQL Server или DB2), хранящая мастер-копию всех объектов, из которой многопользовательские workspace берут объекты на checkout. См. [Многопользовательские workspace](/ToscaBase/ru/administration/multi-user-workspaces/).

**Condition** (условие) — выражение на объекте If, While или Do, решающее, выполнятся ли его TestStep; в TestCase-Design условие на TestStep или папке шаблона решает, будет ли она инстанцирована для данного столбца листа. См. [Управление потоком](/ToscaBase/ru/test-cases/control-flow/) и [Шаблоны и инстанцирование](/ToscaBase/ru/test-case-design/templates-and-instantiation/).

**Configuration (project-level)** (конфигурация уровня проекта) — переиспользуемый набор Test Configuration Parameter в разделе Configurations, который перетаскивают на TestCase, папки или ExecutionList. См. [Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/).

**Configuration Parameter (Module-level)** (параметр конфигурации модуля) — настройка управления на уровне ModuleAttribute, например `ExplicitName` или `ConstraintIndex`; не путать с Test Configuration Parameter. См. [Свойства и параметры Module](/ToscaBase/ru/modules/module-properties-and-parameters/).

**Constraint** (ограничение) — ActionMode, который отбирает, к какой строке, узлу или контролу обращается TestStep (например, к строке таблицы с заданным значением ячейки), вместо того чтобы управлять им. См. [Режимы действия](/ToscaBase/ru/test-cases/action-modes/).

**ConstraintIndex** (индекс окна) — Configuration Parameter уровня Module, выбирающий, в какой из нескольких одинаковых вкладок или окон браузера управлять контролом. См. [Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/).

**Coverage Specified** (заявленное покрытие) — доля требования, покрытая привязанными TestCase, с весом по их Workstate (Planned 20%, In Work 50%, Completed 100%). См. [Требования и взвешивание по риску](/ToscaBase/ru/requirements-and-reporting/requirements-and-risk/).

## D

**DEX agent** (DEX-агент) — машина с запущенным `DEXAgent.exe`, выполняющая TestEvent, которые распределяет DEX-сервер. См. [Распределённое выполнение (DEX)](/ToscaBase/ru/execution/distributed-execution-dex/).

**DEX monitor** (монитор DEX) — веб-страница Tosca Server со списком DEX-агентов и их test event. См. [Tosca Server](/ToscaBase/ru/administration/tosca-server/).

**Digest authentication** (Digest-аутентификация) — HTTP-аутентификация «вызов-ответ» (401 с realm и nonce, затем хешированный заголовок Authorization); Tosca выполняет оба обмена сама. См. [Аутентификация API](/ToscaBase/ru/api-testing/api-authentication/).

**Distributed execution (DEX)** (распределённое выполнение) — запуск ExecutionList на удалённых DEX-агентах, параллельно, через Tosca Server. См. [Распределённое выполнение (DEX)](/ToscaBase/ru/execution/distributed-execution-dex/).

**DokuSnapper** (генератор документации прогона) — настройка, создающая документ на каждый выполненный TestCase с логом и скриншотом на каждый TestStep. См. [DokuSnapper](/ToscaBase/ru/execution/dokusnapper/).

**Dynamic expression** (динамическое выражение) — значение в `{...}` внутри TestStepValue, которое Tosca вычисляет во время выполнения (буфер, дата, случайное значение, строковая операция, арифметика) вместо литерала. См. [Выражения](/ToscaBase/ru/expressions/).

## E

**Embedded control** (встроенный контрол) — контрол вроде ссылки или кнопки, помещённый в Module внутрь ячейки таблицы, чтобы обращаться к нему через строку. См. [Табличные контролы](/ToscaBase/ru/modules/table-controls/).

**Endpoint and Resource (API)** (конечная точка и ресурс) — endpoint — общая часть с хостом у всех запросов API; resource — уникальное расположение одного запроса на сервере. См. [Основы API Scan](/ToscaBase/ru/api-testing/api-scan-basics/).

**Evaluation Tool (TBox)** (инструмент вычисления) — стандартный Module, сравнивающий два динамических выражения и возвращающий true или false; применяется для верификаций и как условие If. См. [TBox Evaluation Tool](/ToscaBase/ru/standard-modules/evaluation-tool/).

**Excel 1:1 File Compare** (сравнение книг Excel) — Module TBox, сравнивающий две книги лист за листом и записывающий расхождения в выходной файл. См. [Движок Excel](/ToscaBase/ru/engines/excel-engine/).

**Execution entry** (запись выполнения) — ссылка на TestCase внутри ExecutionList; у неё собственное свойство Repetitions и собственные результаты. См. [ExecutionList](/ToscaBase/ru/execution/execution-lists/).

**Execution Recorder** (запись выполнения в видео) — настройка проекта TBox, записывающая прогоны в MP4; Test Configuration Parameter `AvoidExecutionRecorder` исключает TestCase из записи. См. [Запись выполнения](/ToscaBase/ru/execution/recording-executions/).

**Execution State** (состояние выполнения) — разбивка требования на passed, failed, not executed и not linked по привязанным к нему ExecutionList. См. [Требования и взвешивание по риску](/ToscaBase/ru/requirements-and-reporting/requirements-and-risk/).

**ExecutionList** (список выполнения) — набор TestCase, собранных для прогона. ExecutionList хранит результаты и историю выполнения; это единица, которую планируют, распределяют и по которой строят отчёты. См. [ExecutionList](/ToscaBase/ru/execution/execution-lists/).

**Exists** (свойство существования) — свойство контрола, возвращающее `True` или `False`; с `Constraint` ищет строку таблицы, с `WaitOn` ждёт появления диалога. См. [Препятствия: таблицы](/ToscaBase/ru/troubleshooting/obstacles-tables/).

**ExplicitName** (явное имя) — Configuration Parameter уровня Module; при `True` переименование атрибута в TestStep меняет, каким контролом управляет шаг, так что один Module обслуживает несколько одинаковых контролов. См. [Идентификация контролов](/ToscaBase/ru/modules/control-identification/).

**Exploratory testing** (исследовательское тестирование) — поддержка тестирования без сценария: запланированная, ограниченная по времени explorative session в Execution > Exploratory Testing и Explorative Scenario Manager, записывающий взаимодействие в документ сценария со скриншотами. См. [Исследовательское тестирование](/ToscaBase/ru/test-cases/exploratory-testing/).

## F

**File Scan** (сканирование файла) — Scan > More > File Scan; строит Module, атрибуты которого — узлы XML-файла. См. [Движок XML](/ToscaBase/ru/engines/xml-engine/).

## G

**Generic list item** (обобщённый элемент списка) — элемент, добавляемый через меню «...» у ModuleAttribute в combo box, значения которого XScan не отсканировал. См. [UIA engine и десктопные контролы](/ToscaBase/ru/engines/uia-engine-and-desktop/).

## I

**Identification methods** (методы идентификации) — четыре способа, которыми XScan идентифицирует контрол: по техническим свойствам, по якорю, по изображению и по индексу, именно в таком порядке. См. [Идентификация контролов](/ToscaBase/ru/modules/control-identification/).

**Identification, steering and transition parameters** (параметры идентификации, управления и перехода) — три из четырёх семейств параметров у Module и ModuleAttribute (четвёртое — Configuration Parameter уровня Module): параметры идентификации находят контрол, параметры управления вроде `ScrollingBehavior` меняют способ работы с ним, параметры перехода описывают, что происходит после. См. [Свойства и параметры Module](/ToscaBase/ru/modules/module-properties-and-parameters/).

**Insert** (вставка) — ActionMode для не-GUI интерфейсов, создающий объекты, например узлы XML. См. [Режимы действия](/ToscaBase/ru/test-cases/action-modes/).

**Instance** (экземпляр) — одно значение атрибута в TestCase-Design; экземпляр целого TestSheet — один сгенерированный TestCase (один столбец). См. [Экземпляры и комбинаторика](/ToscaBase/ru/test-case-design/instances-and-combinatorics/).

**Interval** (интервал) — `{INTERVAL[base][limit]}` или `{INTERVAL[base][lower][upper]}`, проверка (только для Verify), что значение лежит в числовом диапазоне. См. [Интервалы и выражения проверки](/ToscaBase/ru/expressions/intervals-and-verification-expressions/).

## L

**License server** (сервер лицензий) — сервис Tricentis (облачный или локальный), на котором Tosca Commander проходит аутентификацию по учётным данным портала поддержки. Бесплатные trial- и учебные лицензии запрашивают через портал поддержки или tricentis.com. См. [Лицензирование](/ToscaBase/ru/getting-started/licensing/).

**LogViewer** (просмотр логов) — автономный `LogViewer.exe`, показывающий внутренний поток логов Tosca с фильтром по уровню, для низкоуровневой диагностики. См. [Результаты и логи](/ToscaBase/ru/execution/execution-results-and-logs/).

## M

**Maximum repetitions** (максимум повторений) — свойство объектов While и Do, ограничивающее число итераций (по умолчанию 30) и защищающее от бесконечных циклов. См. [Управление потоком](/ToscaBase/ru/test-cases/control-flow/).

**Message Recorder** (запись сообщений) — функция API Scan, записывающая HTTP-трафик между приложением и его бэкендом и экспортирующая перехваченные вызовы как API-сообщения. См. [Message Recorder](/ToscaBase/ru/api-testing/api-message-recorder/).

**Module** (модуль) — переиспользуемое описание экрана, диалога, документа или API-точки, отсканированное Tosca или собранное вручную. Module перечисляет контролы (ModuleAttribute), с которыми могут работать TestCase. См. [Обзор Module](/ToscaBase/ru/modules/modules-overview/).

**Module merge assistant** (помощник слияния модулей) — Find duplicate Modules / Merge selected: сливает исходный Module в целевой, перепривязывает все использования и удаляет исходный. См. [Дубликаты и слияние Module](/ToscaBase/ru/modules/duplicate-and-merge-modules/).

**ModuleAttribute** (атрибут модуля) — контрол или параметр, объявленный в Module, для которого TestStep задаёт значение и ActionMode. См. [Обзор Module](/ToscaBase/ru/modules/modules-overview/).

**MTOM** (бинарные вложения SOAP) — опция бинарных вложений SOAP, включается флагом Enable MTOM на вкладке Attachments в API Scan. См. [Структура сообщений, SOAP и вложения](/ToscaBase/ru/api-testing/api-message-structure-and-soap/).

**Multi-user workspace** (многопользовательский workspace) — workspace, привязанный к общему репозиторию; добавляет вход по логину, check-out и check-in, управление пользователями, ветки, версионирование и test mandate. Опция Slim workspace уменьшает его размер для крупных репозиториев. См. [Многопользовательские workspace](/ToscaBase/ru/administration/multi-user-workspaces/).

## N

**Named group** (именованная группа) — `(?<BufferName>подвыражение)` внутри `{REGEX[...]}`; сохраняет совпавшую часть в буфер и требует ActionMode `Verify`. См. [Интервалы и выражения проверки](/ToscaBase/ru/expressions/intervals-and-verification-expressions/).

## O

**Obstacle Course** (полоса препятствий) — публичная веб-страница Tricentis с задачами по автоматизации для тренировки идентификации и управления контролами. См. [Устранение проблем](/ToscaBase/ru/troubleshooting/).

**OffsetHorizontal / OffsetVertical** (смещение клика) — параметры (в пикселях или процентах), сдвигающие точку, куда попадают `{CLICK}` и `{LONGCLICK}`; Module Click On Screen вместо этого кликает по абсолютным координатам X/Y в окне. См. [Препятствия: ввод и клики](/ToscaBase/ru/troubleshooting/obstacles-input-and-clicks/).

**Owning group / Viewing group** (группа-владелец / группа просмотра) — свойства раздела или папки, называющие группу пользователей, которая может менять объект или только просматривать его. См. [Пользователи и группы](/ToscaBase/ru/administration/users-and-groups/).

## P

**PDF Scan** (сканирование PDF) — режим сканирования движка PDF, превращающий выделенные области PDF (текст, изображение, таблица) в Module. См. [Движок PDF](/ToscaBase/ru/engines/pdf-engine/).

**Pre-execution approval** (утверждение перед выполнением) — автоматизированный workflow утверждения TestCase в Tosca 16.0, управляемый Workstate; только для многопользовательских workspace. См. [Что нового в Tosca 16](/ToscaBase/ru/getting-started/whats-new-in-tosca-16/).

## R

**Recorder** (рекордер) — функция меню Home, генерирующая Module и TestCase из записанных действий; режим верификации (Ctrl+Shift+V) превращает клики в шаги Verify. См. [Рекордер](/ToscaBase/ru/test-cases/recorder/).

**Recovery Scenario** (сценарий восстановления) — TestStep, которые recovery engine запускает при сбое TestCase, TestStep или TestStepValue, после чего повторяет попытку на заданном Retry level (TestCase, TestStep или TestStepValue). См. [Сценарии восстановления и очистки](/ToscaBase/ru/test-cases/recovery-and-cleanup-scenarios/).

**Relative Weight** (относительный вес) — вес требования в сравнении с весами остальных требований его requirement set. См. [Требования и взвешивание по риску](/ToscaBase/ru/requirements-and-reporting/requirements-and-risk/).

**Repetition** (повторение) — свойство папки, выполняющее её TestStep N раз; то же свойство у execution entry выполняет TestCase N раз. См. [Повторения](/ToscaBase/ru/test-cases/repetitions/).

**Report definition** (определение отчёта) — пользовательский отчёт: data set definition (отбор объектов через TQL), designer definition (макет) и движок вывода. Print View экспортирует любое представление как снимок без определения; Print Report запускает определение. См. [Отчёты и определения отчётов](/ToscaBase/ru/requirements-and-reporting/reports/).

**Repository type** (тип репозитория) — поле диалога создания workspace (None, SQLite, Oracle, MS SQL Server, DB2), определяющее, будет ли workspace одно- или многопользовательским. См. [Workspace и настройка проекта](/ToscaBase/ru/getting-started/workspace-and-project-setup/).

**Requirement set** (набор требований) — группа требований в разделе Requirements; TestCase привязывают к отдельным требованиям, никогда к набору. См. [Требования и взвешивание по риску](/ToscaBase/ru/requirements-and-reporting/requirements-and-risk/).

**Rescan** (пересканирование) — повторное открытие существующего Module в XScan на живом приложении, чтобы добавить свойства или контролы, не ломая использующие его TestCase. См. [Пересканирование Module](/ToscaBase/ru/modules/rescan-modules/).

**Resource (XML engine)** (ресурс XML) — имя, присвоенное открытому XML-документу; каждый XML TestStep ссылается на файл по нему. См. [Движок XML](/ToscaBase/ru/engines/xml-engine/).

**ResultCount** (число совпадений) — свойство контрола, возвращающее, сколько контролов подошло под ModuleAttribute, например чтобы посчитать все ссылки на странице. См. [Типичные проблемы и решения](/ToscaBase/ru/troubleshooting/common-problems-and-fixes/).

**Row selectors** (селекторы строк) — адресация таблицы в TestStep: `$1` первая строка, `$n` n-я строка, `$last` последняя, `$lastContentRow` последняя строка с данными, `$header` заголовок, `#n` n-е совпадение. См. [Табличные контролы](/ToscaBase/ru/modules/table-controls/).

**RowCount / ColumnCount** (число строк / столбцов) — свойства табличного контрола, возвращающие число строк и столбцов; их можно проверять в TestStep. См. [Табличные контролы](/ToscaBase/ru/modules/table-controls/).

## S

**ScratchBook** (черновой прогон) — быстрый пробный запуск TestCase или TestStep; результаты временные и пропадают при закрытии ScratchBook, а часть функций работает только из ExecutionList. См. [ExecutionList](/ToscaBase/ru/execution/execution-lists/).

**ScrollingBehavior** (поведение прокрутки) — параметр управления (`Top`, `Bottom`, `Center`, `None`), располагающий контрол в видимой области перед действием. См. [Препятствия: идентификация контролов](/ToscaBase/ru/troubleshooting/obstacles-identification/).

**Select** (выбор узла) — ActionMode, выбирающий узел в иерархии; назначается автоматически на путях к таблицам и строкам. См. [Режимы действия](/ToscaBase/ru/test-cases/action-modes/).

**SendKeys** (эмуляция клавиатуры) — ввод с клавиатуры: `{SENDKEYS["..."]}` в TestStepValue или Module TBox Send Keys с кодами .NET SendKeys (`^` Ctrl, `+` Shift, `%` Alt). См. [Типичные проблемы и решения](/ToscaBase/ru/troubleshooting/common-problems-and-fixes/).

**Standard Modules (TBox Automation Modules)** (стандартные модули) — готовые Module в подмножестве Standard для файлов, буферов, процессов, окон, скриншотов и прочего; добавляются через Add TestStep без сканирования. См. [Стандартные модули](/ToscaBase/ru/standard-modules/).

**Standard.tsu** (стандартный шаблон workspace) — шаблон workspace, предзагружающий стандартные Module, переиспользуемые блоки, шаблоны отчётов и примеры TestCase. См. [Workspace и настройка проекта](/ToscaBase/ru/getting-started/workspace-and-project-setup/).

**Static wait** (статическое ожидание) — шаг TBox Wait с фиксированной длительностью; Tosca ждёт всё время независимо от состояния приложения, поэтому предпочтителен WaitOn. См. [Синхронизация вместо ожиданий](/ToscaBase/ru/best-practices/synchronisation-not-waits/).

**Subset (.tsu) and .tdp** (файл подмножества и дамп репозитория) — `.tsu` — файл экспорта подмножества, создаваемый командой Export subset (и автономным API Scan); `.tdp` — дамп резервной копии репозитория, создаваемый администратором. См. [Резервное копирование и восстановление](/ToscaBase/ru/administration/backup-and-restore/).

**Synchronization policy** (политика синхронизации) — свойство объекта в многопользовательском workspace, определяющее, можно ли исключить объект из синхронизации с репозиторием; Include и Exclude for synchronization — команды контекстного меню, исключённые объекты показаны серым. См. [Многопользовательские workspace](/ToscaBase/ru/administration/multi-user-workspaces/).

## T

**Table control** (табличный контрол) — представление таблицы в TBox с узлами Row, Column и ячеек, селекторами и свойствами (`RowCount`, `ColumnCount`, `RowNumber`, `ResultCount`). См. [Табличные контролы](/ToscaBase/ru/modules/table-controls/).

**TargetDateFormat** (формат даты контрола) — системный Configuration Parameter на ModuleAttribute с датой, сообщающий Tosca формат даты в контроле. См. [Выражения дат](/ToscaBase/ru/expressions/date-expressions/).

**TBox** (движок TBox) — фреймворк движков, стоящий за XScan, XModule и стандартными Module; «TBox» в имени Module означает, что он построен на TBox. См. [Обзор Module](/ToscaBase/ru/modules/modules-overview/).

**TBox buffer Modules** (модули работы с буферами) — TBox Set Buffer, Partial Buffer, Name to Buffer и Delete Buffer: четыре стандартных Module для создания и извлечения буферов. См. [Операции с буферами](/ToscaBase/ru/standard-modules/buffer-operations/).

**TBox XEngines** (модули движков) — группа стандартных Module, привязанных к движку, например TBox XEngines > HTML с Execute JavaScript и Verify JavaScript Result. См. [Выполнение JavaScript](/ToscaBase/ru/standard-modules/execute-javascript/).

**TCShell** (командная оболочка Tosca) — инструмент командной строки, открывающий workspace и выполняющий команды или скрипты `.tcs`; основа для запусков по расписанию и из CI. См. [Инструменты командной строки](/ToscaBase/ru/administration/command-line-tools/).

**TCWorkspaceUtil (TCWorkspaceCloneUtil)** (клонирование workspace) — инструмент командной строки, клонирующий workspace с новыми идентификаторами для каждого участника команды вместо копирования. См. [Инструменты командной строки](/ToscaBase/ru/administration/command-line-tools/).

**TDS type and item** (тип и элемент TDS) — тип — таблица, элемент — строка в репозитории Test Data Services; Expert Module — единый Module TDS, папка Test Data Task которого покрывает все операции. См. [Test Data Services](/ToscaBase/ru/data-and-parameters/test-data-services/).

**Technical TestCase** (технический TestCase) — выполняемый TestCase с TestStep, значениями и ActionMode, в отличие от бизнес-TestCase. См. [Основы TestCase](/ToscaBase/ru/test-cases/test-case-basics/).

**Template (TestCase template)** (шаблон TestCase) — TestCase, преобразованный командой Convert to Template и привязанный через schema path к TestSheet; сам по себе не выполняется. Check Template проверяет его по листу, Instantiate генерирует по TestCase на каждый экземпляр листа, Reinstantiate перегенерирует их после изменений. См. [Шаблоны и инстанцирование](/ToscaBase/ru/test-case-design/templates-and-instantiation/).

**Test Configuration Parameter (TCP)** (параметр тестовой конфигурации) — значение на вкладке Test Configuration объекта, читаемое через `{CP[имя]}`, наследуемое вниз по дереву папок и доступное только для чтения во время выполнения; самый частый — `Browser`. См. [Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/).

**Test Data Services (TDS)** (сервисы тестовых данных) — компонент Tosca Server для централизованного управления тестовыми данными в репозиториях, типах и элементах, общих для TestCase и приложений. См. [Test Data Services](/ToscaBase/ru/data-and-parameters/test-data-services/).

**Test mandate** (тестовый мандат) — объект раздела Execution, привязанный к ExecutionList, чтобы несколько пользователей могли выполнять его одновременно, не перезаписывая результаты друг друга. См. [Test mandate](/ToscaBase/ru/administration/test-mandates/).

**TestCase** (тест-кейс) — упорядоченный набор TestStep, проводящий приложение через контролы, объявленные в одном или нескольких Module; единица выполнения — напрямую или из ExecutionList. См. [Основы TestCase](/ToscaBase/ru/test-cases/test-case-basics/).

**TestCase-Design (TCD)** (дизайн тест-кейсов) — раздел Commander, который хранит тестовые данные в TestSheet отдельно от TestCase и генерирует TestCase из шаблонов. См. [Обзор TestCase-Design](/ToscaBase/ru/test-case-design/test-case-design-overview/).

**TestEvent** (тестовое событие) — объект многопользовательского workspace, объединяющий Configuration и ExecutionList и выполняемый на DEX-агентах. См. [Распределённое выполнение (DEX)](/ToscaBase/ru/execution/distributed-execution-dex/).

**TestSheet** (тестовый лист) — объект верхнего уровня TestCase-Design: таблица атрибутов и экземпляров для одного сценария, по столбцу на каждый сгенерированный TestCase. См. [TestSheet и атрибуты](/ToscaBase/ru/test-case-design/test-sheets-and-attributes/).

**TestStep** (шаг теста) — одно действие внутри TestCase, создаваемое перетаскиванием Module; содержит TestStepValue для атрибутов Module. См. [Основы TestCase](/ToscaBase/ru/test-cases/test-case-basics/).

**TestStep Library** (библиотека TestStep) — контейнер (один на папку, Ctrl+L) с переиспользуемыми TestStepBlock, на которые TestCase ссылаются вместо копирования. См. [Business Parameters и библиотеки TestStep](/ToscaBase/ru/data-and-parameters/business-parameters-and-libraries/).

**TestStepBlock** (блок TestStep) — папка внутри TestCase, группирующая TestStep одной задачи; помещённая в TestStep Library, она становится переиспользуемым TestStepBlock. См. [Business Parameters и библиотеки TestStep](/ToscaBase/ru/data-and-parameters/business-parameters-and-libraries/).

**TestStepValue** (значение шага теста) — значение вместе с ActionMode, заданное для одного ModuleAttribute внутри TestStep. См. [Режимы действия](/ToscaBase/ru/test-cases/action-modes/).

**Tosca Commander** (клиент Tosca) — настольный клиент, в котором создают и ведут Module, TestCase, ExecutionList и требования. См. [Архитектура](/ToscaBase/ru/getting-started/architecture/).

**Tosca Execution Client** (клиент выполнения) — скрипт PowerShell/shell (Tosca 15.2+), запускающий TestEvent из CI/CD и записывающий результаты в XML в стиле JUnit. См. [Tosca Execution Client](/ToscaBase/ru/execution/tosca-execution-client/).

**Tosca Executor** (исполнитель) — компонент, выполняющий TestCase и ведущий логи выполнения. См. [Архитектура](/ToscaBase/ru/getting-started/architecture/).

**Tosca ID Mapper** (сопоставление идентификаторов) — настройка XScan в Tosca 16.0, задающая свойства идентификации по умолчанию на уровне приложения для всех его контролов. См. [Что нового в Tosca 16](/ToscaBase/ru/getting-started/whats-new-in-tosca-16/).

**Tosca Server** (сервер Tosca) — центральный серверный компонент с REST API, файловым сервисом, DEX-сервером и монитором, AOS, администрированием лицензий и пользователей и Test Data Services. См. [Tosca Server](/ToscaBase/ru/administration/tosca-server/).

**ToscaDateFormat** (формат даты Tosca) — системный Test Configuration Parameter, задающий, какой формат даты Tosca принимает как корректный литерал даты. См. [Выражения дат](/ToscaBase/ru/expressions/date-expressions/).

**TQL (Tosca Query Language)** (язык запросов Tosca) — грамматика запросов `scope->objecttype[constraint]` с операторами `=?`, `==`, `>`, `<` для поиска по workspace и наполнения отчётов. См. [Поиск TQL и виртуальные папки](/ToscaBase/ru/requirements-and-reporting/tql-and-virtual-folders/).

**Translate value** (перевести значение) — команда контекстного меню TestStepValue, показывающая конкретное значение, которое даст динамическое выражение. См. [Выражения дат](/ToscaBase/ru/expressions/date-expressions/).

## U

**Unattended execution** (выполнение без оператора) — запуски по расписанию без участия человека: через Планировщик заданий Windows, Jenkins или Tosca Execution Client. См. [Планирование выполнения](/ToscaBase/ru/execution/scheduling-executions/).

## V

**Verification point** (точка проверки) — TestStep с ActionMode `Verify`, сравнивающий ожидаемое значение с фактическим; без неё TestCase способен дать только ложноположительный результат. См. [Структура TestCase](/ToscaBase/ru/best-practices/test-case-structure/).

**Virtual folder** (виртуальная папка) — папка без собственных объектов, показывающая результат сохранённого TQL-запроса; обновляется вручную. См. [Поиск TQL и виртуальные папки](/ToscaBase/ru/requirements-and-reporting/tql-and-virtual-folders/).

## W

**WaitOn** (ожидание состояния) — ActionMode, ждущий, пока контрол не примет заданное значение или состояние, не дольше Synchronization timeout (Settings > TBox > Synchronization, по умолчанию 20000 мс). См. [Режимы действия](/ToscaBase/ru/test-cases/action-modes/).

**Weight** (вес требования) — значение бизнес-риска требования (по умолчанию 1, рекомендуемая шкала 1-5), которое можно вывести как 2^Frequency Class * 2^Damage Class; от него зависят Contribution и Relative Weight. См. [Требования и взвешивание по риску](/ToscaBase/ru/requirements-and-reporting/requirements-and-risk/).

**Workspace** (рабочее пространство) — локальный проект, который открывает Tosca Commander; содержит Module, TestCase, ExecutionList и требования, автономно или с привязкой к общему репозиторию. См. [Workspace и настройка проекта](/ToscaBase/ru/getting-started/workspace-and-project-setup/).

**Workstate** (состояние работы) — статус TestCase (`Planned`, `In Work`, `Completed`), влияющий на покрытие требований и процесс ревью. См. [Структура TestCase](/ToscaBase/ru/best-practices/test-case-structure/).

## X

**XBuffer** (динамический буфер) — `{XB[имя]}` внутри значения Verify; за один шаг проверяет постоянную часть текста и буферизует переменную. См. [Буферы](/ToscaBase/ru/data-and-parameters/buffers/).

**XModule / XModuleAttribute** (XModule и его атрибут) — Module и атрибут, создаваемые движками XEngine на базе TBox через XScan, в отличие от классических Module; XDefinition описывает, как XEngine структурирует контролы технологии для XScan. См. [Обзор Module](/ToscaBase/ru/modules/modules-overview/).

**XScan** (сканер) — инструмент сканирования Tosca, который читает запущенное приложение и превращает его контролы в Module. См. [XScan](/ToscaBase/ru/modules/xscan/).

**XScan engine (WinX, UIA, Vision AI)** (движок XScan) — технология, которой XScan читает контролы: WinX — по умолчанию для окон Windows, UIA (UI Automation) дополнительно видит нативные всплывающие окна браузера вроде JavaScript alert, Vision AI распознаёт контролы по изображению экрана. См. [UIA engine и десктопные контролы](/ToscaBase/ru/engines/uia-engine-and-desktop/).
