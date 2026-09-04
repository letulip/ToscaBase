---
title: Свойства и параметры Module
description: Свойства, которые Tosca хранит у Module и ModuleAttribute (cardinality, business type, synchronization policy, идентификаторы), и четыре типа параметров — configuration, identification, steering и transition — с теми, что реально пригодятся.
level: 1
sidebar:
  order: 60
sources:
  - id: IYGr51H7CIg
    title: "Tosca Tutorial | Lesson 157 - Module Properties | Configuration, Identification & Steering Params |"
    url: https://www.youtube.com/watch?v=IYGr51H7CIg
    at: "00:10"
---

У каждого Module и каждого ModuleAttribute есть набор **свойств** (properties), которые XScan заполняет при сканировании, и необязательные **параметры** (parameters), которые добавляете вы или Tosca, чтобы изменить, как контрол ищется и управляется (steering). И те и другие живут в панели **Properties** справа в Commander (если она свёрнута, разверните стрелкой): выделите Module или атрибут — и панель их перечислит. Часть доступна только для чтения, часть редактируется. Знание этих настроек позволяет починить контрол, который сканируется нормально, но не управляется, без пересканирования. Имена чувствительны к регистру.

## Свойства

Свойства с синей иконкой создаёт Tosca. Важнейшие:

| Свойство | У кого | Смысл |
|---|---|---|
| **Automation framework** | Module | `TBox` — движок по умолчанию, поставляемый с Tosca, — либо generic automation framework, когда вы разворачиваете собственные DLL и generic-контролы |
| **Business type** | Module и атрибут | Технологический тип. У Module это корневой элемент, `HTML document` или `XML document`; у атрибута — тип контрола, например `TextBox` |
| **Cardinality** (кардинальность) | Атрибут | Сколько раз атрибут может использоваться как TestStepValue в одном TestStep. По умолчанию `0-1` (один раз). `0-n` разрешает любое число раз, например для элемента списка или чекбокса, нужного многократно |
| **Node path** | Оба | Уникальный путь объекта в workspace, от корня через `Modules` до атрибута |
| **Synchronization policy** | Module | Включён ли объект в синхронизацию с репозиторием: `Default is on`, `Default is off`, `Cannot be excluded`, `Cannot be excluded for whole tree`. Разобрано в [Синхронизации вместо ожиданий](/ToscaBase/ru/best-practices/synchronisation-not-waits/) |
| **Technical ID** | Module | Технологическое свойство, обычно выставляемое Tosca; есть не у каждого Module |
| **Unique ID** | Оба | Уникальный номер объекта в workspace; по нему объект можно искать |
| **Owning group name**, **Viewing group name** | Module | Группы пользователей, владеющие объектом и имеющие право его видеть; см. [Пользователи и группы](/ToscaBase/ru/administration/users-and-groups/) |
| **Data type**, **Action mode**, **Default value** | Атрибут | Тип значения, ActionMode по умолчанию и значение по умолчанию для TestStepValue |
| **Interface type** | Атрибут | `GUI`, `Non-GUI` или `Implicit` |

:::note
Значения Synchronization policy в источнике зачитываются дважды; выше использовано второе чтение, на 07:09. В первом упоминается *customizable, default is on* — та же формулировка, что и в документе по лучшим практикам. Проверьте выпадающий список в своей версии.
:::

## Параметры

Щёлкните Module или атрибут в панели Properties правой кнопкой, чтобы увидеть, что можно создать: ModuleAttribute, **configuration parameter**, **transition parameter**, **steering parameter** и три вида identification parameter — **business ID**, **technical ID** и **reflected ID**. Отсюда четыре семейства параметров:

| Семейство | За что отвечает |
|---|---|
| Identification (идентификация) | Какие свойства используются для поиска контрола (business ID, technical ID, reflected ID) |
| Configuration (конфигурация) | Какие компоненты используются для управления контролом |
| Steering (управление) | Как контрол ведёт себя во время управления |
| Transition (переход) | Смена технологии или контекста внутри одного TestStep |

У свежеотсканированного HTML Module часть параметров уже есть: configuration parameter `Engine = HTML`, steering parameters `ControlFramework = None`, `EnableSlotContentHandling = False` и `IgnoreAreaControls = False`, а также technical ID parameter `Title`. Отсканированное текстовое поле несёт technical ID `id` и `tag` с их значениями и, в источнике, steering parameter `FireEvent = Change`. Свои параметры вы добавляете, когда стандартного поведения не хватает.

### Identification parameters

- **Technical ID** — самый распространённый. Технологические свойства вроде `value` для HTML input-контролов, `InnerText` для HTML-элементов, `encoding` для XML-декларации. XScan создаёт их из отмеченных свойств; добавить ещё можно через **Create technical ID parameter**, если знаете имя и значение. Несколько ID объединяются через AND.
- **Business ID** — свойства, одинаковые для типа контрола во всех технологиях, например у каждой кнопки есть `label`, у каждого текстового поля — `text`.
- **Reflected ID** — свойства, которые Tosca по умолчанию не показывает, читаемые из технологии через reflection. Технология должна поддерживать reflected object access, и reflected ID медленнее стандартных. Единственный пример в источнике — атрибут `language` в Internet Explorer.

### Configuration parameters

Создаются через **Create configuration parameter**, затем вводится точное имя. Относящиеся к веб-контролам:

| Параметр | Значение | Назначение |
|---|---|---|
| `ConstraintIndex` | целое число | Выбрать *n*-й из нескольких контролов с одинаковыми свойствами. Именно его выставляет *Identify by index*; см. [Идентификацию контролов](/ToscaBase/ru/modules/control-identification/) |
| `ExplicitName` | `True`, `False` или диапазон значений | Разрешает редактировать имя атрибута в TestStep; с диапазоном — только имена из диапазона. От него зависят управление через `#n` и многократные элементы списка |
| `CanExecuteInParallel` | `True` / `False` | Для распределённого выполнения на DEX-агентах, когда два TestCase используют один Module одновременно; см. [Распределённое выполнение](/ToscaBase/ru/execution/distributed-execution-dex/) |
| `ExternalEngine` | | Module мобильного движка, в основном автоматизация по изображению |
| `AlgorithmicAssociation`, `TechnicalAssociation` | | Параметры алгоритма поиска целевого объекта в выбранном контексте; зависят от движка, нужны редко |
| `SpecialExecutionTask` | | Выполняет специальную задачу при управлении контролом |

Пример из источника: у атрибута `Username` создаются `ExplicitName = True` и `ConstraintIndex = 1`. В новом TestCase имена `Password` и `Login` редактировать нельзя, а `Username` можно переименовать в `User` или `Email`.

### Steering parameters

Создаются через **Create steering parameter**. Многие специфичны для Vision AI, SAP или мобильных Module; общие:

| Параметр | Значение | Эффект |
|---|---|---|
| `BringToFront` | `True` (по умолчанию) / `False` | Вывести окно на передний план перед управлением; `False` позволяет работать в фоне |
| `IgnoreInvisibleHtmlElements` | `True` / `False` | Пропускать невидимые HTML-элементы, замедляющие выполнение |
| `ScrollingBehavior` | `Top`, `Bottom`, `Center`, `None` | Где на экране позиционируется контрол, когда Tosca к нему прокручивает |
| `SendKeysDelay` | миллисекунды, например `100` | Задержка между отдельными символами клавиатурной команды |
| `SynchronizationTimeout` | миллисекунды | Сколько Tosca ждёт контрол, прежде чем выдать ошибку. Задаётся также в настройках или для TestCase через configuration parameter; у `WaitOn` есть собственный steering parameter |
| `UserSimulation` | `True` / `False` (по умолчанию) | Вызывать клики и клавиатурные события через ActionMode `Input` так, как это делал бы пользователь: выбор и снятие чекбоксов и радиокнопок, клик по ссылкам, ввод в текстовые поля. Применяйте, когда обычное действие движка не срабатывает |
| `WaitBefore`, `WaitAfter` | миллисекунды | Ожидание до или после управления контролом — для контрола, который ещё грузится |

Источник добавляет `WaitBefore = 10` кнопке `Login` и описывает это как 10 миллисекунд. Такое короткое ожидание — демонстрация, а не рекомендация; предпочитайте синхронизацию, см. [Синхронизацию вместо ожиданий](/ToscaBase/ru/best-practices/synchronisation-not-waits/).

### Transition parameters

Используются редко. Transition parameter меняет технологию или контекст внутри одного TestStep, чтобы разные движки могли его разделять; значение — имя перехода, например `StringPropertyToXml` или `XPathToXmlElement`. Пример из источника — переключение из контекста браузера в мобильный движок с переиспользованием того же XPath. Смежный движок: [XML engine](/ToscaBase/ru/engines/xml-engine/).

## Правила навскидку

- Сначала чините идентификацию в XScan ([Идентификация контролов](/ToscaBase/ru/modules/control-identification/)); к параметрам обращайтесь, когда контрол находится, но ведёт себя не так.
- Вводите имена параметров ровно так, как их пишет Tosca; они чувствительны к регистру.
