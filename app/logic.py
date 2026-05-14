import sympy as sp

with open('themes.txt', 'r') as f:
    THEMES = {}
    for line in f:
        if line.strip() and not line.startswith("#"):
            name, bg, border, text = line.strip().split(",")
            THEMES[name] = {"background": bg, "border": border, "text": text}


class AppLogic:
    def __init__(self, window):
        self.window = window
        self.memory = []
        self.history = []
        self.history_idx = -1
        self.mode = "exact"

    def process_input(self, text):
        text = text.strip()
        if not text:
            return ""

        if text.startswith("/"):
            return self.execute_command(text[1:])

        return self.calculate(text)

    def calculate(self, expression):
        try:
            expr = expression.replace("^", "**")

            if ";" in expr:
                return self.solve_system(expr)

            if "=" in expr:
                return self.solve_equation(expr)

            if any(op in expr for op in ["<", ">", "<=", ">="]):
                return self.solve_inequality(expr)

            return self.evaluate_expression(expr)

        except Exception as e:
            return "Error"

    def evaluate_expression(self, expr):
        sym_expr = sp.sympify(expr)

        if self.mode == "exact":
            result = sp.nsimplify(sym_expr)
        else:
            result = f"{float(sym_expr.evalf()):.10g}"

        self._save_history(expr, result)
        return str(result)

    def solve_equation(self, expr):
        left, right = expr.split("=")
        eq = sp.Eq(sp.sympify(left), sp.sympify(right))

        symbols = list(eq.free_symbols)

        if not symbols:
            return "No variables"

        sol = sp.solve(eq, symbols)

        self._save_history(expr, sol)
        return str(sol)

    def solve_inequality(self, expr):
        x = list(sp.sympify(expr).free_symbols)

        if not x:
            return "No variables"

        var = x[0]
        ineq = sp.sympify(expr)

        sol = sp.solve_univariate_inequality(ineq, var)

        self._save_history(expr, sol)
        return str(sol)

    def solve_system(self, expr):
        parts = expr.split(";")
        equations = []

        for part in parts:
            part = part.strip()

            if "=" in part:
                left, right = part.split("=")
                equations.append(sp.Eq(sp.sympify(left), sp.sympify(right)))
            else:
                return "System must contain equations"

        symbols = list(set().union(*[eq.free_symbols for eq in equations]))

        sol = sp.solve(equations, symbols, dict=True)

        self._save_history(expr, sol)
        return str(sol)

    def _save_history(self, expr, result):
        self.memory.append(result)
        self.history.append(expr)
        self.history_idx = -1

    def mem_previous(self):
        if not self.history:
            return ""

        if self.history_idx == -1:
            self.history_idx = len(self.history) - 1
        elif self.history_idx > 0:
            self.history_idx -= 1

        return self.history[self.history_idx]

    def mem_next(self):
        if not self.history or self.history_idx == -1:
            return ""

        if self.history_idx < len(self.history) - 1:
            self.history_idx += 1
            return self.history[self.history_idx]

        self.history_idx = -1
        return ""

    def execute_command(self, command_text):
        parts = command_text.split()
        cmd = parts[0].lower()
        args = parts[1:]

        try:
            if cmd == "font" and args:
                size = 12 if args[0] == "reset" else int(args[0])
                self.window.update_font_size(size)
                return f"Font size set to {size}"

            elif cmd == "size" and args:
                if args[0] == "reset":
                    w, h = 250, 60
                else:
                    w = int(args[0]) if args[0] != '~' else self.window.width()
                    h = int(args[1]) if args[1] != '~' else self.window.height()
                self.window.resize(w, h)
                return f"Size set to {w}x{h}"

            elif cmd == "pos" and args:
                if args[0] == "reset":
                    screen = self.window.screen().geometry()
                    x = screen.width() // 2 - self.window.width() // 2
                    y = 100
                else:
                    x = int(args[0]) if args[0] != '~' else self.window.x()
                    y = int(args[1]) if args[1] != '~' else self.window.y()
                self.window.move(x, y)
                return f"Position set to ({x}, {y})"

            elif cmd == "theme" and args:
                try:
                    theme = THEMES[args[0]]
                    self.window.update_colors(
                        theme['background'],
                        theme['border'],
                        theme['text']
                    )
                    return f"Theme set to {args[0]}"
                except KeyError:
                    return f"Theme '{args[0]}' not found"

            elif cmd == "mode" and args:
                self.mode = args[0]
                return f"Mode set to {self.mode}"

            return "Unknown command"

        except Exception as e:
            return f"Cmd Error: {e}"