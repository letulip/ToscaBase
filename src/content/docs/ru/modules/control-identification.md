---
title: Идентификация контролов
description: Четыре способа, которыми XScan идентифицирует контрол (properties, anchor, image, index), порядок их применения и параметр ExplicitName для выбора одного из одинаковых контролов из TestCase.
level: 1
sidebar:
  order: 30
sources:
  - id: deY38EHGvNs
    title: "Tricentis Tosca Tutorial Part-4 : Tosca Module Creation, Tosca Xscan, Tosca Modules Overview"
    url: https://www.youtube.com/watch?v=deY38EHGvNs
    at: "08:36"
  - id: Hy7xq4YP-Eo
    title: "Tosca Tutorial | Lesson 6 - Identify Controls By Anchor | Scan Modules |"
    url: https://www.youtube.com/watch?v=Hy7xq4YP-Eo
    at: "00:02"
  - id: GGH8_xFhLdk
    title: "Tosca Tutorial | Lesson 7 - Identify Controls By Image | Image Based Test Automation |"
    url: https://www.youtube.com/watch?v=GGH8_xFhLdk
    at: "00:09"
  - id: zgqUoo_1tpM
    title: "Tosca Tutorial | Lesson 8 - Identify Controls By Index | Duplicate Controls |"
    url: https://www.youtube.com/watch?v=zgqUoo_1tpM
    at: "00:09"
  - id: rCZQyJFonhY
    title: "Tosca Tutorial | Lesson 43 - Use Explicit Name to identify duplicate controls | Module Properties"
    url: https://www.youtube.com/watch?v=rCZQyJFonhY
    at: "00:08"
  - id: EMsHHgKDvEU
    title: "TRICENTIS Tosca 16.0 - Lesson 07 | Identify controls by Properties & Anchor | Create Control Groups"
    url: https://www.youtube.com/watch?v=EMsHHgKDvEU
    at: "03:18"
  - id: NEThwpAbK5U
    title: "TRICENTIS Tosca 16.0 - Lesson 23 | Dynamic ID | Explicit Name |"
    url: https://www.youtube.com/watch?v=NEThwpAbK5U
    at: "04:07"
  - id: 4ELkBwejJIU
    title: "TRICENTIS Tosca 16.0 - Lesson 24 | Set Repetition on Folder Level | Explicit Name | ResultCount"
    url: https://www.youtube.com/watch?v=4ELkBwejJIU
    at: "17:33"
---

Во время выполнения Tosca должна найти каждый контрол на экране по тому, что о нём хранит Module. XScan предлагает четыре метода идентификации в меню **Identify by** в Advanced view: **properties** (по свойствам), **anchor** (по якорю), **image** (по изображению) и **index** (по индексу) — иерархия, которую проходят в этом порядке, останавливаясь на первом методе, делающем контрол уникальным. Пятый приём — configuration parameter `ExplicitName` — не метод XScan, а способ выбрать один из нескольких одинаковых контролов из TestCase. Проблемные случаи: [Препятствия: идентификация контролов](/ToscaBase/ru/troubleshooting/obstacles-identification/). Первый плейлист использует стартовую страницу Google, уроки по Tosca 16 — демонстрационный веб-магазин Tricentis.

## Identify by properties

Метод по умолчанию и всегда первый выбор: Tosca сопоставляет технические свойства, отмеченные в XScan (`id`, `name`, `tag`, `value`, `InnerText`, `alt`, ...), — самый стабильный и быстрый метод.

Когда XScan сообщает *selected item is not unique*, отметьте больше свойств в Advanced view; часто хватает одного дополнительного (`alt` для логотипа Google, `value` для радиокнопки в [Пересканировании Module](/ToscaBase/ru/modules/rescan-modules/), `visible` для ссылки категории *Books*, у которой `tag` и `InnerText` совпадают с вкладкой товаров). Каждое отмеченное свойство стоит времени при выполнении, поэтому отмечайте только необходимые и стабильные, предпочитая свойства, описывающие идентичность, а не состояние. Если контрол всё ещё не уникален при всех осмысленных свойствах, как кнопка *Google Search* (невидимая вторая кнопка имеет те же `name`, `type` и `value`), переходите к anchor.

### Подстановочные знаки для динамических значений

Значение свойства, которое меняется от страницы к странице или от запуска к запуску (*dynamic ID*), сопоставляется через `*` на месте меняющейся части: заголовок демо-магазина — `Demo Web Shop. Login` на одной странице и `Demo Web Shop. Register` на следующей, поэтому technical ID `Title` вида `Demo Web Shop.*` подходит ко всем страницам. Так можно отредактировать любой technical ID — в XScan (щёлкните значение) или позже в панели **Properties**. Поскольку сопоставляется только постоянная часть, подстановочный знак может и намеренно сделать подходящими несколько контролов (см. пример с заказом в разделе про `ExplicitName`).

## Identify by anchor

Anchor (якорь) — соседний контрол, который *уникален*; Tosca сначала находит его, а затем цель относительно него. Используйте его только когда свойства не помогли и рядом есть стабильный уникальный сосед. Хороший якорь — контейнер: ссылки категорий демо-магазина (*Books*, *Computers*, ...) совпадают по свойствам, но каждая уникальна относительно содержащего их `ul`.

1. Повысьте **Filtered items**, если нужного якоря (контейнера `div` или `ul`) нет в дереве.
2. Выделите цель, выберите **Identify by > Anchor** и в панели **Identify by anchor** перетащите уникальный контрол из дерева в слот якоря (*I'm Feeling Lucky* или `ul`) либо нажмите **Select on screen** и щёлкните якорь в приложении. Панель сообщает *target control was successfully identified*, а оранжевая полоса *not unique* на цели исчезает.
3. Если сам якорь не уникален, нажмите **Make anchor unique** (Tosca отметит дополнительное свойство, `InnerHTML`) или отметьте свойство сами.
4. При необходимости добавьте ещё якоря; один контейнер служит якорем всем своим потомкам, а сам контролом становиться не обязан.

**Relative algorithm** определяет, как Tosca идёт от якоря к цели: **Shortest path** следует по дереву контролов, **Coordinate** использует экранные координаты (ломаются при смене разрешения), а **Auto** — значение по умолчанию — сначала пробует кратчайший путь, затем координаты. Оставляйте *Auto* или *Shortest path*.

:::note
Урок 6 (первый плейлист) называет ещё опцию *Always*, которой урок 7 (Tosca 16) не показывает; проверьте названия опций в своей версии.
:::

## Identify by image

Tosca хранит растровое изображение контрола и находит его на экране сопоставлением изображений: запасной вариант после anchor и последнее средство перед index, потому что зависит от множества условий во время выполнения.

1. Выберите **Identify by > Image**; панель **Identify by image** показывает изображение контрола.
2. Нажмите **Add image**, затем обведите прямоугольником нужную область или нажмите **Return**, чтобы взять собственную область контрола; **Escape** отменяет, иконка сохранения сохраняет выделение.
3. Ответьте **Yes** на предупреждение, что идентификация по изображению может долго работать без видимого окна XScan (отметьте *Remember my decision*, чтобы больше не спрашивало).
4. Заполните **image properties**: имя, плюс записанные **screen resolution** (разрешение экрана), **offset** (положение изображения относительно контрола), **method** (*full screen* в источнике) и **accuracy** (по умолчанию 95 %).

После этого контрол идентифицируется по свойствам **и** по изображению; другое разрешение, offset или метод при выполнении либо совпадение ниже порога accuracy роняют шаг, поэтому держите машины выполнения идентичными машине сканирования.

## Identify by index (ConstraintIndex)

Когда у нескольких контролов одинаковые свойства, индекс — это позиция цели среди них, последний вариант в иерархии.

1. Выберите **Identify by > Index**; панель предупреждает: используйте индекс, только если никакие критерии не идентифицируют контрол уникально.
2. Отметьте индекс, который Tosca уже определила; сообщение меняется на *selected item is unique*.

Module при этом получает configuration parameter `ConstraintIndex` с этим числом (или создайте его вручную, см. [Свойства и параметры Module](/ToscaBase/ru/modules/module-properties-and-parameters/)). Индекс хрупок: порядок одинаковых контролов может измениться вместе со страницей, и на записанном индексе окажется похожий контрол.

## ExplicitName: выбор из TestCase

Иногда выбор должен оставаться за TestCase: у всех кнопок *Add to cart* в списке товаров одинаковые свойства, а какую нажать, зависит от теста. Обычно имя TestStepValue в TestCase изменить нельзя, и клик по отсканированной кнопке падает с ошибкой *more than one control found*.

1. В Module выделите атрибут и в панели **Properties** щёлкните правой кнопкой → **Create configuration parameter**; назовите его `ExplicitName` и установите `True` (или диапазон значений, из которого TestCase может взять любое имя).
2. В TestStep переименуйте атрибут в `#3`. Tosca нажмёт третью кнопку *Add to cart*.

`#n` — индекс, задаваемый в каждом TestStep, а не зашитый в Module, поэтому один Module обслуживает любой товар; источник называет его более стабильным, чем *Identify by index*, потому что индекс выбирается там, где известен контекст. Имя может быть и выражением, например `{REPETITION}`, которое управляет контролом 1, 2, 3 ... на последовательных проходах папки с Repetition (так урок 24 очищает корзину; см. [Repetition](/ToscaBase/ru/test-cases/repetitions/)), а вместе с cardinality `0-n` один отсканированный элемент списка может управлять многими пунктами ([Препятствия: идентификация контролов](/ToscaBase/ru/troubleshooting/obstacles-identification/)).

**Пример: последний заказ.** Заказы в истории демо-магазина — отдельные `div`, новейший сверху. Отсканируйте один контейнер (номер и сумма заказа), замените его `OuterText` подстановкой `Order number: *`, задайте `ExplicitName = True` и назовите его `#1` в TestStep, чтобы управлять новейшим заказом при любом номере; его `InnerText` проверяйте по `Order number: {B[order number]}*`, где номер заранее буферизован на странице подтверждения ([Buffer](/ToscaBase/ru/data-and-parameters/buffers/)).

## Сводка

| Метод | Когда | Риск |
|---|---|---|
| Properties | Всегда первым | Нет, если свойства стабильны |
| Anchor | Свойства не помогли, есть уникальный сосед | Сосед изменится |
| Image | Больше ничего не работает | Разрешение, offset, accuracy |
| Index | Image тоже непрактичен | Порядок одинаковых контролов изменится |
| `ExplicitName` (`#n`) | Выбор зависит от TestCase | Как у index, но выбор в каждом TestStep |

От этого выбора зависит всё выполнение: делайте его осознанно и называйте атрибут осмысленно.
