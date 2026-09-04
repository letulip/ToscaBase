---
title: "Препятствия: идентификация контролов"
description: Одинаковые ID, «близнецы», меняющиеся ID, мультиселект, автодополнение, скрытые и невидимые на экране элементы и как их «стирить».
level: 3
sidebar:
  order: 10
sources:
  - id: AX495tz4jIM
    title: "Tosca Tutorial | Lesson 107 - IDs are not everything | Elements with same IDs | Obstacle 1"
    url: https://www.youtube.com/watch?v=AX495tz4jIM
    at: "01:10"
  - id: jB6ay9xvRcE
    title: "Tosca Tutorial | Lesson 108 - Twins | Duplicate Elements with same ID and InnerText | Obstacle 2"
    url: https://www.youtube.com/watch?v=jB6ay9xvRcE
    at: "01:10"
  - id: sZ4uO5o26Kc
    title: "Tosca Tutorial | Lesson 110 - Two Times | Dynamically changing ID Property | Obstacle 4"
    url: https://www.youtube.com/watch?v=sZ4uO5o26Kc
    at: "01:13"
  - id: PKNn-hsjh_Q
    title: "Tosca Tutorial | Lesson 112 - Multiselect ListBox | Cardinality | Explicit Name | Obstacle 6"
    url: https://www.youtube.com/watch?v=PKNn-hsjh_Q
    at: "01:13"
  - id: daXKUviEo2g
    title: "Tosca Tutorial | Lesson 113 - Autocomplete TextBox | ResultCount | InnerText | Obstacle 7"
    url: https://www.youtube.com/watch?v=daXKUviEo2g
    at: "01:14"
  - id: jZvsxD41Iuw
    title: "Tosca Tutorial | Lesson 130 - Hidden Element | Click Element | Obstacle 24"
    url: https://www.youtube.com/watch?v=jZvsxD41Iuw
    at: "01:13"
  - id: RsbKnsNt8Rs
    title: "Tosca Tutorial | Lesson 131 - Scroll Into View | Steering Parameter | Scrolling | Obstacle 25"
    url: https://www.youtube.com/watch?v=RsbKnsNt8Rs
    at: "02:17"
  - id: hoxsuJ47IPg
    title: "TRICENTIS Tosca 16.0 - Lesson 43 | OBSTACLE#1 | IDs are not everything – Elements with Same IDs"
    url: https://www.youtube.com/watch?v=hoxsuJ47IPg
    at: "02:16"
  - id: kIRtbXyTE0w
    title: "TRICENTIS Tosca 16.0 - Lesson 44 | OBSTACLE#2 | Duplicate Elements with Same Properties |"
    url: https://www.youtube.com/watch?v=kIRtbXyTE0w
    at: "01:14"
  - id: xFnTy2jdEyk
    title: "TRICENTIS Tosca 16.0 - Lesson 46 | OBSTACLE#4 | Dynamically Changing ID Property |"
    url: https://www.youtube.com/watch?v=xFnTy2jdEyk
    at: "01:13"
  - id: YUJi9vmPwQ4
    title: "TRICENTIS Tosca 16.0 - Lesson 48 | OBSTACLE #6 | Multiselect ListBox | Cardinality | Explicit Name |"
    url: https://www.youtube.com/watch?v=YUJi9vmPwQ4
    at: "01:16"
  - id: vV0O1w_lLyM
    title: "TRICENTIS Tosca 16.0 - Lesson 49 | OBSTACLE #7 | Autocomplete TextBox | ResultCount | InnerText |"
    url: https://www.youtube.com/watch?v=vV0O1w_lLyM
    at: "02:16"
  - id: TgtrmH4JmTY
    title: "TRICENTIS Tosca 16.0 - Lesson 67 | OBSTACLE #25 | Hidden Element | Click Element"
    url: https://www.youtube.com/watch?v=TgtrmH4JmTY
    at: "01:15"
  - id: ZnmDHKg7rrY
    title: "TRICENTIS Tosca 16.0 - Lesson 69 | OBSTACLE #27 | Steering Parameter | ScrollingBehavior"
    url: https://www.youtube.com/watch?v=ZnmDHKg7rrY
    at: "01:14"
---

*Obstacle Course* (полоса препятствий) Tricentis — публичная веб-страница с небольшими задачами по автоматизации из реальных приложений. Здесь собраны те, где сложность — в **идентификации** контрола: XScan сообщает *selected item is not unique*, идентифицирующее свойство меняется от запуска к запуску или элемент вообще не виден. Вывод всегда один: `id` — хорошее значение по умолчанию; когда он не работает, используйте другие свойства, родительскую иерархию, другой метод идентификации или Steering Parameter (параметр управления) — методы описаны в [Идентификации контролов](/ToscaBase/ru/modules/control-identification/), здесь показано их применение.

Таблицы — в [Препятствия: таблицы](/ToscaBase/ru/troubleshooting/obstacles-tables/); ввод и клики — в [Препятствия: ввод и клики](/ToscaBase/ru/troubleshooting/obstacles-input-and-clicks/); циклы — в [Препятствия: циклы и условия](/ToscaBase/ru/troubleshooting/obstacles-logic/). Обе серии уроков (107–137 и уроки 43–75 по Tosca 16, где *Hidden element* — препятствие 25, а *Scroll into view* — 27) решают каждое препятствие одинаково; различия отмечены по месту.

:::tip
Во всех препятствиях клик выполняется значением `X` (ActionMode `Input`), а не `{CLICK}`, который двигает реальную мышь — медленнее и не рекомендуется Tricentis. При отладке `{CLICK}` всё же полезен: по движению курсора видно, в какого «близнеца» попал клик.
:::

## ID не решают всё (IDs are not everything, препятствие 1)

**Проблема.** Две ссылки — *Don't* и *Click me*; при выборе *Click me* XScan сообщает *not unique*.

**Причина.** У обеих ссылок одинаковый `id` и, поскольку это ссылки, одинаковый `tag`.

**Решение.**

1. В XScan сравните технические свойства контрола с «двойником» и отметьте то, которое отличается: здесь `InnerText` (*Click me* против *Don't*) делает элемент уникальным.
2. Сохраните Module (модуль), перетащите его в TestCase (тест-кейс), поставьте `X` на ссылку и запустите.

Комбинируйте несколько свойств, если одного недостаточно; не держитесь за `id` по привычке.

## Близнецы (Twins, препятствие 2)

**Проблема.** Две одинаковые кнопки *I am the one*; нужно нажать вторую (правую). `id`, `InnerText` и `tag` совпадают, дополнительные свойства не помогают.

**Причина.** У контролов нет отличительных свойств; они различаются только тем, *где* находятся в структуре страницы.

**Решение.** [Identify by index](/ToscaBase/ru/modules/control-identification/#identify-by-index-constraintindex) работает, но сломается, как только появится похожая ссылка. Вместо этого идентифицируйте через родительский контейнер:

1. Поднимите уровень **filtered items** в XScan, чтобы стали видны родители.
2. Найдите контейнер, оборачивающий нужную кнопку; здесь у правого уникальный `id`, у левого он пустой.
3. Добавьте в Module контейнер, затем кнопку внутри него. Tosca ставит контейнеру ActionMode `Select`; на вложенную ссылку поставьте `X`.

Родители и соседи часто несут свойство, которого нет у элемента.

## Дважды (Two times, препятствие 4)

**Проблема.** Кнопку нужно нажать дважды. После первого клика подпись меняется с *Click me twice* на *Click me once more*, и TestStep (шаг теста), сработавший в первый раз, на второй падает.

**Причина.** `id` кнопки — `rd_` плюс число, которое меняется после каждого клика. Module, отсканированный до клика, ищет контрол по старому `id`.

**Решение.**

1. Сканируйте до первого клика, кликните один раз и пересканируйте, чтобы увидеть, какая часть `id` меняется.
2. В атрибуте Module замените меняющиеся цифры на `*`, оставив постоянный префикс (`rd_*`).
3. Перетащите Module в TestCase дважды (*Click once*, *Click twice*), оба раза с `X`.

:::note
Автор называет `*` регулярным выражением; в значениях свойств Tosca это подстановочный знак. Полноценные регулярные выражения описаны в [Интервалах и выражениях проверки](/ToscaBase/ru/expressions/intervals-and-verification-expressions/).
:::

## Список с множественным выбором (Multiselect list box, препятствие 6, «Testing methods»)

**Проблема.** Список с множественным выбором содержит методы тестирования. Нужно выбрать четыре из них: *Functional testing*, *GUI testing*, *End-to-End testing*, *Exploratory testing*.

**Причина.** По умолчанию атрибут Module используется один раз в TestStep (cardinality `0-1`) под фиксированным именем, поэтому один отсканированный элемент списка не может обращаться к четырём записям.

**Решение.** Сканируйте только сам список и **один** элемент списка. Снимите у элемента `InnerText` (только `tag`; *not unique* не мешает) и переименуйте его в `item`. Установите **cardinality** (кардинальность) `0-n` и правой кнопкой — **Create Configuration Parameter** `ExplicitName = True`: теперь атрибут можно использовать любое число раз, а имя, набранное в TestStep, решает, какой элемент управляется ([Идентификация контролов](/ToscaBase/ru/modules/control-identification/#explicitname-выбор-из-testcase)).

В TestCase у списка ActionMode `Select`. Переименуйте элемент в `Functional testing`; появится пустая строка элемента, которую переименовываете в следующий метод, и так далее. У элементов остаётся ActionMode `Input` — он выбирает запись. Используйте полное видимое имя (`End-to-End testing`, а не `End-to-End`), иначе ничего не найдётся.

## Поле с автодополнением (Autocomplete text box, препятствие 7, «And counting»)

**Проблема.** `span` показывает строку поиска (например, `ddd`). Ввод её в поле с автодополнением открывает список совпадений; количество записей нужно ввести во второе текстовое поле.

**Причина.** Текст поиска динамический; обычный `Input` в поле автодополнения не открывает список подсказок; подсказки — список неизвестной длины.

**Решение.** Введите в поле любой текст *до* сканирования, иначе списка подсказок нет в DOM. Module: `span` (снимите его динамический `InnerText`, оставьте `id` и `tag`), поле автодополнения, один `li` списка подсказок и поле для количества; если заголовок страницы динамический, поставьте в свойство title подстановочный знак. TestSteps:

1. `span` → свойство `InnerText`, ActionMode `Buffer`, значение `text`.
2. Поле автодополнения → `{SENDKEYS "{B[text]}"}`; посимвольный ввод запускает автодополнение, обычный `Input` — нет.
3. Элемент списка → свойство `ResultCount`, ActionMode `Buffer`, значение `count`.
4. Поле количества → `{B[count]}`, ActionMode `Input`.

`ResultCount` возвращает, сколько контролов подошло под атрибут, поэтому снимите у `li` его `id` (уникальный у каждой записи) и оставьте один `tag`; урок 113 дополнительно задаёт cardinality `0-n`. Тем же приёмом считаются ссылки в [Типичных проблемах и решениях](/ToscaBase/ru/troubleshooting/common-problems-and-fixes/).

## Скрытый элемент (Hidden element, препятствие 24)

**Проблема.** «Кто выключил свет?» Элемент, по которому нужно кликнуть, невидим — на экране нечего выбирать.

**Причина.** Видимость — не идентификация: Tosca управляет всем, что XScan разрешает из DOM, видно это или нет.

**Решение.**

1. Поднимите уровень **filtered items** в XScan, пока не появится всё HTML-дерево.
2. Ориентируйтесь по видимым соседям (текст *easy* лежит в том же `div`) и найдите нужный `span`; его `id` уникален.
3. Добавьте его в Module и кликните `X`; вся работа — в сканировании.

## Прокрутка к элементу (Scroll into view, препятствие 25)

**Проблема.** Текстовое поле внутри `iframe` лежит вне видимой области, и что-то перекрывает интерфейс. Текст, введённый, пока поле вне экрана, теряется; поле нужно прокрутить в область видимости, заполнить и отправить.

**Причина.** Браузер принимает ввод, только пока контрол находится во viewport.

**Решение.** Используйте **Steering Parameter** вместо шага прокрутки:

1. Отсканируйте текстовое поле (вложенность `iframe` → HTML-документ → поле) и кнопку *Submit*.
2. Правой кнопкой по атрибуту поля — **Create Steering Parameter**, имя `ScrollingBehavior` (точное написание, без пробела), значение `Top` (другие: `Bottom`, `Center`, `None`).
3. TestCase: *Enter text* (`Tosca`, ActionMode `Input`), затем *Click submit* (`X`).

Tosca прокручивает поле к верху viewport перед вводом; ни статическое ожидание, ни Module прокрутки не нужны. Другие Steering Parameters — в [Свойствах и параметрах Module](/ToscaBase/ru/modules/module-properties-and-parameters/); см. также [Синхронизация вместо ожиданий](/ToscaBase/ru/best-practices/synchronisation-not-waits/).
