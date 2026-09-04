---
title: Обзор Module
description: Что такое Module в Tosca, как ModuleAttribute соответствуют контролам, чем классические Module отличаются от XModule, какие движки за ними стоят и чем стандартные Module отличаются от пользовательских.
level: 1
sidebar:
  order: 10
sources:
  - id: deY38EHGvNs
    title: "Tricentis Tosca Tutorial Part-4 : Tosca Module Creation, Tosca Xscan, Tosca Modules Overview"
    url: https://www.youtube.com/watch?v=deY38EHGvNs
    at: "00:40"
---

Module (модуль) — это описание одного экрана, страницы или диалога тестируемого приложения в Tosca. В нём хранятся технические свойства каждого контрола, который нужен TestCase (тест-кейсу), так что TestStep (шаг теста) обращается к контролу по имени, а не через внутренности HTML или окна. Создание Module — первый шаг разработки TestCase: нет Module — нет TestStep. Этот документ вводит словарь; сканирование описано в [XScan](/ToscaBase/ru/modules/xscan/), а способы, которыми Tosca различает контролы, — в [Идентификации контролов](/ToscaBase/ru/modules/control-identification/).

## Module и ModuleAttribute

- **Module** отображает одну страницу или экран приложения на Tosca. Рекомендуемая гранулярность — один Module на логический функциональный блок (форма входа, шапка, страница с таблицей); см. [Гигиену Module](/ToscaBase/ru/best-practices/module-hygiene/).
- **ModuleAttribute** (атрибут модуля) — один контрол внутри Module: текстовое поле, кнопка, ссылка, таблица. Каждый атрибут несёт технические свойства (для HTML: `id`, `name`, `tag`, `value`, `InnerText` и т. д.), по которым Tosca находит контрол во время выполнения. Атрибуты можно переименовывать в логические имена; технические свойства остаются под ними.
- Панель **Properties** справа в Commander показывает свойства и параметры атрибута. Их значение разобрано в [Свойствах и параметрах Module](/ToscaBase/ru/modules/module-properties-and-parameters/).

Когда Module перетаскивают в TestCase, он становится TestStep, а каждый ModuleAttribute — TestStepValue, которому задают значение и ActionMode (режим действия). Module хранятся в секции **Modules** workspace (рабочего пространства); в многопользовательском workspace новые Module нужно сдать в репозиторий (**Check in all**), прежде чем их увидят коллеги.

## Классические Module и XModule

В Tosca два поколения Module, различающихся архитектурой движка, который их создал:

| Вид | Кем создаётся | Атрибуты |
|---|---|---|
| Классический Module | Классические движки — исходные движки Tosca, каждый написан под одну технологию | Классические ModuleAttribute |
| XModule | XEngine на базе TBox, сканирование через XScan | XModuleAttribute |

Иконки в дереве Modules слегка различаются. Вся эта база знаний использует XModule, потому что именно их создаёт XScan и именно их ожидают современные версии Tosca.

### Движки

- **Классические движки** разработаны на раннем этапе Tosca. Каждый обрабатывает информацию TestCase и управляет (steering) тестовым объектом одной технологии.
- **TBox** — фреймворк, алгоритм которого лежит в основе XEngine. Он одинаково управляет GUI- и не-GUI-объектами.
- **XEngine** определяются в Tosca через **XDefinition**. XDefinition иерархически структурирует контролы технологии, поэтому дерево тестовых объектов ложится на дерево ModuleAttribute, которое вы видите в XScan.

Источник перечисляет поколение 3.0 движков, совместимых с TBox: XScan 3.0, AnyUI Engine 3.0, API Engine 3.0, Database Engine 3.0, .NET Engine 3.0, Mobile Engine 3.0 и SAP Engine 3.0. Подробности по движкам — в разделе [Движки](/ToscaBase/ru/engines/).

:::note
Названия движков взяты из автоматических субтитров, и одно из них искажено («ap engine»); здесь оно прочитано как API Engine. Считайте список иллюстративным, а не полным.
:::

## Стандартные и пользовательские Module

По назначению Module делятся на две группы.

**Стандартные Module** поставляет Tricentis; они импортируются при создании workspace (их можно загрузить и позже). Они выполняют типовые операции, не зависящие от вашего приложения: открыть файл, запустить программу, операции со строками и Buffer (буферами), проверки. Источник группирует их в три папки, которые по умолчанию видны в секции Modules:

- **TBox Automation Tools** — базовые операции с окнами, Buffer, файлами и папками, строками, датой и временем, процессами и ресурсами.
- **TBox XEngines** — технологические базовые Module для баз данных, HTML, .NET, SAP, мобильных приложений и т. д.
- **Test data related Modules** — Test Data Management и Test Data Services.

Tosca поставляет намного больше, но эти три папки используются почти в каждом проекте. Они описаны в [Стандартных Module](/ToscaBase/ru/standard-modules/).

**Пользовательские Module** создаёт тестировщик, сканируя тестируемое приложение. Каждый представляет один логический функциональный блок. Их созданию посвящён [XScan](/ToscaBase/ru/modules/xscan/).

## Что дальше

1. [XScan](/ToscaBase/ru/modules/xscan/): отсканировать страницу и выбрать контролы.
2. [Идентификация контролов](/ToscaBase/ru/modules/control-identification/): сделать каждый контрол уникальным.
3. [Пересканирование Module](/ToscaBase/ru/modules/rescan-modules/): починить Module после изменения страницы или требований.
4. [Дубликаты и слияние Module](/ToscaBase/ru/modules/duplicate-and-merge-modules/): не допускать копий в workspace.
5. [Свойства и параметры Module](/ToscaBase/ru/modules/module-properties-and-parameters/): настроить, как контрол ищется и управляется.
6. [Табличные контролы](/ToscaBase/ru/modules/table-controls/): строки, столбцы, ячейки и встроенные контролы.
