# ChromePlagin 

Плагин для хрома.
При помощи этого исходника можно обращается к Python скрипту из JavaScript
<br/>service.py содержит функции обработки команд на стороне клиента 
<br/>После установки плагина в JS коде на любой закладки появляется объект BarsPy.
Для запуска калькулятора необходимо в консоли ввести команду BarsPy.send('calc')
Для запуска блокнота требуется команда BarsPy.send('notepad') 
После ввода этих команд запускается скрипт service.py, с бесконечным циклом.
на каждой новой закладке, после ввода команды BarsPy.send('***') в клиентской системе, запускается новый экземпляр программы
 

<h3>Установка</h3>
1)Изменить название сервиса с "com.google.chrome.example.ech" на тот, который необходим в файлах:
<br/>       a) linux_install_host.sh
<br/>       b) manifest_service_linux.json
<br/>       c) manifest_service_win.json
<br/>       d) regedit_register.bat
<br/>       e) regedit_un_register.bat
<br/>       f) ServiceApp/js/background.js
<br/>       g) ServiceApp/js/content.js

2) Загружаем плагин из каталога ServiceApp
3) Запускаем под Windows файл regedit_register.bat 

<br/>Доступ к окну по URL  chrome-extension://knldjmfmopnpolahpmmgbagdohdnhkik/main.html
<br/>https://overcoder.net/q/512991/api-chrome-native-messaging-chromeruntimeconnectnative-%D0%BD%D0%B5-%D1%8F%D0%B2%D0%BB%D1%8F%D0%B5%D1%82%D1%81%D1%8F-%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%B5%D0%B9
<br/> chrome://apps
