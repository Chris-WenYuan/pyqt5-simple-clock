# pyqt5-simple-clock

This is a simple clock (with memory feature) example made by pyqt5.

## Development Environment

- **Operation System:** Windows 10
- **Python Version:** v3.8.2
- **PyQt Version:** PyQt 5.14.2

## Directory Tree

```bash
pyqt5-simple-clock
├── App # Exported application
│   ├── ui
│   ├── image
│   ├── save
│   ├── sound
│   └── SimpleHW.exe # Executable file for windowsOS
├── Project # Source code
│   ├── ui
│   ├── image
│   ├── save
│   ├── sound
│   ├── main.py # main program
│   ├── stopwatch.py # Control stopwatch
│   └── countdown.py # Control countdown timer
└── README.md
```

## How to Run?

### 1. For WindowsOS

The source code had been exported as an application in `App` folder, please double click the `SimpleHW.exe` file in the filder.

### 2. For LinuxOS

I haven't exported the source code to an application for LinuxOS, so you have to compile and run by yourself.

```bash
# Install pyqt5 package
$ pip install PyQt5

# Compile and run
$ cd Project
$ python main.py
```

## Result

After you execute the program.

![](https://i.imgur.com/KShMTX0.png)

Here is the stopwatch.

![](https://i.imgur.com/nLbh1vu.png)

Here is the countdown timer.

![](https://i.imgur.com/KTm5H9P.png)