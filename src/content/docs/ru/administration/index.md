---
title: Администрирование
description: Многопользовательские workspace на общем репозитории, пользователи и группы, ветки, резервное копирование и версионирование, Test mandates, инструменты командной строки и Tosca Server.
level: 4
sidebar:
  order: 0
---

Всё в этом разделе предполагает команду: несколько человек работают с одними и теми же Module (модулями), TestCase (тест-кейсами) и ExecutionList (списками выполнения) через общий репозиторий, и кто-то это администрирует. Раздел начинается с многопользовательского workspace (рабочего пространства), потому что все остальные возможности существуют только внутри него, и заканчивается Tosca Server — компонентом, соединяющим установки Commander, агентов DEX и CI.

| Документ | О чём |
|---|---|
| [Многопользовательские workspace](/ToscaBase/ru/administration/multi-user-workspaces/) | Типы репозитория (SQLite, Oracle, MS SQL Server, DB2), создание workspace, Update All / Checkout / Checkout Tree / Check In All, сведения об изменениях и checkout, отзыв checkout |
| [Пользователи и группы](/ToscaBase/ru/administration/users-and-groups/) | Создание пользователей и групп, пароли, группа Admins, owning и viewing group на разделах, отключение пользователей, personal data report |
| [Ветки](/ToscaBase/ru/administration/branches/) | Создать ветку, работать в ней в отдельном workspace, слить в Master, удалить |
| [Резервное копирование и восстановление](/ToscaBase/ru/administration/backup-and-restore/) | Export subset для однопользовательских проектов; резервная копия и восстановление репозитория для многопользовательских |
| [Версионирование и восстановление объектов](/ToscaBase/ru/administration/versioning-and-recovery/) | Настройки версионирования, история изменений, восстановление удалённого объекта через Export subset for revision |
| [Test mandates](/ToscaBase/ru/administration/test-mandates/) | Выполнение одного ExecutionList несколькими пользователями без перезаписи результатов |
| [Инструменты командной строки](/ToscaBase/ru/administration/command-line-tools/) | TCShell в интерактивном и скриптовом режиме; клонирование workspace через TCWorkspaceUtil |
| [Tosca Server](/ToscaBase/ru/administration/tosca-server/) | Архитектура, установка, службы, дашборд и DEX monitor |

**Synchronization policy** (политика синхронизации) репозитория — самый частый источник вопросов «почему я не могу взять эту папку на check-out» — объяснена в [Многопользовательских workspace](/ToscaBase/ru/administration/multi-user-workspaces/#synchronization-policy).
