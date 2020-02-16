::  включение сервиса в реестре
REG ADD "HKLM\Software\Google\Chrome\NativeMessagingHosts\com.google.chrome.example.echo" /ve /t REG_SZ /d "%~dp0manifest_service_win.json" /f
REG ADD "HKCU\Software\Google\Chrome\NativeMessagingHosts\com.google.chrome.example.echo" /ve /t REG_SZ /d "%~dp0manifest_service_win.json" /f
pause
