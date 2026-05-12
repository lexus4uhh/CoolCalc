# CoolCalc

A minimal popup calculator with a global hotkey for quick, distraction-free calculations.

## Features

* Toggle with **Ctrl + Alt**
* Supports standard math functions (`sin`, `cos`, `sqrt`, etc.)
* Instant evaluation on Enter
* Always-on-top window
* Simple UI with customization commands
* Close with **Esc**

## Installation

```bash
git clone https://github.com/lexusuhh/CoolCalc.git
cd CoolCalc
pip install PyQt6 pynput
```

## Run

```bash
python app.py
```

The app runs in the background. Press **Ctrl + Alt** to show or hide it.

## Usage

Examples:

```
2 + 2
sqrt(16)
sin(pi / 2)
3^3
```

## Commands

```
set font size
/font 16
/font reset

set window size
/size 300 80
/size ~ 100
/size reset

set window position
/pos 500 200
/pos 300 ~
/pos reset

set theme
/theme dark
/theme light
```
## Ideas for improvement

* More commands (for example: custom hotkeys)
* Calculation/command history
* Variable support
* Representation tools (different for approx. and exact answer)
* Add more themes