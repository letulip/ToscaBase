---
title: UIA engine и десктопные контролы
description: Что делать, когда Application scan не видит контролы - сменить движок XScan (WinX, UIA, Vision AI), добавить generic list item в combo box и закрыть JavaScript alert.
level: 3
sidebar:
  order: 40
sources:
  - id: UkEHEb_LNrI
    title: "Tosca Tutorial | Lesson 142 - Common Problems & Fixes | Desktop Application | Generic List Items"
    url: https://www.youtube.com/watch?v=UkEHEb_LNrI
    at: "00:12"
  - id: BUXOkE9GlI0
    title: "Tosca Tutorial | Lesson 143 - Common Problems & Fixes | UIA Engine | JavaScript Alert Window"
    url: https://www.youtube.com/watch?v=BUXOkE9GlI0
    at: "00:12"
---

Веб-приложения Tosca сканирует хорошо, а вот окна десктопных программ и нативные диалоги браузера часто распознаются лишь частично: combo box появляется без своих элементов, JavaScript alert не появляется вовсе. Писать custom control на .NET — крайняя мера. До этого XScan предлагает другие движки для того же окна, а свойства Module (модуля) позволяют добавить контролы, которые Tosca не отсканировала. Обе техники показаны на двух типичных проблемах.

## Выбор другого движка в XScan

**Scan > Application** показывает все открытые окна. У каждого окна есть движок, которым XScan идентифицирует его контролы; щёлкните окно в дереве XScan правой кнопкой, чтобы увидеть и сменить его:

- **HTML** выбран по умолчанию для окон браузера.
- **WinX** выбран по умолчанию для окон Windows, например диалогов Панели управления.
- **UIA** (UI Automation) сканирует контролы Windows, а также нативные всплывающие окна браузера.
- **Vision AI** распознаёт контролы по изображению экрана; требуется учётная запись Vision AI.

Если движок по умолчанию не показывает нужный контрол, сначала увеличьте число filtered items в XScan, чтобы убедиться, что контрол не просто скрыт, затем пересканируйте через UIA или Vision AI. Только если его не находит ни один движок и нельзя добавить generic item (см. ниже), оправдан custom control.

## Десктопный combo box без элементов

Пример: **Device Manager > Monitors > Generic PnP Monitor > Properties > Details** содержит combo box `Property`. Задача: проверить, что определённые записи есть в этом выпадающем списке.

1. **Scan > Application**, выберите окно свойств; для него выбран WinX. Скан показывает label, combo box `Property`, список `Value`, tab control и кнопки, но элементов внутри combo box нет даже при большем числе filtered items.
2. Выделите combo box (он и так уникален), сохраните Module.
3. В Module щёлкните combo box правой кнопкой, откройте меню **...** (многоточие) и выберите **Create generic list item**. Под combo box появится generic-элемент `Item` типа list item. Его движок WinX, а свойство **explicit name** уже перечисляет все записи выпадающего списка запущенного приложения.
4. Кардинальность элемента `0-n`, поэтому в TestCase (тест-кейсе) его можно использовать сколько угодно раз; каждое использование добавляет ещё одну строку item.

TestCase (`Verify driver properties` в папке `Win controls`):

1. Добавьте Module. Для combo box задайте ActionMode (режим действия) `Select`.
2. Добавьте generic item по одному разу на каждую проверяемую запись (`Device description`, `Capabilities`, `Status`), выберите запись из explicit names и проверьте `Exists` == `True` для каждой.
3. Запустите. Tosca разворачивает окно, и log info сообщает об успешной проверке каждого элемента.

:::note
Generic items доступны только для некоторых типов контролов. Если меню **...** их не предлагает, а другие движки тоже не помогают, нужен custom control.
:::

## JavaScript alert в Chrome

JavaScript `alert()` открывает нативное окно браузера поверх страницы и блокирует все дальнейшие шаги. Скан браузера через **Application** (движок HTML) показывает кнопки и ссылки страницы, но никогда не показывает само окно и его кнопку OK, сколько бы filtered items вы ни включили.

1. Вызовите alert в браузере, затем **Scan > Application** и выберите окно браузера.
2. В окне XScan щёлкните окно правой кнопкой и переключите движок с HTML на **UIA**, затем нажмите **Scan**. Среди отсканированных контролов теперь есть alert и его кнопка `OK`.
3. Выделите `OK` (он уникален), сохраните Module как `JavaScript popup`.
4. Сделайте Module универсальным: заголовок окна alert в Chrome выглядит как `<сайт> says`, поэтому замените часть с сайтом в идентификации по заголовку подстановочным знаком, `*says`, и Module подойдёт к любому alert с любой страницы.
5. Создайте TestCase (`Click on popup`), добавьте Module, задайте клик по кнопке `OK` и запустите в ScratchBook. Окно закрывается, TestCase продолжается.

:::caution
Шаблон заголовка зависит от браузера. Firefox, Edge и другие называют окно иначе, поэтому идентификацию нужно подстроить под каждый браузер.
:::

## См. также

- [Идентификация контролов](/ToscaBase/ru/modules/control-identification/): идентификация по explicit name.
- [Obstacles: идентификация](/ToscaBase/ru/troubleshooting/obstacles-identification/): другие случаи, когда Tosca не видит контролы.
- [Десктопные диалоги](/ToscaBase/ru/standard-modules/desktop-dialogs/): стандартные модули для нативных диалогов.
