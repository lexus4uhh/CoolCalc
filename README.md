# CoolCalc

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)

A minimal popup calculator with a global hotkey for quick, distraction-free calculations.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Commands](#commands)
- [Themes](#themes)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [License](#license)

## Features

- **Global Hotkey**: `Alt + Ctrl` to toggle calculator anywhere
- **Customizable Themes**: 15 pre-built color themes
- **Smart Calculation**: Supports symbolic math via SymPy
- **Command System**: Customize font, size, position, and more
- **History Navigation**: Use `Up/Down` arrows to navigate previous expressions
- **Floating Window**: Always-on-top, frameless design

## Prerequisites

- Python 3.9 or higher
- PyQt6
- SymPy
- pynput

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/CoolCalc.git
   cd CoolCalc
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

## Usage

### Basic Calculation

1. Press `Alt + Ctrl` to open the calculator
2. Type a mathematical expression:
   ```
   2 + 2
   3.14 * 2^2
   sqrt(16)
   sin(pi/2)
   ```
3. Press `Enter` to calculate
4. Press `Esc` to hide the window

### Quick Examples

| Expression | Result |
|-----------|--------|
| `2 + 2` | `4` |
| `10 ^ 2` | `100` |
| `sqrt(25)` | `5` |
| `pi * 2` | `2*pi` (exact) or `6.28318...` (default) |

## Configuration

### Commands

Use the `/command` syntax to configure the calculator on-the-fly:

| Command | Syntax | Example |
|---------|--------|---------|
| **Font Size** | `/font <size \| reset>` | `/font 14` or `/font reset` |
| **Window Size** | `/size <width> <height>` | `/size 300 80` or `/size ~ 100` |
| **Position** | `/pos <x> <y>` | `/pos 0 0` or `/pos ~ 200` |
| **Theme** | `/theme <name>` | `/theme neon` |
| **Mode** | `/mode <exact \| default>` | `/mode exact` |

*Use `~` to keep current value when resizing or repositioning.*

## Themes

Available themes are defined in `themes.txt`. Current options:

- `light` – Light gray background
- `dark` – Dark with subtle borders
- `solarized` – Solarized light
- `neon` – Cyberpunk neon
- `pastel` – Soft pastels
- `midnight` – Deep blue night
- `forest` – Green forest theme
- `sunset` – Warm orange/brown
- `ocean` – Cool blue
- `coffee` – Brown tones
- `rose` – Pink vintage
- `slate` – Cool grays
- `amber` – Golden tones
- `lavender` – Purple soft
- `ice` – Cyan ice

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Alt + Ctrl` | Toggle calculator visibility |
| `Enter` | Calculate expression |
| `Esc` | Hide calculator |
| `Up Arrow` | Previous history entry |
| `Down Arrow` | Next history entry |
| `Alt` | Toggle between exact and default mode |