::  выключение сервиса в реестре
rem reg DELETE "HKEY_LOCAL_MACHINE\Software\Google\Chrome\NativeMessagingHosts\com.google.chrome.example.echo" /f
rem reg DELETE "HKEY_LOCAL_MACHINE\SOFTWARE\Mozilla\NativeMessagingHosts\com.google.chrome.example.echo" /f
rem reg DELETE "HKEY_LOCAL_MACHINE\SOFTWARE\Mozilla\ManagedStorage\com.google.chrome.example.echo" /f
rem reg DELETE "HKEY_LOCAL_MACHINE\SOFTWARE\Mozilla\PKCS11Modules\com.google.chrome.example.echo" /f
rem REG DELETE "HKLM\Software\Google\Chrome\NativeMessagingHosts\com.google.chrome.example.echo" /f
rem REG DELETE "HKCU\Software\Google\Chrome\NativeMessagingHosts\com.google.chrome.example.echo" /f

REG DELETE "HKCU\Software\Google\Chrome\NativeMessagingHosts\com.google.chrome.example.echo" /f
REG DELETE "HKLM\Software\Google\Chrome\NativeMessagingHosts\com.google.chrome.example.echo" /f


pause

