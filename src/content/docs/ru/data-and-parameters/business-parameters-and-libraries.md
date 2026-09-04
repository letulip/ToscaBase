---
title: Business Parameters и библиотеки TestStep
description: Группировка TestStep в TestStepBlock, перенос их в TestStep Library как переиспользуемых TestStepBlock, на которые ссылаются многие TestCase, и передача разных данных в каждую ссылку через Business Parameters.
level: 2
sidebar:
  order: 30
sources:
  - id: 5kWTxvxcfXQ
    title: "Tricentis Tosca Tutorial Part-8: Tosca Business Parameters,Tosca Library,Reusable TestStepBlocks"
    url: https://www.youtube.com/watch?v=5kWTxvxcfXQ
    at: "00:45"
  - id: nL1Vv11tBpA
    title: "Tosca Tutorial | Lesson 51 - Create TestStep Libraries | Reusable TestStep Blocks | Parameters |"
    url: https://www.youtube.com/watch?v=nL1Vv11tBpA
    at: "03:10"
---

В большинстве наборов одни и те же действия повторяются в каждом TestCase: открыть приложение, войти, создать запись, выйти. Tosca позволяет хранить такую последовательность один раз — в **TestStep Library (библиотеке шагов)** — и ссылаться на неё из любого TestCase как на **reusable TestStepBlock (переиспользуемый блок шагов)**. **Business Parameters (бизнес-параметры)** — входы этого блока, поэтому каждая ссылка выполняет его со своими данными. Изменение блока делается в одном месте, и все ссылки следуют за ним, что сокращает разработку и, главное, сопровождение.

## Строительные блоки

| Термин | Значение |
|---|---|
| **TestStepBlock** | Папка внутри TestCase, группирующая шаги одной задачи (логин, логаут, создание записи). Улучшает читаемость и снижает затраты на сопровождение даже без библиотеки. |
| **TestStep Library** | Контейнер переиспользуемых TestStepBlock. Создаётся в любой папке раздела **TestCases**, но в одной папке может быть **только одна** библиотека. Иконка — папка TestCase с буквой **L**. |
| **Reusable TestStepBlock** | TestStepBlock, лежащий в библиотеке. TestCase его не копируют, а держат **ссылку** на него. |
| **Business Parameter** | Именованный вход переиспользуемого блока. Блок использует параметр вместо литерала, а значение подставляет каждая ссылка. |

## Создание библиотеки и переиспользуемого блока

1. В многопользовательском workspace сначала сделайте check-out родительской папки ([Многопользовательские workspace](/ToscaBase/ru/administration/multi-user-workspaces/)).
2. Кликните правой кнопкой по папке и выберите **Create TestStep Library** (пункт с иконкой L; сочетание **Ctrl+L**).
3. Поместите блок в библиотеку одним из двух способов:
   - **Создать новый**: правой кнопкой по библиотеке, создать переиспользуемый TestStepBlock, дать ему функциональное имя (`Google Search`, `Login User`) и перетащить в него шаги из существующего TestCase.
   - **Преобразовать существующий**: перетащите TestStepBlock или сами шаги из TestCase в библиотеку. Шаги переезжают в библиотеку, а то, что остаётся в TestCase, превращается в ссылку с иконкой-стрелкой.
4. Используйте блок в другом месте, перетащив его из библиотеки в TestCase. Результат — снова ссылка, а не копия: удалите продублированные шаги из другого TestCase и поставьте ссылку на их место.

Во втором видео два TestCase — *login with valid user* и *login with invalid user* — делят шаги `Open URL` и `Login User`. После преобразования оба кейса ссылаются на одни и те же два блока и выполняются как раньше.

## Business Parameters

Ссылка на блок по-прежнему несёт собственные значения блока: оба кейса логина теперь входили бы одним пользователем. Business Parameters делают данные входом.

1. Выберите переиспользуемый TestStepBlock и выберите **Create Business Parameter Container**.
2. Внутри контейнера создайте по параметру на каждое изменяемое значение: `Username`, `Password`, `URL` или `SearchText` в примере с Google. Параметрам не нужны ни значение, ни ActionMode, ни тип данных — это только имена.
3. В шагах блока удалите жёстко прописанные значения и **перетащите каждый параметр на TestStepValue**, который должен его использовать. Значение теперь показывает ссылку на параметр в виде `{PL[Username]}`.
4. Вернитесь к TestCase. Каждая ссылка на блок теперь перечисляет Business Parameters с пустыми значениями; заполните их в каждом TestCase (`standard_user` в одном, `locked_out_user` в другом, одинаковый URL в обоих).

:::note
Автор описывает ссылку как «PL, затем имя параметра»; `{PL[имя]}` — письменная форма, использованная здесь по аналогии с `{B[...]}` и `{CP[...]}`. Проверьте, что Tosca вставляет при перетаскивании параметра.
:::

Значения, передаваемые в ссылку, сами могут быть параметрами. В первом видео на TestCase создаётся Test Configuration Parameter `SearchText` = `Tricentis Tosca`, а как значение Business Parameter вводится `{CP[SearchText]}`, так что текст поиска настраивается во вкладке **Test Configuration**, а не в шаге. То же работает для URL, хранимого на уровне папки. См. [Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/).

## Когда использовать библиотеку

- Выделите шаги, общие для многих TestCase, и перенесите в библиотеку только их; остальное остаётся в TestCase.
- Параметризуйте каждое значение, различающееся между вызовами (пользователь, URL, текст поиска); константы оставьте внутри блока.
- Сочетайте библиотеки с TestCase-Design: шаблон может ссылаться на переиспользуемый блок и заполнять его Business Parameters из TestSheet, см. [Шаблоны и инстанцирование](/ToscaBase/ru/test-case-design/templates-and-instantiation/).

## Смежное

- [Буферы](/ToscaBase/ru/data-and-parameters/buffers/): значения, захваченные во время выполнения, третий вид параметров
- [Структура TestCase](/ToscaBase/ru/best-practices/test-case-structure/): группировка шагов в папки
