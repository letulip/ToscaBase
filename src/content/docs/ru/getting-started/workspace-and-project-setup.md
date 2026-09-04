---
title: Workspace и настройка проекта
description: Что такое workspace в Tosca, чем однопользовательский workspace отличается от многопользовательского, стандартный шаблон workspace и пошаговое создание однопользовательского workspace.
level: 1
sidebar:
  order: 50
sources:
  - id: c-VgJF2i1mU
    title: "Tricentis Tosca Tutorial Part-3 : Tosca Initial Project Setup, Tosca Workspace Overview & Creation"
    url: https://www.youtube.com/watch?v=c-VgJF2i1mU
    at: "00:15"
  - id: 6Z-XkFoVoxw
    title: "Tosca Tutorial | Lesson 5 - Create First Test Case | Tosca Commander | New Workspace |"
    url: https://www.youtube.com/watch?v=6Z-XkFoVoxw
    at: "00:05"
  - id: qzYWlZJ8oac
    title: "Tosca Tutorial | Lesson 3 - Setup Tosca 16 | AWS EC2 | Virtual Windows Server | Cloud |"
    url: https://www.youtube.com/watch?v=qzYWlZJ8oac
    at: "18:39"
---

**Workspace (рабочее пространство)** — репозиторий, в котором работает Tosca Commander. Всё, что вы создаёте (Module, TestCase, тестовые данные, ExecutionList, требования), живёт в workspace, и к нему нужно подключиться прежде, чем что-либо разрабатывать, сопровождать или выполнять. Сам workspace определяется на локальной машине; его данные могут храниться локально или синхронизироваться с базой данных, выступающей общим репозиторием для команды. Первое, что нужно сделать после установки и лицензирования Tosca, — создать workspace.

## Однопользовательский и многопользовательский workspace

| | Single-user (однопользовательский) | Multi-user (многопользовательский) |
|---|---|---|
| Кто подключается | Один пользователь | Несколько пользователей |
| Центральный репозиторий | Не нужен | Обязателен: база данных (Oracle, SQLite, DB2, MS SQL Server) |
| Управление данными | Локально | Общее; записи нужно **взять на редактирование (check-out)** перед изменением и **вернуть (check-in)** после |
| Вход | Нет | По учётным данным; пользователь по умолчанию `Admin` с пустым паролем |

Для изучения Tosca достаточно однопользовательского workspace — именно его предполагает остальная часть раздела. Когда команда работает с общими Module и TestCase, каждый участник вместо этого получает workspace, подключённый к общему репозиторию. Какой вид создаётся, определяет поле **Type of repository** в диалоге создания: `None` — однопользовательский workspace, любой тип базы данных — многопользовательский. Типы репозитория, процедура создания многопользовательского workspace, экран входа и цикл check-out/check-in описаны в [Многопользовательских workspace](/ToscaBase/ru/administration/multi-user-workspaces/); пользователи, группы и ветки — в [Пользователях и группах](/ToscaBase/ru/administration/users-and-groups/) и [Ветках](/ToscaBase/ru/administration/branches/).

## Шаблон workspace

Диалог создания предлагает **Use workspace template**. Стандартный шаблон `Standard.tsu` наполняет workspace стандартными Module ([Стандартные модули](/ToscaBase/ru/standard-modules/)), reusables, шаблонами отчётов и примерами TestCase, нужными каждому проекту. Всегда используйте его для нового проекта; можно подставить и собственный шаблон.

Если шаблон не отображается в списке, найдите его вручную: он лежит в папке проектов Tosca `C:\Tosca_Projects\`, где также есть папки `Common Repositories` и `Workspaces`, в подпапке `Tosca Commander` как `Standard.tsu` (названия папок — как произнесены в источнике).

## Создание однопользовательского workspace

1. Запустите Tosca Commander. На стартовой странице нажмите **Create new**.

   :::note
   До Tosca 14.x команда называлась **Project > New**. В текущих версиях она на стартовой странице.
   :::

2. **Type of repository**: `None`.
3. **Location**: оставьте путь по умолчанию (папка внутри `Workspaces`).
4. **Name**: имя workspace, например `Training`.
5. Отметьте **Use workspace template** и оставьте `Standard.tsu`.
6. Нажмите **OK**. Создание занимает несколько секунд; появляется сообщение об успехе, кнопка **Close** становится активной.
7. Закройте диалог. Commander загружает новый workspace с разделами по умолчанию (TestCases, TestCase-Design, Execution и т. д.; см. [Обзор Commander](/ToscaBase/ru/getting-started/commander-overview/)).

Чтобы увидеть иерархию workspace, нажмите **Project** на вкладке **Home**.

## Далее

Когда workspace открыт, переходите к [Обзору Commander](/ToscaBase/ru/getting-started/commander-overview/), чтобы изучить разделы, затем к [Первому TestCase](/ToscaBase/ru/getting-started/first-test-case/).
