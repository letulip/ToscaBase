---
title: Мобильная автоматизация
description: Настройка Mobile engine с Tricentis Mobile Agent, привязка конфигураций приложения и подключения к TestCase, первый Android TestCase с Open Mobile App на реальном устройстве и эмуляторе, сканирование нативного приложения на реальных устройствах SauceLabs через подключение Cloud APM.
level: 3
sidebar:
  order: 50
sources:
  - id: wpkwzSAGpgs
    title: "Tosca Mobile Automation - Lesson 05 | Automate First Mobile Test Case for Android | Test Automation"
    url: https://www.youtube.com/watch?v=wpkwzSAGpgs
    at: "02:16"
  - id: ohfGxtWWRno
    title: "Tosca Mobile Automation - Lesson 06 | Scan Native App using SauceLabs | SauceLabs Integration"
    url: https://www.youtube.com/watch?v=ohfGxtWWRno
    at: "05:32"
---

Mobile engine (мобильный движок) управляет нативными приложениями Android и iOS так же, как HTML engine — веб-страницей: приложение сканируется в Module (модуль), TestStep (шаги теста) собираются с обычными ActionMode (режимами действия), затем запуск. Отличается обвязка. До устройства Tosca добирается через **Tricentis Mobile Agent** (TMA) — отдельный сервис с собственной консолью, а само устройство либо подключено к машине с агентом (USB, Wi-Fi, эмулятор Android Studio), либо арендовано в облачной ферме: SauceLabs, BrowserStack или [Tricentis Device Cloud](/ToscaBase/ru/engines/device-cloud/). Здесь описаны конфигурации, которые создаёт мобильный скан, первый Android TestCase (тест-кейс) и сканирование нативного приложения на устройствах SauceLabs.

:::note
Уроки 1–4 мобильной серии (установка Tricentis Mobile Agent, Android Studio и виртуальные устройства, подключение Android-телефона по USB или Wi-Fi, сканирование нативного приложения через **Scan > Mobile**) в загруженный плейлист не входят. Этот документ начинается там, где они заканчиваются: устройство видно в консоли агента, а приложение (APK *Tip calculator*) отсканировано в Module.
:::

## Что оставляет после себя мобильный скан

**Scan > Mobile** перед открытием сканера спрашивает подключение, устройство и приложение и сохраняет выбранное под узлом проекта в **Configurations > Mobile**:

- **Applications**: по записи на каждое отсканированное приложение — `ApplicationID` (полный путь к APK), платформа и тип приложения.
- **Connections**: `Local` и `Remote`. Удалённое подключение содержит адрес сервера TMA и тип `TMA`.

Эти записи — [Test Configuration Parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/), и каждому мобильному TestCase они должны быть привязаны до выполнения первого шага.

## Первый Android TestCase

Сценарий: открыть калькулятор чаевых, ввести базовую цену, проверить итог, который приложение считает с чаевыми по умолчанию.

1. Создайте папку `Mobile automation` и TestCase `Tip calculator basic test`.
2. Откройте вкладку **Test configurations** этого TestCase. Перетащите вкладку проекта вправо, чтобы TestCase и проект оказались рядом, раскройте **Configurations > Mobile** и перетащите на конфигурации TestCase запись приложения (`Tip calculator`) и нужное подключение (в источнике `Remote`: телефон подключён к другой машине, где работает агент).
3. Добавьте третий параметр: правая кнопка, **Create test configuration parameter**, из предложенных имён выберите `DeviceName`. Его значение — **UDID** устройства. Щёлкните правой кнопкой значок TMA в трее, выберите **Open console > Configure devices** и скопируйте UDID устройства; у каждого устройства он свой.
4. Первый TestStep — стандартный Module **TBox Engine > Mobile > Open Mobile App** (правая кнопка на TestCase, **Search and add TestStep**, набрать имя). В `Application` введите `{CP[ApplicationID]}`: после `{CP[` Tosca показывает параметры, привязанные к TestCase, а `ApplicationID` раскрывается в путь к APK. Каждый мобильный TestCase начинается с этого шага.
5. Перетащите ниже отсканированный Module приложения и назовите шаг `Validate the total price`: базовое текстовое поле получает `2000` с ActionMode `Input`, итог — `2300` с ActionMode `Verify`.
6. Сохраните и выполните **Run in ScratchBook**. Tosca сначала устанавливает APK на устройство (так при каждом прогоне), открывает приложение, вводит значение и проверяет; окно-зеркало показывает экран телефона во время прогона.

:::caution
Первый прогон падает: ожидание `2300`, факт `2300.0`. Приложение показывает итог с десятичным знаком, поэтому проверяемое значение нужно писать так, как его отображает приложение.
:::

### Тот же TestCase на эмуляторе

Запустите Android Virtual Device из Device Manager в Android Studio. Он появится в консоли TMA рядом с реальным телефоном, со своим UDID (`emulator-54xx`). Измените только параметр `DeviceName` и запустите снова: APK ставится на эмулятор, и те же шаги проходят.

## Сканирование нативного приложения на SauceLabs

Чтобы сканировать или выполнять тесты на устройстве SauceLabs, нужны учётная запись, загруженное туда приложение и подключение другого типа в Tosca.

Сначала подготовьте SauceLabs:

- **App Management**: загрузите APK (Android) и IPA (iOS) приложения; в источнике используется образец *Swag Labs*, который предоставляет SauceLabs.
- **Live > Mobile App** перечисляет доступные реальные устройства (Google Pixel, Samsung Galaxy, iPhone XR, iPhone 12). На странице каждого устройства виден его уникальный id, например `iPhone_XR_free`.
- **Account > User settings** показывает **OnDemand URL** — адрес, к которому подключается Tosca.

Затем в Tosca щёлкните правой кнопкой **Modules** и выберите **Scan > Mobile**:

1. **Add connection**: имя (`SauceLabs connect`), тип **Cloud APM** вместо `TMA`, а как адрес APM-сервера — OnDemand URL (см. предупреждение ниже).
2. **Add device**: имя, **Device ID**, скопированный со страницы устройства, операционная система (iOS или Android) и признак *real device*. В источнике добавлены iPhone XR и Samsung Galaxy.
3. **Add app**: тип приложения **Native**, имя (`SauceLabs_Android`), а как **Full path** — `storage:filename=<имя файла>`, где имя файла берётся в SauceLabs из **App Management > приложение > Settings > App version**; затем тип приложения (APK или iOS).
4. Выберите подключение, устройство и приложение, нажмите **Connect**, дождитесь *connection established, device is connected*, затем **Scan**. Рядом со сканером откроется живой экран облачного устройства. Выберите контролы (username и password — через **Make unique**, если сканер сообщает, что контрол не уникален; кнопку входа — через **Select on screen**), сохраните Module (`Mobile app Android`) и закройте скан; живой экран закроется вместе с ним.
5. Повторите с iPhone XR и записью приложения для IPA (`storage:filename=<имя ipa-файла>`, тип iOS), чтобы получить `Mobile app iOS`.

:::caution
В версии Tosca 2023, показанной в уроке 6, диалог **Add connection** отвергает полный OnDemand URL как недопустимый, а с URL, обрезанным до части, начинающейся с `ondemand`, **Connect** падает с ошибкой *failed serving request POST*. Обходной путь: добавьте подключение с укороченным URL, затем откройте в проекте **Configurations > Mobile > Connections > SauceLabs connect**, вставьте полный OnDemand URL в поле APM-сервера и сохраните. После этого диалог скана показывает полный адрес, и Connect работает. Полный URL содержит ваше имя пользователя и ключ SauceLabs, поэтому обращайтесь с этой конфигурацией как с секретом.
:::

BrowserStack и Tricentis Device Cloud подключаются тем же путём: подключение Cloud APM, устройства, приложения, затем скан.

## См. также

- [Test configuration parameters](/ToscaBase/ru/data-and-parameters/test-configuration-parameters/): группа параметров `Mobile` и синтаксис `{CP[...]}`.
- [Tricentis Device Cloud](/ToscaBase/ru/engines/device-cloud/): что ферма устройств Tricentis добавляет помимо выполнения TestCase.
- [XScan](/ToscaBase/ru/modules/xscan/): сканирование в целом.
