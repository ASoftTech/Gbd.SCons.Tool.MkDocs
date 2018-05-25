@echo off
SETLOCAL

IF EXIST "py36dev" (
    echo "Entering virtual environment py36dev"
    cmd /k "py36dev\Scripts\activate.bat"

) ELSE (
    echo "Creating virtual environment py36dev"
    SET WORKON_HOME=.
    mkvirtualenv --python=C:\Python36\python.exe py36dev
    cmd /k "py36dev\build\activate.bat & pip install -r requirements_py3.txt"
)

ENDLOCAL