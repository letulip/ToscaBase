---
title: Архитектура
description: Компоненты пакета Tosca — Tosca Commander, XScan, Executor, репозиторий тестов и сервер лицензий — и интерфейсы, через которые используется Tosca.
level: 1
sidebar:
  order: 20
sources:
  - id: qTmnXrP3Dqw
    title: "Tosca Testing Tutorial Part 1:  What is Tosca, Tosca, Architecture, Introduction"
    url: https://www.youtube.com/watch?v=qTmnXrP3Dqw
    at: "05:35"
  - id: 4At7coUGDJU
    title: "Tosca Tutorial | Lesson 1 - Introduction To Tosca | What is Tosca | Codeless Automation Tool |"
    url: https://www.youtube.com/watch?v=4At7coUGDJU
    at: "05:35"
---

Tosca — не одна программа, а пакет. Та часть, в которой вы работаете каждый день, — Tosca Commander; за ним стоят сканер, создающий Module (модули), исполнитель, запускающий TestCase, репозиторий, где всё хранится, и сервер лицензий, решающий, кто может пользоваться инструментом. Понимание того, какой компонент за что отвечает, упрощает чтение остальной базы знаний: Module приходят из XScan, результаты — из Executor, а многопользовательский workspace — это репозиторий.

## Компоненты

| Компонент | Роль |
|---|---|
| **Tosca Commander** | Основное приложение. Создание, управление, выполнение и анализ автоматизации: разработка TestCase, выполнение, сопровождение и отчётность происходят здесь. См. [Обзор Commander](/ToscaBase/ru/getting-started/commander-overview/) |
| **Tosca XScan** (мастер сканирования) | Сканирует тестируемое приложение и сохраняет техническую информацию о его контролах в Module, которые затем используются для идентификации и управления элементами экрана. См. [XScan](/ToscaBase/ru/modules/xscan/) |
| **Tosca Executor** | Выполняет TestCase на тестовых объектах, управляет выполнениями и их логами. См. [ExecutionList](/ToscaBase/ru/execution/execution-lists/) |
| **Репозиторий тестов** | Хранит TestCase, Module, динамические тестовые данные, информацию о пользователях и связанные артефакты в общей базе данных. В источнике названы Oracle, SQL Server, DB2 (для небольших многопользовательских установок используется SQLite; см. [Workspace и настройка проекта](/ToscaBase/ru/getting-started/workspace-and-project-setup/)) |
| **Сервер лицензий** | Настраивает, подключает и проверяет лицензии, чтобы пользователи могли работать в Tosca. См. [Лицензирование](/ToscaBase/ru/getting-started/licensing/) |

:::note
Учебник LambdaGeeks описывает Tosca как «пять компонентов», включая сервер лицензий; вводный урок QASCRIPT перечисляет четыре (Commander, Executor, XScan, репозиторий тестов) и описывает репозиторий как хранилище «тестовых данных, нужных для выполнения». Оба описания — упрощения одного пакета; таблица выше их объединяет.
:::

## Интерфейсы

Доступ к Tosca возможен через несколько интерфейсов:

- **GUI** — графический интерфейс Tosca Commander, обычный способ работы.
- **API** — программный доступ для интеграций.
- **CLI** — командная строка для автономного выполнения и администрирования. См. [Инструменты командной строки](/ToscaBase/ru/administration/command-line-tools/).
- **Интегрированная среда управления тестированием** — доступ из инструментов управления тестированием, в которые встроена Tosca.

## Как части работают вместе

1. Тестировщик открывает **Tosca Commander**, подключённый к workspace (локальный файл или общий репозиторий для команды).
2. **XScan** сканирует приложение и создаёт **Module** в этом workspace.
3. TestCase собираются из Module и группируются в **ExecutionList (списки выполнения)**.
4. **Executor** выполняет ExecutionList локально или на распределённых агентах и записывает результаты и логи обратно в репозиторий.
5. Каждый экземпляр Commander и каждый агент получает лицензию с **сервера лицензий** — облачного сервера Tricentis или собственного.

Связанное: [Что такое Tosca](/ToscaBase/ru/getting-started/what-is-tosca/), [Распределённое выполнение](/ToscaBase/ru/execution/distributed-execution-dex/), [Tosca Server](/ToscaBase/ru/administration/tosca-server/).
