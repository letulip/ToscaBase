---
title: Test mandate
description: Позвольте нескольким пользователям выполнять один ExecutionList одновременно, не перезаписывая результаты друг друга, связав его с test mandate, и снимите auto-merge-связь, когда она больше не нужна.
level: 4
sidebar:
  order: 60
sources:
  - id: zFHcStTuHbI
    title: "Tosca Tutorial | Lesson 96 - Use Test Mandates to execute same tests simultaneously | Multiple Users"
    url: https://www.youtube.com/watch?v=zFHcStTuHbI
    at: "00:09"
---

В многопользовательском workspace у [ExecutionList](/ToscaBase/ru/execution/execution-lists/) (списка выполнения) один журнал результатов, и для выполнения его нужно взять на check-out. Если несколько пользователей запускают один ExecutionList одновременно, каждый прогон перезаписывает результаты остальных. **Test mandate** (тестовый мандат) решает это: это объект раздела Execution, связанный с ExecutionList, записью выполнения или папкой выполнения. Пользователи выполняют мандат вместо ExecutionList, check-out самого ExecutionList не нужен, а когда все сделали check-in, их результаты собираются в ExecutionList, а не перезаписываются. Test mandate существуют только в многопользовательских workspace.

## Создание test mandate и связывание

1. Возьмите на check-out дерево папки ExecutionList.
2. Щёлкните папку ExecutionList правой кнопкой и выберите **Create Test Mandate**; назовите его (в источнике `Login mandate` для ExecutionList `Login test`).
3. Перетащите ExecutionList (или запись выполнения, или папку выполнения) на мандат. Tosca создаёт его копию в виде папки внутри мандата, включая записи TestCase.
4. В журнале исходного ExecutionList **синяя стрелка** теперь помечает его как связанный с test mandate.
5. **Check In All**, чтобы другие пользователи увидели мандат.

## Выполнение через мандат

Каждый пользователь берёт на check-out мандат (не ExecutionList) и запускает его как ExecutionList; прогон показывает passed или failed как обычно. После **Check In All** откройте исходный ExecutionList: его последнее выполнение помечено как связанное с мандатом и несёт результаты мандата. Когда мандат выполняют несколько пользователей, их результаты собираются в ExecutionList и показываются в мандате, никогда не перезаписывая друг друга.

Из журнала ExecutionList есть команда перехода к соответствующей записи test mandate.

## Снятие связи

Чтобы ExecutionList перестал собирать результаты мандата:

1. Возьмите ExecutionList на check-out.
2. Щёлкните его журнал правой кнопкой и выберите **Clear auto merge list**.

Последний журнал выполнения больше не связан с мандатом, и результаты мандата перестают появляться в ExecutionList.

## См. также

- [Результаты выполнения и журналы](/ToscaBase/ru/execution/execution-results-and-logs/): чтение журнала, который наполняет мандат.
- [Многопользовательские workspace](/ToscaBase/ru/administration/multi-user-workspaces/): правила check-out, из-за которых мандаты необходимы.
