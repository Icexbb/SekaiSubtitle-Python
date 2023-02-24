@echo off
chcp 65001
for %%f in (*.ui) do (
    pyside6-uic.exe -o %%~nf.py %%~nf.ui
    echo DONE %%~nf.py
)