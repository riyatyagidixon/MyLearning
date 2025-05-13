@echo off
cd /d %~dp0

set CONTAINER_NAME=ping-app-mongo

echo ==================================================
echo    POST-CLEANUP: Shutting Down Project
echo ==================================================

echo Stopping MongoDB container: %CONTAINER_NAME% ...
docker stop %CONTAINER_NAME%

echo Removing MongoDB container: %CONTAINER_NAME% ...
docker rm %CONTAINER_NAME%

echo.
echo ==================================================
echo    Cleanup Completed Successfully!
echo ==================================================
echo.