# CoolCalc

A lightweight, always-on-top calculator application built with PyQt6 and SymPy. Perform calculations, solve equations, and customize the interface with themes and commands.

## Features

- **Mathematical Expressions**: Evaluate complex expressions with support for trigonometric functions, logarithms, etc.
- **Equation Solving**: Solve single equations and systems of equations.
- **Inequality Solving**: Handle inequalities with SymPy.
- **History Navigation**: Use arrow keys to navigate through previous inputs.
- **Commands**: Customize font size, window size, position, theme, and calculation mode.
- **Themes**: Multiple built-in themes for personalization.
- **Hotkey Toggle**: Press `Alt + Ctrl` to show/hide the calculator.
- **Mode Toggle**: Press `Alt` to switch between exact and approximate results.

## Installation

1. Ensure you have Python 3.8+ installed.
2. Install dependencies:
   ```
   pip install PyQt6 sympy pynput
   ```
3. Clone or download the repository.
4. Run the application:
   ```
   python app.py
   ```

## Usage

- **Input Expressions**: Type mathematical expressions, equations (e.g., `x^2 + 2x - 3 = 0`), inequalities, or systems (e.g., `x + y = 5; x - y = 1`).
- **Commands**: Start with `/` followed by the command, e.g., `/theme dark`, `/font 14`, `/size 300 80`.
- **Navigation**: Use `Up`/`Down` arrows for history, `Alt` to toggle mode, `Escape` to hide.
- **Themes**: Edit `themes.txt` to add custom themes.

## Commands

- `/font <size>` or `/font reset`: Set font size.
- `/size <width> <height>` or `/size reset`: Resize window.
- `/pos <x> <y>` or `/pos reset`: Move window position.
- `/theme <name>`: Apply a theme from `themes.txt`.
- `/mode <exact|default>`: Set calculation mode.

## Themes

Themes are defined in `themes.txt`. Each line: `Name,Background,Border,Text`.