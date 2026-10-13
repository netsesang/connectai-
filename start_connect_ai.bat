@echo off
chcp 65001 > nul
set "HTML_PATH=file:///D:/Project_Act/97.Connect AI Lab/assets/webview/dashboard_app.html"

rem 1. Check Chrome
if exist "C:\Program Files\Google\Chrome\Application\chrome.exe" (
    start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --app="%HTML_PATH%" --window-size=1200,860
    exit /b 0
)

rem 2. Check Edge
if exist "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" (
    start "" "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --app="%HTML_PATH%" --window-size=1200,860
    exit /b 0
)

rem 3. Fallback to default browser
start "" "D:\Project_Act\97.Connect AI Lab\assets\webview\dashboard_app.html"
exit /b 0
