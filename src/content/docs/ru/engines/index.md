---
title: Движки
description: Движки Tosca для документов и трудно сканируемых контролов — Excel, PDF, XML, UIA и WinX для окон десктопа и диалогов браузера, а также Mobile engine и Tricentis Device Cloud для нативных приложений на реальных устройствах.
level: 3
sidebar:
  order: 0
---

Помимо веб-страниц Tosca управляет файлами, нативными окнами и мобильными приложениями через отдельные engines (движки). У каждого движка свой скан (PDF Scan, File Scan) или свой набор стандартных Module (модулей), а к тому, что они предоставляют, применимы те же ActionMode (режимы действия), что и в обычных TestCase (тест-кейсах).

Порядок чтения:

1. [Движок Excel](/ToscaBase/ru/engines/excel-engine/): открытие, создание и сравнение книг, определение диапазонов, чтение и проверка ячеек, буферизация числа строк и столбцов модулями TBox Excel.
2. [Движок PDF](/ToscaBase/ru/engines/pdf-engine/): сравнение двух PDF модулем `1:1 Compare`, сканирование текста, картинок и таблиц через PDF Scan, подсчёт страниц документа без номеров страниц.
3. [Движок XML](/ToscaBase/ru/engines/xml-engine/): открытие и проверка XML по XPath, сканирование XML-файла в Module, связка браузерного, файлового и XML-движков в одном TestCase.
4. [UIA engine и десктопные контролы](/ToscaBase/ru/engines/uia-engine-and-desktop/): смена движка XScan (WinX, UIA, Vision AI), когда Application scan не видит контролы, добавление generic list item в combo box, закрытие JavaScript alert.
5. [Мобильная автоматизация](/ToscaBase/ru/engines/mobile-automation/): доступ к устройству через Tricentis Mobile Agent, привязка конфигураций приложения и подключения к TestCase, открытие нативного Android-приложения модулем `Open Mobile App`, сканирование приложения на реальных устройствах SauceLabs через подключение Cloud APM.
6. [Tricentis Device Cloud](/ToscaBase/ru/engines/device-cloud/): ферма устройств Tricentis с удалённым управлением, performance sessions, которые mobile AI engine превращает в issue cards, и мониторингом производительности user flows.

Об HTML-движке и повседневных веб-контролах см. [Modules](/ToscaBase/ru/modules/), о проблемных контролах в целом — [Troubleshooting](/ToscaBase/ru/troubleshooting/).
