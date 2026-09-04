---
title: Tosca Server
description: Что такое Tosca Server в архитектуре Tosca, как скачать и установить его с версией, совпадающей с Commander, какие сервисы он запускает, как их перезапускать и что показывают дашборд и DEX monitor.
level: 4
sidebar:
  order: 80
sources:
  - id: btvqHGsOLMo
    title: "Tosca Tutorial | Lesson 151 - Tosca Server Setup, Features & Architecture"
    url: https://www.youtube.com/watch?v=btvqHGsOLMo
    at: "00:04"
---

Tosca Server — центральный компонент, с которым взаимодействуют установки Tosca Commander, агенты DEX и CI-клиент. Он объединяет набор служб Windows (REST API, file service, DEX server и DEX monitor, Automation Object Service, license administration, authentication и другие) за одним веб-дашбордом. Он нужен, как только вы хотите [распределённое выполнение](/ToscaBase/ru/execution/distributed-execution-dex/), [Test Data Services](/ToscaBase/ru/data-and-parameters/test-data-services/) или центральное администрирование лицензий и пользователей. Этот документ описывает архитектуру, установку и обслуживание служб; настройка DEX — в разделе о выполнении.

## Архитектура

Диаграмма архитектуры в источнике помещает Tosca Server в центр, соединяя его с:

- **уровнем базы данных** (общий репозиторий);
- установками **Tosca Commander**;
- **агентами DEX**, которые получают тестовые события от DEX server;
- **Tosca CI client**, используемым для построения CI/CD-конвейеров;
- **уровнем лицензий**.

Службы внутри Tosca Server, как они названы в источнике: REST API service, file service, DEX monitor, DEX server, Automation Object Service (AOS), license administration, authentication service, gateway и Test Data Services (TDS).

## Мощность и размещение

Tosca Server запускает много служб и потребляет заметно больше ресурсов, чем Commander. Реальная инсталляция состоит из машин трёх видов: **выделенный Windows-сервер** (физический или облачный) для Tosca Server, отдельные машины для пользователей Commander и отдельные машины для агентов DEX. Установка Server и Commander на один ПК годится для практики, если машина выдерживает обоих, — так делает источник; это не production-конфигурация.

## Скачивание

1. Откройте портал поддержки Tricentis и перейдите в product support.
2. Выберите версию Tosca и откройте её раздел загрузок.
3. Скачайте установщик **Tosca Server** этой версии.

:::caution
Версия Server должна совпадать с установленной версией Commander. У автора был Commander 14.3, сервера 14.3 на портале не нашлось, и он обновил Commander до 16.0, прежде чем ставить Server 16.0. Либо обновите Commander до версии, которую можно скачать, либо скачайте сервер, совпадающий с Commander.
:::

## Установка

Установщик работает так же, как у Commander:

1. Запустите `.exe` и нажмите **Continue**; сначала ставятся недостающие предварительные компоненты.
2. Показывается список устанавливаемых служб (gateway, license administration, AOS, distributed execution, file service, REST API и другие). Оставьте расположение по умолчанию или измените.
3. Выберите **HTTP** или **HTTPS**. Для HTTPS нужен сертификат, отпечаток (thumbprint) которого вы вводите и который должен совпадать; для демонстрации автор использует HTTP.
4. Выберите порт. По умолчанию 80; если он занят (как на ПК автора), введите другой, например `8080`. Сервер тогда доступен по `http://localhost:8080`.
5. Подтвердите расположение установки file service и запустите установку. Она занимает несколько минут.

По завершении Tosca Server открывается в браузере вместе со страницей **settings**.

## Дашборд и настройки

Дашборд — стартовая страница для администраторов и пользователей с доступом к серверу. Плитки, названные в источнике:

- **Test Data Services (TDS)**
- **License administration**
- **User administration**
- **Administration console**
- **Distributed execution**, открывающая DEX monitor

Страница **Settings** перечисляет каждую службу с её портом, endpoint URL и конфигурацией. Измените значение и нажмите **Save** — затронутая служба перезапустится. Каждая используемая служба должна быть в состоянии running, а каждый порт — свободен на машине, иначе служба недоступна. Неиспользуемые службы могут оставаться остановленными.

## Перезапуск служб

Три равнозначных способа:

1. **Страница Settings**: нажмите **Save**; служба перезапускается.
2. **Диспетчер задач > Службы**: перечислены службы Tricentis; запустите, остановите или перезапустите (перезапуск проходит через stopped к running).
3. **Службы Windows** (`services.msc`): тот же список со статусами, для мониторинга и перезапуска.

Файлы конфигурации лежат в `C:\Program Files\Tricentis\Tosca Server\`, по папке на службу (включая `DEX monitor` и `DEX server`). Некоторые настройки, в том числе распределённое выполнение, требуют правки этих файлов.

## DEX monitor

Плитка **Distributed execution** открывает DEX monitor — веб-страницу с двумя представлениями:

- **Agents**: каждый агент DEX, подключённый к серверу, с его состоянием (running или ошибка). Отсюда агентов можно перезапускать. Пока агенты не настроены, счётчик равен нулю.
- **Events**: каждое тестовое событие, запущенное из Commander, с его состоянием (running, passed, failed). Отсюда события можно останавливать.

URL монитора доступен, как только Tosca Server установлен. Настройка агентов и запуск тестовых событий описаны в [Распределённое выполнение](/ToscaBase/ru/execution/distributed-execution-dex/).

## См. также

- [Лицензирование](/ToscaBase/ru/getting-started/licensing/) и [Установка](/ToscaBase/ru/getting-started/installation/) Commander.
- [Многопользовательские workspace](/ToscaBase/ru/administration/multi-user-workspaces/): репозиторий на уровне базы данных.
