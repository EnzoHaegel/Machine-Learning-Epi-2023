@echo off

REM This batch file assumes that Python is already installed on the system.

REM Define the environment name
SET ENV_NAME=env_SML_EPI_23

REM Create a virtual environment
python -m venv %ENV_NAME%

REM Activate the virtual environment
CALL %ENV_NAME%\Scripts\activate

REM Upgrade pip to the latest version
python -m pip install --upgrade pip

REM Install requirements from requirements.txt
pip install -r requirements.txt

echo Setup completed. Environment '%ENV_NAME%' is ready to use.
echo Activate it using the command: CALL %ENV_NAME%\Scripts\activate
