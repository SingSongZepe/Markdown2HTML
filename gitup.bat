@echo off

git add .
if not "%1" == "" (
	git commit -m "%1"
) else (
	git commit -m "daily"
)
git push -u origin main

pause
	