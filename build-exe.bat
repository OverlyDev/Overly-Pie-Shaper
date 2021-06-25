@echo off

echo Creating packaging directory
if not exist "packaging" mkdir "packaging"

create-version-file metadata.yml --outfile packaging/file_version_info.txt

cd packaging
echo Building executable
pyinstaller  --uac-admin  --onefile ../main.py --debug=all --log-level ERROR --version-file=file_version_info.txt
cd ..

if not exist "release" mkdir "release"

echo Copying files to release folder
copy "packaging\dist\main.exe" "release\OverlyPieShaper.exe" 1>NUL
copy "steamids.txt" "release\steamids.txt" 1>NUL

echo Removing packaging folder
rmdir /s /q packaging

echo Done