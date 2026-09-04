---
title: "Распределённое выполнение (DEX)"
description: "Настройка распределённого выполнения Tosca с AOS: workspace для AOS, DEX-агент, настройки Commander, Configurations, TestEvent и сопоставление агентов с конфигурациями."
level: 2
sidebar:
  order: 100
sources:
  - id: -hceXOD_WB4
    title: "Tosca Tutorial | Lesson 152 - Tosca Distributed Execution Setup with AOS | DEX Agents| Test Events |"
    url: https://www.youtube.com/watch?v=-hceXOD_WB4
    at: "00:03"
---

**Распределённое выполнение (DEX, distributed execution)** запускает ExecutionList на других машинах, называемых **DEX-агентами**, и параллельно. Вы запускаете **TestEvent (тестовое событие)** из Commander, Tosca Server распределяет его на агента, а результаты возвращаются в репозиторий. Настройка состоит из нескольких частей; этот документ проходит их в том порядке, в каком их нужно делать. Предполагается, что Tosca Server установлен и на нём запущены **Automation Object Service (AOS)** и **Distribution Service** (см. [Tosca Server](/ToscaBase/ru/administration/tosca-server/)).

## Архитектура

- **Commander** (ваш workspace) создаёт и запускает TestEvent.
- **Tosca Server** содержит **AOS** и **DEX-сервер**. У AOS есть собственный workspace, и он посредник: берёт из общего репозитория объекты автоматизации и тестовые данные, нужные событию, и передаёт их DEX-серверу, который раздаёт работу агентам. Когда агенты заканчивают, результаты идут обратно через AOS в репозиторий.
- **DEX-агенты** — машины с процессом агента (с полным Commander или без), которые выполняют тесты.

:::caution
DEX работает только с **многопользовательскими workspace**. Workspace AOS и ваш рабочий workspace должны быть в **одном репозитории**. В демо используется SQLite на одной машине; для продуктива нужны Oracle, SQL Server или DB2 и отдельные машины (см. [Многопользовательские workspace](/ToscaBase/ru/administration/multi-user-workspaces/)).
:::

## Шаг 1: workspace для AOS

На машине с Tosca Server создайте отдельный workspace для AOS:

1. **Create new** workspace, выберите **существующий репозиторий**, который использует ваш многопользовательский workspace (новый не создавайте), ветку `master` и отличающееся имя, например `multi-aos`.
2. **Не** создавайте slim workspace; AOS с ним не работает.
3. На большом репозитории создание может занять много времени, потому что обновляются все объекты.
4. Войдите один раз, чтобы проверить имя корня проекта и совпадение объектов с рабочим workspace, затем закройте.

Никогда не используйте этот workspace для повседневной работы; откройте его — и DEX перестанет работать.

## Шаг 2: регистрация workspace на сервере

В интерфейсе Tosca Server: **Settings > Automation Object Service > Add new**, введите **имя корня проекта** (как показано в workspace, в демо `multi-demo`, а не имя workspace), **имя workspace** (`multi-aos`), логин и пароль. Параллельно может работать до **10** workspace AOS, по одному на проект. **Save** перезапускает связанные службы.

Затем перезапустите DEX-сервер: в **Services** Windows найдите службу Tricentis **Distributed Execution** и перезапустите её, а также службу монитора. Дашборд сервера должен снова показывать, что всё работает.

## Шаг 3: DEX-агент

Исполняемый файл агента поставляется с Commander по пути `...\Tricentis\Tosca Testsuite\Distributed Execution\DEXAgent.exe`. Установщик также предлагает установить **только DEX-агент** вместо полного Commander; это легче и лучше подходит для выделенной машины выполнения. Запускайте от администратора.

Иконка в трее показывает состояние: **белая** — не запущен, **зелёная** — настроен и подключён, **жёлтая** — выполняет, **красная** — настроен неверно. Правый клик по ней — **configure** или **stop**. Поля конфигурации:

- Данные машины (операционная система, память, тип ОС, IP-адрес, имя хоста), определяются автоматически и редактируются.
- Workspace на агенте не нужен.
- **Connect to server**: endpoint DEX-сервера, в демо `localhost:5007`. Проверьте в интерфейсе сервера в **Settings > Automation Object Service > Distribution server address**.
- **Authentication**, если требуется.
- **RDP**: включите и введите логин, пароль и размер рабочего стола, когда агент работает на удалённой машине, чтобы действия мыши и клавиатуры выполнялись даже при заблокированной сессии. Без этого тесты начнут падать, как только машина заблокируется.
- **Logging**: установите `Debug`; файл лога лежит рядом с исполняемым файлом.

Когда иконка зелёная, агент появляется в **DEX monitor > Agent view** сервера в состоянии idle (другие состояния: running, paused, stopped, error). Из монитора можно перезапустить агента и изменить его машинную, RDP- и лог-конфигурацию; endpoint URL меняется только на самом агенте.

## Шаг 4: подключение Commander к серверу

В рабочем workspace, **Project > Settings**:

- **Commander > Distributed Execution**: **Monitor URL** (в демо `http://localhost:8080/monitor`, скопируйте с сервера) и **Server** (endpoint DistributionServerService/ManagerService; меняйте только хост и порт).
- **Tricentis Services**: endpoint сервера, хост плюс порт (`localhost:8080`).

Закройте диалог, чтобы сохранить.

## Шаг 5: Configurations

В разделе Execution папка **Configurations** содержит три конфигурации по умолчанию: `Any` (любой агент), `RDP` (`UseRDP` = true) и `SupportsClassic` (классические Module). Правый клик **Configurations > Refresh agents**: каждый агент показывается под каждой конфигурацией, свойствам которой он соответствует, так что новый агент появится под `Any`. Число агентов на конфигурацию — то, что будет использовать TestEvent.

## Шаг 6: TestEvent

**TestEvent** существуют только в многопользовательских workspace, под папкой Execution. TestEvent нужна **конфигурация** и **ExecutionList**:

1. Возьмите папку TestEvents на check-out и создайте TestEvent (`dex event`).
2. Перетащите на него конфигурацию (`Any` позволяет серверу выбрать свободного агента; конкретная конфигурация закрепляет тип агента).
3. Перетащите на него ExecutionList для запуска. Test mandate и другие объекты выполнения добавляются так же.
4. **Сделайте check in всего**: TestEvent, ExecutionList и его TestCase.
5. Правый клик по TestEvent > **Execute now**.

TestEvent появляется в **Event view** монитора со статусом, временем начала и создателем; откройте его для подробностей. Agent view показывает агента в выполнении, затем снова idle.

:::caution
TestEvent или ExecutionList на check-out приводит к статусу события **cancelled** и «failed to retrieve the needed automation objects». Сначала сделайте check in.
:::

## Собственные конфигурации

Свойства, которые может иметь конфигурация, берутся из `ConfigurationParameters.xml` в установке Tosca Server (в демо `...\Tosca Server\DEX Server\`): операционные системы, объёмы памяти, типы ОС, `UseRDP`, `SupportsClassic`, IP-адрес. Отредактируйте его от администратора, например добавив `Windows 11` в операционные системы или параметр `Browser` со значениями, и сохраните. Затем в Commander:

1. Возьмите корень проекта на check-out, правый клик **Configurations > Update configurations from server** (без корня на check-out завершится ошибкой).
2. Создайте новую конфигурацию (`local`) и задайте её свойства: ОС `Windows 11`, память `16 GB`, тип `64bit`.
3. На агенте задайте **те же** значения в его конфигурации.
4. Check in всего и **Refresh agents**; агент теперь появится под `local`.
5. Замените `Any` в TestEvent на `local`, чтобы запускать только на подходящих агентах.

Конфигурация, свойства агента и XML должны совпадать; в этом всё правило сопоставления.

## Запуск извне Commander

TestEvent можно запускать из CI-конвейера через [Tosca Execution Client](/ToscaBase/ru/execution/tosca-execution-client/).
