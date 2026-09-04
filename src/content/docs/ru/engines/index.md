---
title: Движки
description: Движки Tosca для документов и трудно сканируемых контролов - Excel, PDF, XML, а также UIA и WinX для окон десктопа и диалогов браузера.
sidebar:
  order: 0
---

Помимо веб-страниц Tosca управляет файлами и нативными окнами через отдельные engines (движки). У каждого движка свой скан (PDF Scan, File Scan) или свой набор стандартных Module (модулей), а к тому, что они предоставляют, применимы те же ActionMode (режимы действия), что и в обычных TestCase (тест-кейсах).

Порядок чтения:

1. [Excel engine](/ToscaBase/ru/engines/excel-engine/): открытие, создание и сравнение книг, определение диапазонов, чтение и проверка ячеек, буферизация числа строк и столбцов модулями TBox Excel.
2. [PDF engine](/ToscaBase/ru/engines/pdf-engine/): сравнение двух PDF модулем `1:1 Compare`, сканирование текста, картинок и таблиц через PDF Scan, подсчёт страниц документа без номеров страниц.
3. [XML engine](/ToscaBase/ru/engines/xml-engine/): открытие и проверка XML по XPath, сканирование XML-файла в Module, связка браузерного, файлового и XML-движков в одном TestCase.
4. [UIA engine и десктопные контролы](/ToscaBase/ru/engines/uia-engine-and-desktop/): смена движка XScan (WinX, UIA, Vision AI), когда Application scan не видит контролы, добавление generic list item в combo box, закрытие JavaScript alert.

Об HTML-движке и повседневных веб-контролах см. [Modules](/ToscaBase/ru/modules/), о проблемных контролах в целом — [Troubleshooting](/ToscaBase/ru/troubleshooting/).
