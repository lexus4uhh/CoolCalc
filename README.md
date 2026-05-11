# CoolCalc

A minimalist popup calculator with a global hotkey. Quickly perform calculations from anywhere without opening a full application.

![Demo](assets/example_rec.gif)

## Features

* Instant access via global hotkey **Ctrl + Alt**
* Supports math expressions (`sin`, `cos`, `sqrt`, etc.)
* Press **Enter** to evaluate expressions
* Always on top of other windows
* Minimalist, translucent UI
* Close with **Esc**

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/CoolCalc.git
cd CoolCalc
```

### 2. Install dependencies

```bash
pip install PyQt6 pynput
```

## Run

```bash
python main.py
```

After launching, the calculator runs in the background.

Press **Ctrl + Alt** to toggle the window.

## Example expressions

```
2 + 2
sqrt(16)
sin(pi / 2)
log(10)
3^3
```

## Security

This project uses `eval` for calculations, but:

* Python built-in functions are disabled
* Only functions from the `math` module are allowed

Still, avoid entering untrusted input.

## Project structure

```
CoolCalc/
├── assets/
│   └── example_rec.gif
├── LICENSE
├── main.py
└── README.md
```

## Requirements

* Python 3.9+
* PyQt6
* pynput

## Ideas for improvement

* Calculation history
* Custom hotkeys
* Themes / UI customization
* Variable support