---
title: Данные и параметры
description: Где живут значения вне TestStep — буферы, Test Configuration Parameters, Business Parameters с библиотеками TestStep и Test Data Services.
level: 2
sidebar:
  order: 0
---

TestStep с жёстко прописанным значением приходится править при каждой смене данных. Tosca предлагает несколько способов держать значения вне шагов, каждый для своего вида данных: **Buffer (буфер)** для значений, которые приложение порождает во время выполнения, **Test Configuration Parameter (параметр тестовой конфигурации)** для настроек окружения, **Business Parameter (бизнес-параметр)** для входов переиспользуемого TestStepBlock и **Test Data Services (сервисы тестовых данных)** для данных, которые должны быть уникальными, отслеживаемыми и общими для нескольких приложений. Статический data-driven дизайн через TestSheet описан в [TestCase-Design](/ToscaBase/ru/test-case-design/).

| Документ | Содержание |
|---|---|
| [Буферы](/ToscaBase/ru/data-and-parameters/buffers/) | ActionMode `Buffer`, `{B[имя]}`, динамический XBuffer `{XB[имя]}`, время жизни буфера, Buffer Viewer |
| [Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/) | `{CP[имя]}`, наследование от папок, системные параметры, Configurations уровня проекта, `ConstraintIndex` Module для одинаковых вкладок браузера |
| [Business Parameters и библиотеки TestStep](/ToscaBase/ru/data-and-parameters/business-parameters-and-libraries/) | TestStepBlock, TestStep Library, переиспользуемые TestStepBlock, контейнеры Business Parameter |
| [Test Data Services](/ToscaBase/ru/data-and-parameters/test-data-services/) | Управление тестовыми данными на Tosca Server: репозитории, типы, элементы, обязательные параметры, `{TDS[тип.атрибут]}` |
| [Модули Test Data Service](/ToscaBase/ru/data-and-parameters/test-data-service-modules/) | Создание, поиск, обновление, перенос и удаление элементов из TestCase; Expert Module; массовые данные через Repetitions |

Читайте по порядку: буферы встречаются почти в каждом TestCase, Test Configuration Parameters — в каждом наборе, библиотеки — когда в наборе появились повторяющиеся шаги, а Test Data Services — когда данные делят несколько процессов. Сами буферные стандартные Module описаны в [Операциях с буферами](/ToscaBase/ru/standard-modules/buffer-operations/).
