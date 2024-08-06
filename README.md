## Success Button

Plays a cute little sound of encouragement to provide you a boost of motivation. I mainly created this application for personal use.


## Build Instructions:
Install pyinstaller:
```
pip install pyinstaller
```

### Then build the exe file:
cd to the directory of this project. Then run the following command.

Windows:
```
pyinstaller --onefile --windowed --add-data "success_sound.mp3;." --add-data "window_icon.png;." --icon=file_icon.ico success_button.py
```

Mac/Linux:
```
pyinstaller --onefile --windowed --add-data "success_sound.mp3:." --add-data "window_icon.png:." --icon=file_icon.ico success_button.py
```

And the desired executable will be in the dist folder.