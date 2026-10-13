@echo off
chcp 65001 > nul
title Connect AI — AI 1인 기업 · 나만의 에이전트 팀 실행기
cd /d "%~dp0"

echo ========================================================
echo   Connect AI — AI 1인 기업 · 나만의 에이전트 팀 실행 중...
echo ========================================================

start "" "C:\Users\netse\AppData\Local\Programs\Antigravity IDE\Antigravity IDE.exe" --user-data-dir="C:\Google antigravity paulnteddy" "%~dp0"
exit /b 0
