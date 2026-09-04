---
title: Тестирование API
description: Тестирование REST- и SOAP-сервисов с помощью Tosca API Scan и API Engine — от первого ручного запроса до связанных в цепочку верифицированных API TestCase.
level: 3
sidebar:
  order: 0
---

Tosca тестирует веб-сервисы через API Engine (движок API) и инструмент **Tosca API Scan**. Вы сканируете определение API или записываете живой трафик, чтобы получить сообщения, отправляете и изучаете их в API Scan, а затем экспортируете в Tosca Commander, где они становятся API Module и TestCase с верификациями, буферами и Configuration Parameter — точно как UI-тесты.

| Документ | Содержание |
|---|---|
| [Основы API Scan](/ToscaBase/ru/api-testing/api-scan-basics/) | Зачем тестировать API, запуск API Scan из Commander или standalone, отправка запроса вручную, сканирование файла или URI Swagger, OpenAPI, WSDL, WADL |
| [API TestCases](/ToscaBase/ru/api-testing/api-test-cases/) | Экспорт сообщений, Module запроса и ответа, Technical view, ModuleAttribute, верификация кодов состояния и полей payload, буферизация значений для цепочки запросов, ExecutionList |
| [Аутентификация API](/ToscaBase/ru/api-testing/api-authentication/) | Basic и Digest аутентификация, как Digest устроен внутри, токены и учётные данные при сканировании |
| [Структура сообщений, SOAP и вложения](/ToscaBase/ru/api-testing/api-message-structure-and-soap/) | Validate, Pretty Print, Word Wrap и Search in payload; сканирование и верификация SOAP-калькулятора через Configuration Parameter и MATH; отправка файлов-вложений |
| [Message Recorder](/ToscaBase/ru/api-testing/api-message-recorder/) | Запись трафика работающего приложения и экспорт захваченных вызовов как сообщений |

Читайте по порядку. Первые два документа — основной рабочий процесс; остальные три добавляют к нему аутентификацию, инструменты работы с сообщениями, SOAP и вложения, а также запись трафика.
