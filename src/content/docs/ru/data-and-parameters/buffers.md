---
title: Буферы
description: Что такое буфер в Tosca, как создать его через ActionMode Buffer или TBox Set Buffer, прочитать через {B[имя]}, извлечь динамический текст XBuffer-ом {XB[имя]} и просматривать или править буферы в Buffer Viewer.
level: 2
sidebar:
  order: 10
sources:
  - id: cTqAz-nwRV8
    title: "Tricentis Tosca Tutorial Part-9 : Tosca Buffer"
    url: https://www.youtube.com/watch?v=cTqAz-nwRV8
    at: "00:45"
  - id: HOZ81KPcyMY
    title: "Tosca Tutorial | Lesson 77 - View and Manage buffers using Buffer Viewer | Tools |"
    url: https://www.youtube.com/watch?v=HOZ81KPcyMY
    at: "00:08"
  - id: HhOPIJ-fwyI
    title: "Tosca Tutorial | Lesson 116 - Extract Text | XBuffer | Dynamic Text | Obstacle 10 |"
    url: https://www.youtube.com/watch?v=HhOPIJ-fwyI
    at: "03:22"
  - id: XYRtKA8lkBI
    title: "TRICENTIS Tosca 16.0 - Lesson 13 | Action Mode Buffer | Math Function | Dynamic Expressions |"
    url: https://www.youtube.com/watch?v=XYRtKA8lkBI
    at: "04:27"
  - id: GsSNWhKRiRQ
    title: "TRICENTIS Tosca 16.0 - Lesson 13 (Updated) | Action Mode Buffer |Math Function |Dynamic Expressions|"
    url: https://www.youtube.com/watch?v=GsSNWhKRiRQ
    at: "02:03"
  - id: glZeQF7BWNo
    title: "TRICENTIS Tosca 16.0 - Lesson 22 | Dynamic Comparison | XBuffer Syntax {XB}"
    url: https://www.youtube.com/watch?v=glZeQF7BWNo
    at: "01:03"
---

**Buffer (буфер)** — переменная Tosca: именованное значение, которое один TestStep записывает во время выполнения, а последующие шаги читают. Это простейший из способов параметризации в Tosca (остальные — [Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/), [Business Parameters](/ToscaBase/ru/data-and-parameters/business-parameters-and-libraries/), TestCase-Design и [Test Data Services](/ToscaBase/ru/data-and-parameters/test-data-services/)). Буфер — стандартный способ перенести значение, которое породило приложение (номер заказа, итоговую сумму), с экрана, где оно появилось, на экран, где оно нужно.

## Время жизни и область видимости

- Буфер создаётся при первой записи и хранит значение, пока его не перезапишут или не удалят. Значение остаётся и **после завершения выполнения**, так что его можно посмотреть в Buffer Viewer.
- Буферы принадлежат **локальному workspace**. В общий репозиторий они не попадают: буфер, записанный на одной машине, на другой не виден.
- Новое выполнение просто перезаписывает буферы с теми же именами; удалять их в конце TestCase — необязательная гигиена.

:::note
Урок 13 (Updated) по Tosca 16 утверждает, что буфер следует создавать и использовать внутри **одного TestCase**, а общие данные хранить в TestCase-Design или Test Data Services; Part-9 и урок 77 показывают, что буферы переживают прогон и читаются из другого TestCase. Верно и то и другое: буфер сохраняется в workspace, но чтение его из другого TestCase работает только при таком порядке выполнения. Считайте правило «один TestCase» рекомендуемой практикой.
:::

## Создание буфера

Записать буфер можно тремя способами:

1. **ActionMode `Buffer` на любом TestStepValue.** Установите ActionMode у ModuleAttribute в `Buffer` и введите имя буфера как значение. Во время выполнения Tosca читает текущее значение контрола (у текстового элемента — его inner text) и сохраняет под этим именем. Так захватывают то, что показывает приложение. В Tosca 16 свойство можно выбрать явно: раскройте стрелку рядом с атрибутом, выберите `InnerText` (например, для отображаемой цены), введите имя буфера и задайте ActionMode; знак `=` превращается в стрелку, показывая, что значение уходит в буфер. См. [Action modes](/ToscaBase/ru/test-cases/action-modes/).
2. **`TBox Set Buffer`** и остальные буферные стандартные Module — когда значение известно в TestCase (литерал, выражение, другой буфер или Test Configuration Parameter). Четыре Module — `Set Buffer`, `Partial Buffer`, `Name to Buffer`, `Delete Buffer` — описаны в [Операциях с буферами](/ToscaBase/ru/standard-modules/buffer-operations/).
3. **Динамический XBuffer внутри шага `Verify`**, описанный ниже, — когда интересна только часть текста.

Лог ScratchBook сообщает о каждом буфере, который создал шаг, вместе со значением, поэтому ScratchBook — быстрый способ проверить, что буферный шаг работает.

## Чтение буфера: `{B[имя]}`

Везде, где TestStepValue принимает текст, `{B[MyBuffer1]}` заменяется текущим значением буфера `MyBuffer1`. Типичные применения:

- значение **Input** для контрола — чтобы ввести захваченное значение обратно в приложение;
- **Value** в `TBox Set Buffer` или `TBox Partial Buffer` — чтобы скопировать или вырезать буфер;
- внутри [выражений](/ToscaBase/ru/expressions/), например строковых операций, где буфер обычно первый аргумент;
- значение Configuration Parameter уровня Module, чтобы настройка вроде `ConstraintIndex` управлялась из TestCase (см. [Типичные проблемы и решения](/ToscaBase/ru/troubleshooting/common-problems-and-fixes/#одинаковые-вкладки-браузера)).

Буферы и Test Configuration Parameters естественно сочетаются: `TBox Set Buffer` со значением `{CP[MyTCP]}` копирует конфигурационное значение в буфер, и лог показывает подставленное значение.

## Буферы внутри выражений

Буфер может быть операндом любого динамического выражения, а результат можно сразу проверить. Пример с webshop для Tosca 16 проверяет страницу оформления заказа после покупки 25 пар джинсов:

1. На странице товара сохраните `InnerText` элемента с ценой через `Buffer` в `PriceBlueJeans`.
2. На странице оформления проверьте подытог через `Verify` со значением `{MATH[{B[PriceBlueJeans]}*25]}`.
3. Сохраните подытог через `Buffer` в `SubTotal`, затем проверьте итог заказа через `Verify` со значением `{MATH[{B[SubTotal]}+10]}`, где 10 — стоимость доставки, проверенная отдельным шагом.

Две детали делают это рабочим. Правый клик по значению > **Translate value** показывает, во что разрешается выражение (25, 35), ещё до прогона, так что ошибка в формуле ловится сразу. А **тип данных** TestStepValue должен быть `Numeric`: со строковым типом по умолчанию проверка 35 против 35 в уроке падала, пока тип не сменили. Синтаксис выражений — в [Выражениях](/ToscaBase/ru/expressions/).

## Извлечение динамического текста: XBuffer `{XB[имя]}`

Если текст содержит меняющуюся часть, буферизовать элемент целиком недостаточно. **Динамический XBuffer** одним шагом проверяет постоянную часть текста и буферизует переменную.

Сценарий из видео: сообщение об успехе состоит из «Purchase completed» и итоговой суммы, сумма каждый раз другая, и её нужно ввести в текстовое поле на той же странице.

1. Отсканируйте страницу. Элемент с сообщением по умолчанию не показан; увеличьте число отфильтрованных элементов в скане, пока текстовый элемент не появится, затем выберите его вместе с целевым текстовым полем и сохраните Module.
2. В TestCase у элемента с сообщением используйте свойство `InnerText` (в его свойствах видно, что inner text содержит всё сообщение вместе с суммой).
3. Установите ActionMode **`Verify`** и в качестве значения вставьте текст сообщения, заменив сумму на `{XB[amount]}`.
4. У текстового поля — ActionMode `Input`, значение `{B[amount]}`.

Во время выполнения шаг `Verify` проверяет совпадение постоянного текста и сохраняет то, что стоит на месте `{XB[amount]}`, в буфер `amount`; следующий шаг вводит его. В логе выполнения видны и проверка, и ввод.

:::note
Автор называет значение на месте суммы «регулярным выражением», но диктует только `{XB[amount]}`; простой подстановки здесь достаточно. Регулярные выражения в проверках описаны в [Интервалах и выражениях проверки](/ToscaBase/ru/expressions/intervals-and-verification-expressions/).
:::

Урок 22 применяет тот же шаблон к подтверждению заказа: `Verify` на `InnerText` элемента подтверждения со значением `Order number: {XB[OrderNumber]}` проверяет подпись и сохраняет номер; в логе проверка отмечена как пройденная, а **Tools > Buffer Viewer** показывает `OrderNumber` с реальным значением, готовым для следующих шагов. Если шаг входит в переиспользуемый TestStepBlock, перед правкой разрешите ссылку (см. [Business Parameters и библиотеки TestStep](/ToscaBase/ru/data-and-parameters/business-parameters-and-libraries/)).

Тот же приём читает меняющуюся ячейку веб-таблицы, см. [Препятствия: таблицы](/ToscaBase/ru/troubleshooting/obstacles-tables/).

## Buffer Viewer

**Tools > Buffer Viewer** открывает окно со всеми буферами workspace, как бы они ни были созданы, и позволяет их править; каждое изменение применяется сразу:

| Действие | Как |
|---|---|
| Поиск | Введите текст в поле поиска; выводятся все буферы, чьё имя или значение содержит текст (поиск `X` покажет все буферы с этим символом) |
| Переименовать | Кликните ячейку имени и введите новое |
| Изменить значение | Кликните ячейку значения и введите |
| Добавить буфер | Перейдите в пустую последнюю строку, отредактируйте её, введите имя и значение |
| Удалить | Выделите строку или несколько с **Ctrl** и нажмите **Delete** |

Используйте его после прогона в ScratchBook, чтобы проверить, что захватил шаг, чтобы вручную подготовить буфер перед шагом, который его читает, и чтобы почистить накопившиеся буферы.

## Смежное

- [Операции с буферами](/ToscaBase/ru/standard-modules/buffer-operations/): `TBox Set Buffer`, `Partial Buffer`, `Name to Buffer`, `Delete Buffer` с рабочим примером
- [Action modes](/ToscaBase/ru/test-cases/action-modes/): ActionMode `Buffer` и `Verify`
- [Строковые операции](/ToscaBase/ru/expressions/string-operations/): обрезка и вырезание буферизованного текста
