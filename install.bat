@echo off
title Craftrise Checker Setup 
color 0b
echo ========================================================
echo        CRAFTRISE CHECKER - OTOMATIK KURULUM
echo ========================================================
echo.

echo [*] Python ve kutuphaneler kontrol ediliyor...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    color 0c
    echo [X] HATA: Bilgisayarinizda Python kurulu degil! Lutfen Python yukleyin.
    pause
    exit
)

echo [*] Gerekli kutuphaneler (requests, colorama) yukleniyor...
pip install requests colorama --upgrade >nul 2>&1

echo.
echo [+] Kurulum basariyla tamamlandi!
echo [*] Program baslatiliyor...
echo.
python cr.py
pause