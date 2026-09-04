---
title: TestCase для API
description: Экспорт сообщений из API Scan в Tosca Commander, добавление ModuleAttribute для кодов состояния и полей payload, верификация ответов, буферизация значений для цепочки запросов и запуск API TestCase из ExecutionList.
level: 3
sidebar:
  order: 20
sources:
  - id: NXR5dZ-DYHw
    title: "Tricentis Tosca Tutorial Part-13: Advance Tosca Api Testing And Tosca API Test Case"
    url: https://www.youtube.com/watch?v=NXR5dZ-DYHw
    at: "00:15"
  - id: rdxTMtZrVEs
    title: "Tosca Tutorial | Lesson 81 - Generate & Execute API Test Cases | API Testing |"
    url: https://www.youtube.com/watch?v=rdxTMtZrVEs
    at: "02:08"
  - id: 4Y9u474ohJM
    title: "Tosca Tutorial | Lesson 82 - Buffer API Response Values | Configure Request Parameters | API Testing"
    url: https://www.youtube.com/watch?v=4Y9u474ohJM
    at: "01:16"
  - id: tkUDG21IiMA
    title: "Tosca Tutorial | Lesson 86 - Scan & Verify SOAP API Messages | API Testing |"
    url: https://www.youtube.com/watch?v=tkUDG21IiMA
    at: "03:13"
---

Сообщения в [API Scan](/ToscaBase/ru/api-testing/api-scan-basics/) можно отправлять, но не верифицировать и не параметризовать. Чтобы протестировать API, сообщения экспортируются в Tosca Commander, где каждое становится парой **API Module (API-модулей)** и одним TestCase. Затем вы добавляете ModuleAttribute для нужных полей, верифицируете ответ, буферизуете значения из одного ответа для следующего запроса и запускаете всё из ExecutionList.

## Экспорт сообщений из API Scan

1. В Commander создайте **component folder (папку компонента)** для API (например, `API testing`) и **выделите её**. Если ничего не выделено, экспорт попадёт в корневую папку. Workspace или хотя бы целевая папка должны быть взяты на **check-out** (взятие на редактирование); в многопользовательском workspace экспорт иначе завершается ошибкой (см. [Многопользовательские workspace](/ToscaBase/ru/administration/multi-user-workspaces/)).
2. В API Scan **выделите все сообщения**, которые хотите экспортировать. Экспортируются только выделенные; при одном выделенном сообщении получите ровно одно.
3. Откройте **API Test Case > Export** и после завершения закройте API Scan.

Если API Scan запущен standalone, то же меню сохраняет **subset (подмножество)** — файл `.tsu`. В Commander выделите папку компонента, импортируйте subset и получите папку импорта с теми же Module и TestCase. При запуске API Scan из Commander объекты появляются сразу (в части LambdaGeeks — в папке `API Scan_import`).

Что создаёт экспорт:

- **Module**: **по два на сообщение** — для запроса и для ответа, в папках, повторяющих папки сообщений. Три сообщения дают шесть Module. Их можно переименовать под своё приложение.
- **TestCase**: по одному на сообщение, каждый с **двумя TestStep** — запрос и ответ.

## Technical view

У API Module есть дополнительная вкладка **Technical view (техническое представление)**, которой нет у обычных отсканированных Module. Это то же представление, что в API Scan: метод, endpoint, resource, header-параметры и payload для запроса; код состояния, время ответа и payload для ответа. Поскольку всё нужное сообщению хранится там, сгенерированный TestCase запускается как есть, без открытия API Scan.

Запустите один и посмотрите лог: тест проходит, но сообщает лишь время ответа сервера. Ничего ещё не проверено.

## Добавление ModuleAttribute

Чтобы что-то верифицировать или параметризовать, превратите элементы сообщения в ModuleAttribute. Это API-аналог Business Parameter (бизнес-параметров): значения, задаваемые в каждом TestCase.

1. Откройте Module и его **Technical view**.
2. Выделите элемент: код состояния, поле payload, время ответа или параметр. Работает множественное выделение; выделив всё, вы добавите все элементы payload разом.
3. Нажмите **Add** вверху вкладки **API Testing**.

Атрибут сразу появляется во всех TestCase, использующих этот Module. В TestStep выберите значение из выпадающего списка (там значения, захваченные при сканировании) или введите своё и задайте ActionMode (см. [ActionModes](/ToscaBase/ru/test-cases/action-modes/)).

В части LambdaGeeks то же делается через **Attribute assistant (помощник атрибутов)**: он открывается опцией **Buffer module attributes with dynamic list items**; выделите поля (для запроса логина — `username` и `password`; для Module ответа — `status code` и нужные поля payload, например `token`, `id` или `name`) и нажмите **Add**. Ненужные для теста атрибуты просто не создаются.

## Верификация ответа

Минимальная верификация для любого запроса — **код состояния**: добавьте его из Module ответа, задайте значение `200` и ActionMode `Verify`. Лог покажет ожидаемое и фактическое значение, и TestCase упадёт при расхождении. Поля payload добавляются так же; в примере с Petstore `name`, отправленный в `POST`, верифицируется в ответе.

:::caution
Сканирование захватывает значения последнего запуска. В источнике имя в запросе изменили после сканирования, поэтому Module ответа хранил старое имя, а для кода состояния был записан `404` из неудачного прогона. Не доверяйте отсканированным значениям: настраивайте значения, которые отправляете, и верифицируйте значения, которые ожидаете.
:::

Чтобы отправить другое значение, добавьте поле и из Module **запроса** и задайте его в TestStep запроса (`Max` для имени питомца в примере).

## Буферизация значений для цепочки запросов

`GET` или `DELETE` по ID требуют ID, который вернул `POST`. Свяжите запросы через буфер (см. [Буферы](/ToscaBase/ru/data-and-parameters/buffers/)):

1. В Module ответа `POST` добавьте `id` как ModuleAttribute.
2. В TestCase `POST` задайте ему ActionMode `Buffer`, а в значении укажите имя буфера, например `B_pet_ID`.
3. В Module запросов `GET` и `DELETE` добавьте path-параметр `petId` (а для `DELETE` ещё header `api_key`) как ModuleAttribute.
4. В этих TestCase задайте `petId` = `{B[B_pet_ID]}`. Константа вроде API-ключа может остаться литералом или стать Configuration Parameter (см. [Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/)).

Запустите `POST` в ScratchBook: лог покажет возвращённый ID, сохранённый в `B_pet_ID`, и последующие запросы его используют. Добавьте верификацию кода состояния и в ответы `GET` и `DELETE`.

Порядок важен, поэтому переименуйте TestCase в `01_post_request`, `02_get_request`, `03_delete_request` и перетащите их в эту последовательность. Полезный негативный TestCase — `GET` по ID после `DELETE`, который должен вернуть `404`.

## Разобранный пример: логин по токену, создание, проверка

Часть LambdaGeeks строит один TestCase `Add Coffee` против примера Swagger-сервиса Tricentis с тремя папками TestStep: `Authentication`, `Post Coffee`, `Verify New Coffee`. Перетащите Module запроса и ответа в соответствующие папки.

| TestStep | Значения |
|---|---|
| Login request | `username`, `password` |
| Login response | Verify `status code` = `200`; буфер `token` под именем `auth_token` |
| Post coffee request | `name` = `test 1`, `description` = `test coffee`, `authorization` = слово `token`, пробел, затем `{B[auth_token]}` |
| Post coffee response | Verify `status code`; буфер `id` |
| Get coffee by id request | `id` = буферизованный id, `authorization` как выше |
| Get coffee by id response | Verify `status code` = `200`, verify `name` = `test 1` |

## Запуск API TestCase

Запускайте из ScratchBook или создайте папку ExecutionList (например, `API Suite`), сам ExecutionList (`Swagger App`), перетащите туда TestCase, сохраните порядок и нажмите **Run** (см. [ExecutionLists](/ToscaBase/ru/execution/execution-lists/)). Во время выполнения UI не появляется. Лог выполнения показывает статус каждого запроса и ответа, буферизованное значение и значение, использованное позже; [Buffer Viewer](/ToscaBase/ru/data-and-parameters/buffers/) перечисляет буферы. После этого сохраните workspace и сделайте check-in.
