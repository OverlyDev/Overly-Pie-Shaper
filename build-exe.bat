@echo off

echo Creating packaging directory
if not exist "packaging" mkdir "packaging"

create-version-file metadata.yml --outfile packaging/file_version_info.txt

cd packaging
echo Building executable
:: add --debug=all to enable logging output within the application
pyinstaller --uac-admin --onefile ../main.py --log-level ERROR --version-file=file_version_info.txt --add-data "..\venv\Lib\site-packages\pyfiglet;./pyfiglet"
cd ..

if not exist "release" mkdir "release"

echo Copying files to release folder
copy "packaging\dist\main.exe" "release\OverlyPieShaper.exe" 1>NUL
copy "steamids.txt" "release\steamids.txt" 1>NUL

echo Removing packaging folder
rmdir /s /q packaging

echo Zipping up the release
set /p ReleaseVer=<VERSION.txt
set filename=OverlyPieShaper_v%ReleaseVer%.zip
cd release
tar.exe -a -cf %filename% OverlyPieShaper.exe steamids.txt
cd ..

echo Done