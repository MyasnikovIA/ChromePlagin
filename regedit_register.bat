::  включение сервиса в реестре
REG ADD "HKLM\Software\Google\Chrome\NativeMessagingHosts\ru.bars.group.plagin.barspy" /ve /t REG_SZ /d "%~dp0manifest_service_win.json" /f
REG ADD "HKCU\Software\Google\Chrome\NativeMessagingHosts\ru.bars.group.plagin.barspy" /ve /t REG_SZ /d "%~dp0manifest_service_win.json" /f
pause
